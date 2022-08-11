# dataset_51
Downloading, loading and manipulating datasets using fiftyone

## Quick Start Examples

```bash
$ git clone https://github.com/khatami-mehrdad/dataset_51.git
$ cd dataset_51
$ pip install -r requirements.txt

## example
python main.py --classes "Human face" "Human hand" --splits train validation --max-samples 1000 100
