import os

from . import data
from . import downloader
from .utils import * # make all utils directly accesible by calling tp.<utils-func>
from .plots import *




def load_data(path):
    return data.Dataset(path)



def dataset_exists(path):
    if not os.path.isdir(path):
        return False

    files = os.listdir(path)
    for i in range(1,4):
        if f'sub{i}_comp.mat' not in files:
            return False

        if f'sub{i}_testlabels.mat' not in files:
            return False

    return True



def download_dataset(target_folder):
    os.makedirs(target_folder, exist_ok=True)
    downloader.download_bciciv(target_folder)
