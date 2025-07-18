SEQmil: Biomolecular Multi-Instance Machine Learning
====================================================================

``SEQmil`` is a Python package for applying **Multi-Instance Learning (MIL)** to biological sequences such as **RNA, DNA, and proteins**.
It enables flexible representation of sequences as bags of subsequences, and supports learning tasks where only bag-level labels
are available.


Key Features
------------

- 🧬 MIL support for biological sequences (RNA, DNA, Proteins)
- 🧩 Instance construction using sliding windows
- 🛠️ Compatible with scikit-learn, PyTorch, and standard ML tools
- 📊 Integrated tutorial and example workflow

Installation
------------

``SEQmil`` can be installed using conda/mamba package managers.

.. code-block:: bash

    git clone https://github.com/KagakuAI/SEQmil.git
    conda env create -f SEQmil/conda/seqmil_linux.yml
    conda activate seqmil

The installed ``SEQmil`` environment can then be added to the Jupyter platform:

.. code-block:: bash

    conda install ipykernel
    python -m ipykernel install --user --name seqmil --display-name "seqmil"


Quick start
------------

See the examples of ``SEQmil`` application for different tasks in the `tutorial collection <tutorials>`_ .