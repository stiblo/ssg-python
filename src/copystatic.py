import os
import shutil

def copy_static_to_public(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    if not os.path.exists(source_dir):
        raise Exception("source directory does not exist")
    
    source_content = os.listdir(source_dir)
    if len(source_content) == 0:
        raise Exception("source directory is empty")
    
    for i in source_content:
        source_path = os.path.join(source_dir, i)
        dest_path = os.path.join(dest_dir, i)
        if os.path.isfile(source_path):
            print(f"- {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            copy_static_to_public(source_path, dest_path)