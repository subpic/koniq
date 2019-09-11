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
- Read-trained model weights (on SPP features) are available [here](https://www.dropbox.com/s/z6hpj66et6o8rjr/i1%5B768%2C1024%2C3%5D_lSPP_o1%5B2048%5D_r2.h5?dl=1&raw=1).
- The features extracted from KonIQ-10k are available [here](https://www.dropbox.com/s/1c7hkxrhlnzphjg/bsz128_i1%5B18432%5D_imsz%5B768%2C%201024%5D_lcustom_l_o1%5B5%5D_best_weights.h5?dl=1&raw=1).

**`metadata/koniq10k_distributions_sets.csv`**

- Contains image file names, scores, and train/validation/test split assignment (random).

