import cnn_finetune.resnet_101
from cnn_finetune.resnet_101 import resnet101_model

def preprocess_input_resnet101(x):
    """For preprocessing specific to `cnn_finetune`"""
    # Switch RGB to BGR order 
    x = x[..., ::-1]
    x[..., 0] -= 103.939
    x[..., 1] -= 116.779
    x[..., 2] -= 123.68   
    return x


