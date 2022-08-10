import os
import yaml

def correct_dataset_yaml(export_dir, export_name):

    dataset_yaml_path = os.path.join(export_dir, export_name, 'dataset.yaml')
    train_abs_path = os.path.abspath( os.path.join(export_dir, export_name, 'images/train') )
    validation_abs_path = os.path.abspath( os.path.join(export_dir, export_name, 'images/validation') )
    out_yaml_abs_path = os.path.abspath( os.path.join(export_dir, export_name, 'dataset_c.yaml') )
    with open(dataset_yaml_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        yaml_dict = yaml.load(file, Loader=yaml.FullLoader)

        if 'validation' in yaml_dict.keys():
            yaml_dict['val'] = yaml_dict.pop('validation')
            yaml_dict['val'] = validation_abs_path

        if 'train' in yaml_dict.keys():
            yaml_dict['train'] = train_abs_path
            
        
        with open(out_yaml_abs_path, 'w') as file:
            yaml.dump(yaml_dict, file)
    
    return out_yaml_abs_path
