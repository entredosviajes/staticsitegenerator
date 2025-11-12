import os
from markdown_to_html_node import *
from extract_title import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(template_path, "r") as f:
        template_string = f.read()
    with open(from_path, "r") as f:
        from_string = f.read()
    node = markdown_to_html_node(from_string)
    html = node.to_html()
    print('ZE', html)
    title = extract_title(from_string)
    template_string = template_string.replace('{{ Title }}', title).replace('{{ Content }}', html)
    with open(dest_path, "w") as f:
        f.write(template_string)

#generate_page('content/index.md', 'template.html', '')
