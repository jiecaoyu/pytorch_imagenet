import caffe
import lmdb
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Convert dataset key')
parser.add_argument('--target', default=None, action='store',
        help='target directory')
parser.add_argument('--source', default=None, action='store',
        help='target directory')
args = parser.parse_args()

print '\n===========================\nConverting keys from:'
print '\t'+args.source
print ' to:'
print '\t'+args.target+'\n'

# read source
source_env = lmdb.open(args.source, readonly=True)
source_txn = source_env.begin()
source_cursor = source_txn.cursor()

# clean remaining target directory
subprocess.call('rm -r '+args.target, shell=True)
target_env = lmdb.open(args.target, map_size=int(1e12))
target_txn = target_env.begin(write=True)
batch_size = 1000

item_id = -1
for key, value in source_cursor:
    item_id += 1
    key_str = key[0:8]
    target_txn.put( key_str, value )
    
    # write batch
    if(item_id + 1) % batch_size == 0:
        target_txn.commit()
        target_txn = target_env.begin(write=True)
        print (item_id + 1)

# write last batch
if (item_id+1) % batch_size != 0:
    target_txn.commit()
    print 'last batch'
    print (item_id + 1)
source_env.close()
