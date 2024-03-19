from urllib.request import urlretrieve
from shutil import unpack_archive
import os
from os.path import join


COMP_LINK = 'https://www.bbci.de/competition/download/competition_iv/BCICIV_4_mat.zip'
EVAL_LINK = 'https://www.bbci.de/competition/iv/results/ds4/true_labels.zip'



def download_bciciv(target_folder):
    comp_archive = join(target_folder, COMP_LINK.split('/')[-1])
    print(f'Downloading {os.path.basename(comp_archive)}...')
    retrieve(COMP_LINK, comp_archive)

    eval_archive = join(target_folder, EVAL_LINK.split('/')[-1])
    print(f'Downloading {os.path.basename(eval_archive)}...')
    retrieve(EVAL_LINK, eval_archive)

    unpack_archive(comp_archive, target_folder)
    unpack_archive(eval_archive, target_folder)

    os.remove(comp_archive)
    os.remove(eval_archive)
    print('Done')



def retrieve(url, to_file):
    try:
        urlretrieve(url, to_file)
    except:
        # the website's certificate is expired, let's use an unsafe download
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        urlretrieve(url, to_file)
