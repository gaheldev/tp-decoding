from shutil import unpack_archive
import os
from os.path import join, isfile
import wget


COMP_LINK = 'https://www.bbci.de/competition/download/competition_iv/BCICIV_4_mat.zip'
EVAL_LINK = 'https://www.bbci.de/competition/iv/results/ds4/true_labels.zip'



def download_bciciv(target_folder):
    comp_archive = join(target_folder, COMP_LINK.split('/')[-1])
    print(f'Downloading {os.path.basename(comp_archive)}...')
    download(COMP_LINK, comp_archive, unsafe=True)

    eval_archive = join(target_folder, EVAL_LINK.split('/')[-1])
    print()
    print(f'Downloading {os.path.basename(eval_archive)}...')
    download(EVAL_LINK, eval_archive, unsafe=True)

    unpack_archive(comp_archive, target_folder)
    unpack_archive(eval_archive, target_folder)

    os.remove(comp_archive)
    os.remove(eval_archive)
    print()
    print('Done')



def download(url, out=None, unsafe=False):
    """ wget wrapper with some safety net

        WARNING: if out exists, it will be removed !!
    """
    try:
        if isfile(out):
            remove(out)
        wget.download(url, out=out)

    except KeyboardInterrupt:
        import sys
        print()
        print("Aborting...")
        sys.exit()

    except:
        if not unsafe:
            raise

        # download even if certificate is invalid
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        wget.download(url, out=out)
