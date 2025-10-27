import numpy as np
from abc import ABC, abstractmethod

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

class Featurizer(ABC):
    """Abstract base class for sequence featurizers."""

    @abstractmethod
    def run(self, sequences):
        """
        Takes a list of sequences and returns a list (or array) of encoded vectors.
        """
        pass

class OneHotFeaturizer(Featurizer):
    """One-hot featurization of amino acid sequences."""

    def __init__(self, amino_acids=AMINO_ACIDS):
        self.amino_acids = amino_acids
        self.aa_to_idx = {aa: i for i, aa in enumerate(amino_acids)}

    def encode_one(self, seq):
        """Encode a single amino acid sequence to a flattened one-hot vector."""
        vec = np.zeros((len(seq), len(self.amino_acids)))
        for i, aa in enumerate(seq):
            if aa in self.aa_to_idx:
                vec[i, self.aa_to_idx[aa]] = 1.0
        return vec.flatten()

    def run(self, sequences):
        """Encode a list of sequences to one-hot vectors."""
        return [self.encode_one(seq) for seq in sequences]
