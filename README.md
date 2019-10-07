# KonIQ-10k models 
Deep Learning Models for the KonIQ-10k Image Quality Assessment Database

This is part of the code for the paper ["KonIQ-10k: An ecologically valid database for deep learning of blind image quality assessment"](). The included notebooks rely on the [kutils library](https://github.com/subpic/kutils). Project data is available for download from [osf.io](https://osf.io/hcsdy/).

## Overview

Python 2.7 notebooks:

**`train_koncept512.ipynb`, `train_koncept224.ipynb`**:

- Training and testing code for the KonCept512 and KonCept224 model (on KonIQ-10k).
- Ready-trained model weights for [KonCept512](https://osf.io/uznf8/download) and [KonCept224](https://osf.io/cxtyp/download).

**`train_deeprn.ipynb`**

- Reimplementation of the [DeepRN](https://www.uni-konstanz.de/mmsp/pubsys/publishedFiles/VaSaSz18.pdf) model trained on KonIQ-10k, following the advice of the original author, Domonkos Varga.
- Re-trained model weights (on SPP features) are available [here](https://osf.io/avyd5/download).
- The features extracted from KonIQ-10k are available [here](https://osf.io/y6brn/download).

**`metadata/koniq10k_distributions_sets.csv`**

- Contains image file names, scores, and train/validation/test split assignment (random).

