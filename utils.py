
import glob
from pathlib import Path
import os

import numpy as np

def label_list(export_dir : str):
    
    labels = []
    export_dir = Path(export_dir)
    if export_dir.is_dir():  # dir
        labels += glob.glob(str(export_dir / 'labels' / '*' / '*.*'), recursive=True)
    else:
        raise Exception(f'{export_dir} does not exist')

    return labels

def find_overlapping_labels(labels : list, nc : int ):
    
    overlap_labels = []
    nonoverlap_labels = []
    for lb_file in labels:
        with open(lb_file, 'r') as f:
            l = [x.split() for x in f.read().strip().splitlines() if len(x)]
        l = np.array(l, dtype=np.float32)
        if np.unique(l[:,0]).size == nc:
            overlap_labels.append(lb_file)
        else:
            nonoverlap_labels.append(lb_file)

    return overlap_labels, nonoverlap_labels

def img2label_paths(img_paths):
    # Define label paths as a function of image paths
    sa, sb = os.sep + 'images' + os.sep, os.sep + 'labels' + os.sep  # /images/, /labels/ substrings
    return [sb.join(x.rsplit(sa, 1)).rsplit('.', 1)[0] + '.txt' for x in img_paths]

def label2img_paths(label_paths):
    # Define label paths as a function of image paths
    sa, sb = os.sep + 'images' + os.sep, os.sep + 'labels' + os.sep  # /images/, /labels/ substrings
    return [sa.join(x.rsplit(sb, 1)).rsplit('.', 1)[0] + '.jpg' for x in label_paths]

def label2img_path(label_path):
    # Define label paths as a function of image paths
    sa, sb = os.sep + 'images' + os.sep, os.sep + 'labels' + os.sep  # /images/, /labels/ substrings
    img_path_no_ext = sa.join(label_path.rsplit(sb, 1)).rsplit('.', 1)[0]
    img_path = glob.glob(str(img_path_no_ext + '.*'), recursive=True)
    return img_path


def remove_nonoverlap_imgs_labels(export_dir : str, nc : int):
    labels = label_list(export_dir)

    _, noll = find_overlapping_labels(labels, nc)

    for f in noll:
        os.remove(f)
        img_path = label2img_path(f)
        for img_f in img_path:
            os.remove(img_f)

def gen_export_name(classes : list):
    export_name = ''
    for cl in classes:
        export_name += cl.replace(" ", "_")
        export_name += '-'
    
    return export_name