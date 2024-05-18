import os
from box.exceptions import BoxValueError
import yaml
import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import sys


"""
reads yaml file and returns
Args:
    path_to_yaml(str): path like input

Raise:
    ValueError: if file is empty
"""
@ensure_annotations  #help to ensure datatype mention in def correctly 
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file :{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise (e,sys)
    


@ensure_annotations
def create_directories(path_to_directories: list,verbos=True):
    # creating list of directories if dir already exists then it will cancelled
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbos:
            logging.info(f"created directory at: {path}")




@ensure_annotations
def get_size(path: Path)-> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} kb"



# configbox can help in acces by . annotation
# dict={key:value}
# instead of dict[key]
# use dict.key with help of configbox