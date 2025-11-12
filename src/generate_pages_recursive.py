import os
from generate_page import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for f in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, f)
        full_dest = os.path.join(dest_dir_path, f.replace('.md', '.html'))
        if os.path.isfile(full_path):
            if not os.path.exists(full_dest):
                os.makedirs(dest_dir_path, exist_ok=True)
            generate_page(full_path, template_path, full_dest)
        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, full_dest)
