The implementation of AlexNet in [PyTorch Vision](https://github.com/pytorch/vision) is not actually the ordinary version. In this case, this repository reimplements some of the networks for the author's usage.

# Pre-requirements
- [Caffe](https://github.com/BVLC/caffe)
- [PyTorch](https://github.com/pytorch/pytorch)

# Data Preparation
The original data loader ([link](https://github.com/pytorch/vision#imagenet-12)) is slow. Therefore, I build a new data loader with Caffe utils.
### Genearte LMDB
Follow the [instructions](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html) for Caffe to build the LMDB dataset of ImageNet. However, the ```key``` used in the LMDB dataset is not suitable for accessing. Therefore, please use the script ```./tools/fix_key.sh``` to convert the keys.
Preprocessed data will be available soon.
### Load LMDB
Please change the variable ```lmdb_dir``` in ```./datasets/folder.py``` to the directory which includes the training and validating LMDB datasets.
# AlexNet
The implementation is in ```./networks/model_list/alexnet.py```. Since PyTorch does not support local response normalization (LRN) layer, I implements it also. The trained model will be available soon.
