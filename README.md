## NR-IQA models trained on the KonIQ-10k dataset

This is part of the code for the paper ["KonIQ-10k: An ecologically valid database for deep learning of blind image quality assessment"](https://arxiv.org/abs/1910.06180). The included Python 2.7 notebooks rely on the [kutils library](https://github.com/subpic/kutils). The Google colab requires the [ku library](https://github.com/subpic/ku). Project data is available for download from [osf.io](https://osf.io/hcsdy/). 

Please cite the following paper if you use the code:
```
@article{koniq10k,
author={V. {Hosu} and H. {Lin} and T. {Sziranyi} and D. {Saupe}},
journal={IEEE Transactions on Image Processing},
title={KonIQ-10k: An Ecologically Valid Database for Deep Learning of Blind Image Quality Assessment},
year={2020},
volume={29},
pages={4041-4056}}
```

## Overview

Google colab notebook, Python 3 compatible:

**[koncept512_train_test_py3.ipynb](https://github.com/subpic/koniq/blob/master/koncept512_train_test_py3.ipynb)** *(updated May 2020)*
- Download KonIQ-10k dataset, train the KonCept512 model and test it
- Load a pre-trained KonCept512 model, and use it to predict the quality of an image

Python 2.7 notebooks:

**[train_koncept512.ipynb](https://github.com/subpic/koniq/blob/master/train_koncept512.ipynb), [train_koncept224.ipynb](https://github.com/subpic/koniq/blob/master/train_koncept224.ipynb)**:

- Training and testing code for the KonCept512 and KonCept224 model (on KonIQ-10k).
- Ready-trained model weights for [KonCept512](https://osf.io/uznf8/download) and [KonCept224](https://osf.io/cxtyp/download).

**[train_deeprn.ipynb](https://github.com/subpic/koniq/blob/master/train_deeprn.ipynb)**

- Reimplementation of the [DeepRN](https://www.uni-konstanz.de/mmsp/pubsys/publishedFiles/VaSaSz18.pdf) model trained on KonIQ-10k, following the advice of the original author, Domonkos Varga.
- Re-trained model weights (on SPP features) are available [here](https://osf.io/avyd5/download).
- The features extracted from KonIQ-10k are available [here](https://osf.io/y6brn/download).

**[metadata/koniq10k_distributions_sets.csv](https://github.com/subpic/koniq/blob/master/metadata/koniq10k_distributions_sets.csv)**

- Contains image file names, scores, and train/validation/test split assignment (random).

