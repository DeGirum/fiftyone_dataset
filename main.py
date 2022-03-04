import os
from tkinter.messagebox import NO
os.system("rm -r ~/.fiftyone")

import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField as F
from parser import parser_arguments
from utils import remove_nonoverlap_imgs_labels, gen_export_name

if __name__ == '__main__':

    args = parser_arguments()

    export_name = gen_export_name(args.classes) if args.export_name == None else args.export_name
    ####
    # download or loading the dataset
    dataset = foz.load_zoo_dataset(
        args.dataset,
        splits=args.splits,
        dataset_dir=args.dataset_dir,
        label_types=args.label_types,
        classes = args.classes,
        dataset_name=export_name,
        download_if_necessary=True,
        max_samples=args.max_samples,
        seed=args.seed,
    )
    ####
    # exporting to a new dataset
    if (args.dataset_format == 'yolov5'):
        dataset_type = fo.types.YOLOv5Dataset
    elif (args.dataset_format == 'coco'):
        dataset_type = fo.types.COCODetectionDataset

    export_path = args.export_dir
    export_path = os.path.join(args.export_dir, export_name)

    filter = F("label").is_in(args.classes)
    for field in args.label_types:
        for split in args.splits:
            split_view = dataset.filter_labels(field=field, filter=filter )
            split_view.export(
                export_dir=export_path,
                dataset_type=dataset_type,
                label_field=field,
                split=split,
                classes=args.classes,
            )

    if (args.remove_nonoverlap):
        remove_nonoverlap_imgs_labels(export_path, args.classes.__len__())

