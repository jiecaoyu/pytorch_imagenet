The implementation in Torch Vision is not actually accurate. In this case, this repository reimplements some of the networks for the author's usage.

# Pre-requirements
- [Caffe](https://github.com/BVLC/caffe)
- [PyTorch](https://github.com/pytorch/pytorch)

# Data Preparation
The original data loader ([link](https://github.com/pytorch/vision#imagenet-12)) is slow. Therefore, I build a new data loader with Caffe utils.
# AlexNet
