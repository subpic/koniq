# KonIQ-10k models 
Deep Learning Models for the KonIQ-10k Image Quality Assessment Database

This is part of the code for the paper ["KonIQ-10k: An ecologically valid database for deep learning of blind image quality assessment"](). The included notebooks rely on the [kutils library](https://github.com/subpic/kutils).

## Overview

Python 2.7 notebooks:

**`train_koncept512.ipynb`**:

- Training and testing code for the KonCept512 model (on KonIQ-10k).
- Ready-trained model weights for [KonCept512](https://www.dropbox.com/s/7ci22gx5c3c8xo3/bsz32_i1%5B384%2C512%2C3%5D_lMSE_o1%5B1%5D_best_weights.h5?dl=1&raw=1
).

**`train_deeprn.ipynb`**

- Reimplementation of the [DeepRN](https://www.uni-konstanz.de/mmsp/pubsys/publishedFiles/VaSaSz18.pdf) model trained on KonIQ-10k, following the advice of the original author, Domonkos Varga.

**`metadata/koniq10k_distributions_sets.csv`**

- Contains image file names, scores, and train/validation/test split assignment (random).

