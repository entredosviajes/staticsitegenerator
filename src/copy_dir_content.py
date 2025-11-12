import os
import shutil
import sys

def copy_dir_content(src, dest):
    print(src, os.path.exists(src), os.path.isfile(src), os.path.isdir(src))
    print(dest, os.path.exists(dest), os.path.isfile(dest), os.path.isdir(dest))
    if not os.path.isdir(src):
        raise Exception('Source is not a dir')
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for f in os.listdir(src):
        src_full = os.path.join(src, f)
        dest_full = os.path.join(dest, f)
        if os.path.isfile(src_full):
            shutil.copy(src_full, dest_full)
        elif os.path.isdir(src_full):
            copy_dir_content(src_full, dest_full)
