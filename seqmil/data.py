import numpy as np
import random

# ==== Parameters ====
AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

# ==== Core generation utils ====
def generate_protein(length, amino_acids=AMINO_ACIDS):
    return "".join(random.choices(amino_acids, k=length))


def embed_motif(protein, motif):
    start = random.randint(0, len(protein) - len(motif))
    return protein[:start] + motif + protein[start + len(motif):], start


def sliding_windows(protein, window, step):
    return [protein[i:i+window] for i in range(0, len(protein) - window + 1, step)]

# ==== Protein Pair Generation ====
def generate_protein_pair_with_motif(is_positive, motif_pair, protein_length, window, step):
    p1 = generate_protein(protein_length)
    p2 = generate_protein(protein_length)
    key_indices = []
    motifs = None

    if is_positive:
        if motif_pair is None:
            raise ValueError("motif_pair must be provided for positive bags.")
        motif1, motif2 = motif_pair

        p1, _ = embed_motif(p1, motif1)
        p2, _ = embed_motif(p2, motif2)

        subseqs1 = sliding_windows(p1, window, step)
        subseqs2 = sliding_windows(p2, window, step)

        for i, s1 in enumerate(subseqs1):
            if motif1 in s1:
                for j, s2 in enumerate(subseqs2):
                    if motif2 in s2:
                        key_indices.append(i * len(subseqs2) + j)

        motifs = (motif1, motif2)

    return p1, p2, key_indices, motifs

def generate_negative_protein_pair(protein_length, window, step, motif_pairs):
    """Generate a motif-free protein pair."""
    while True:
        p1 = generate_protein(protein_length)
        p2 = generate_protein(protein_length)
        subseqs1 = sliding_windows(p1, window, step)
        subseqs2 = sliding_windows(p2, window, step)

        motif_present = False
        for m1, m2 in motif_pairs:
            if any(m1 in s for s in subseqs1) or any(m2 in s for s in subseqs2):
                motif_present = True
                break

        if not motif_present:
            return p1, p2

# ==== Bag Construction ====
def create_bag_and_keys(p1, p2, key_indices, motifs, window, step):
    subseqs1 = sliding_windows(p1, window, step)
    subseqs2 = sliding_windows(p2, window, step)

    bag = []
    key_instance_indices = []

    for i, s1 in enumerate(subseqs1):
        for j, s2 in enumerate(subseqs2):
            bag.append((s1, s2))
            if key_indices and (i * len(subseqs2) + j) in key_indices:
                key_instance_indices.append(len(bag) - 1)

    return {
        "raw_bag": bag,  # list of (s1, s2) tuples
        "label": 1 if key_indices else 0,
        "key_indices": key_instance_indices,
        "protein_1": p1,
        "protein_2": p2,
        "subseqs_1": subseqs1,
        "subseqs_2": subseqs2,
        "motifs": motifs
    }

# ==== Dataset Generation ====
def create_ppi_dataset(
    n_bags=1000,
    pos_ratio=0.5,
    protein_length=50,
    window_size=10,
    step_size=3,
    motif_pairs=None,
    seed=42,
):
    if motif_pairs is None or len(motif_pairs) == 0:
        raise ValueError("motif_pairs must be provided as a non-empty list of tuples.")

    random.seed(seed)
    np.random.seed(seed)

    n_pos = int(n_bags * pos_ratio)
    n_neg = n_bags - n_pos
    bags = []

    for i in range(n_pos):
        motif_pair = random.choice(motif_pairs)
        p1, p2, key_indices, motifs = generate_protein_pair_with_motif(
            True, motif_pair, protein_length, window_size, step_size
        )
        bag_data = create_bag_and_keys(p1, p2, key_indices, motifs, window_size, step_size)
        bags.append(bag_data)

    for i in range(n_neg):
        p1, p2 = generate_negative_protein_pair(protein_length, window_size, step_size, motif_pairs)
        bag_data = create_bag_and_keys(p1, p2, None, None, window_size, step_size)
        bags.append(bag_data)

    return bags
