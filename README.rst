SEQmil: Biomolecular multi-instance machine learning
====================================================================

``SEQmil`` is a Python package for applying **Multi-Instance Learning (MIL)** to biological sequences such as **RNA, DNA, and proteins**.
It enables flexible representation of sequences as bags of subsequences, and supports learning tasks where only bag-level labels
are available.


Key Features
------------

- 🧬 MIL support for biological sequences (RNA, DNA, Proteins)
- 🧩 Instance construction using sliding windows or domain-based segmentation
- 🛠️ Compatible with scikit-learn, PyTorch, and standard ML tools
- 📊 Integrated tutorial and example workflow

Installation
------------

Set up a clean environment and install the package:

.. code-block:: bash

   # Create and activate a new environment
   conda create -n seqmil python=3.9 -y
   conda activate seqmil

   # Install SEQmil from GitHub
   pip install git+https://github.com/KagakuAI/SEQmil.git


Quick start
------------

See the examples of ``SEQmil`` application for different tasks in the `tutorial collection <tutorials>`_ .