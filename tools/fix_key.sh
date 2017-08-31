Original_Train_LMDB=/data/jiecaoyu/imagenet/lmdb/ilsvrc12_train_lmdb_badkey/
Original_Val_LMDB=/data/jiecaoyu/imagenet/lmdb/ilsvrc12_val_lmdb_badkey/

Target_Train_LMDB=/data/jiecaoyu/imagenet/lmdb/ilsvrc12_train_lmdb/
Target_Val_LMDB=/data/jiecaoyu/imagenet/lmdb/ilsvrc12_val_lmdb/

python convert_key.py --source $Original_Train_LMDB --target $Target_Train_LMDB
python convert_key.py --source $Original_Val_LMDB --target $Target_Val_LMDB
