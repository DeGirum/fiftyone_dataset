import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField as F
from pyparsing import And

# dataset = foz.download_zoo_dataset(
#     "open-images-v6",
#     split=None,
#     splits=None,
#     dataset_dir='./datasets/OIDv6',
#     overwrite=False,
#     cleanup=True,
#     label_types=["detections"],
#     classes = ["Burrito", "Cheese", "Popcorn"],
# )

dataset_dir='./datasets/OIDv6'
classes = ["Human eye", "Human face"]

dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="validation",
    dataset_dir=dataset_dir,
    label_types=["detections"],
    classes = classes,
    dataset_name="open-images-human",
    download_if_necessary=True
)

label_field = "detections"  # for example

import fiftyone as fo

export_dir = "./yolov5-face-eye-dataset3"

# The splits to export
splits = ["validation"]


# The dataset or view to export
# We assume the dataset uses sample tags to encode the splits to export
# Export the splits

filter = F("label").is_in([classes[0]]) & F("label").is_in([classes[1]])

for split in splits:
    split_view = dataset.filter_labels(feild='detections', filter=filter )
    split_view.export(
        export_dir=export_dir,
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=label_field,
        split=split,
        classes=classes,
    )

a=2