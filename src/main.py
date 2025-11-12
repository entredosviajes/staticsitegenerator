from textnode import *
from copy_dir_content import *
from generate_pages_recursive import *

def main():
    basepath = '/' if len(sys.argv) == 1 else sys.argv[1]
    copy_dir_content('static', 'docs')
    generate_pages_recursive(basepath, 'content', 'template.html', 'docs')

main()
