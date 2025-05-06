# dataset_51
Downloading, loading and manipulating datasets using fiftyone

## Quick Start Examples

```bash
$ git clone https://github.com/DeGirum/fiftyone_dataset
$ cd fiftyone_dataset
$ pip install -r requirements.txt

## example
## For Open Images v6
python main.py --classes "Human face" "Human hand" --splits train validation --max-samples 1000 100
## For Open Images v7
python main_v7.py --classes "Human face" "Human hand" --splits train validation --max-samples 1000 100
