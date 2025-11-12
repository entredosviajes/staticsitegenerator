from textnode import *
from copy_dir_content import *
from generate_page import *

def main():
    copy_dir_content('static', 'public')
    generate_page('content/index.md', 'template.html', 'public/index.html')

main()
