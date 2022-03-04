import argparse

def parser_arguments():
    '''
    Manage the input from the terminal.
    :return: parser
    '''
    parser = argparse.ArgumentParser(description='DeGirum Open Image Dataset Downloader')

    parser.add_argument('--dataset', required=False, default="open-images-v6",
                        help='public datasets')

    parser.add_argument('--dataset-dir', required=False, default="./datasets/OIDv6",
                        help='path to the downloaded datasets')

    parser.add_argument('--export-dir', required=False, default="exported_dataset",
                        help='where to copy the exported dataset dir')

    parser.add_argument('--export-name', required=False, default=None,
                    help='where to copy the exported dataset name')

    parser.add_argument('--label-types', required=False, nargs='+', default=['detections'],
                    help="list of label types: 'detections' or 'classifications' or ...")

    parser.add_argument('--classes', required=True, nargs='+',
                        metavar="list of classes",
                        help="Sequence of 'strings' of the wanted classes")

    parser.add_argument('--splits', required=True, nargs='+',
                        metavar="'train' or 'validation' or 'test'")

    parser.add_argument('--dataset-format', required=False, default='yolov5', choices=['yolov5', 'coco'],
                       help='dataset export format')

    parser.add_argument('--remove-nonoverlap', required=False, action='store_true',
                        help="example: eye and face")

    parser.add_argument('--max-samples', required=False, type=int, nargs='+', default=[None]*3,
                        metavar="integer number",
                        help='Optional limit on number of images to download')

    parser.add_argument('--seed', required=False, type=int, default=None,
                        metavar="integer number")


    return parser.parse_args()
