""" CNN/DM dataset"""
import json
import re
import os
from os.path import join

from torch.utils.data import Dataset


class CnnDmDataset(Dataset):
    def __init__(self, split: str, path: str) -> None:
        print("SUYASH_ Dataset class created")
        assert split in ['train', 'val', 'test']
        self._data_path = join(path, split)
        self._n_data = _count_data(self._data_path)
		 
    def __len__(self) -> int:
        return self._n_data

    def __getitem__(self, i: int):
        with open(join(self._data_path, '{}.json'.format(i))) as f: # edited here  .story  /.json
            #js =  f.read()
            js = json.loads(f.read())
        return js


def _count_data(path):
    """ count number of data in the given path"""
    matcher = re.compile(r'[0-9]+\.json')#edited here
    match = lambda name: bool(matcher.match(name))
    names = os.listdir(path)
    n_data = len(list(filter(match, names))) #edited here: 
    return n_data  # edited here
