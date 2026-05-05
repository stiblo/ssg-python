import os
from markdown import markdown_to_html_node
from markdown import extract_title

from pathlib import Path


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    source_file = open(from_path, "r")
    source_file_content = source_file.read()
    source_file.close()

    template_file = open(template_path, "r")
    template_file_content = template_file.read()
    template_file.close()

    source_file_html_node = markdown_to_html_node(source_file_content)
    page_title = extract_title(source_file_content)

    finished_page = template_file_content.replace("{{ Title }}", page_title)
    finished_page = finished_page.replace("{{ Content }}", source_file_html_node.to_html())

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    write_file = open(dest_path, "w")
    write_file.write(finished_page)
    write_file.close()

def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    source_contents = os.listdir(content_dir_path)

    if len(source_contents) == 0:
        raise Exception("content dir empty")
    
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for i in source_contents:
        source_path = os.path.join(content_dir_path, i)
        dest_path = os.path.join(dest_dir_path, i)
        if os.path.isfile(source_path):
            generate_page(source_path, template_path, Path(dest_path).with_suffix(".html"))
        else:
            generate_pages_recursive(source_path, template_path ,dest_path)

