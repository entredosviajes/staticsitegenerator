from textnode import *
from copy_dir_content import *
from generate_pages_recursive import *

def main():
    copy_dir_content('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')

main()
