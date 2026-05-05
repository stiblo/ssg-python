from copystatic import copy_static_to_public
from generate import generate_page, generate_pages_recursive
import os
import shutil
import sys

static_dir_path = "./static"
public_dir_path = "./docs"
content_dir_path = "./content"
template_path = "./template.html"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory ...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    print(f"Copying static files to public directory ...")
    copy_static_to_public(static_dir_path,public_dir_path)

    generate_pages_recursive(content_dir_path, template_path, public_dir_path, basepath)
    

main()

