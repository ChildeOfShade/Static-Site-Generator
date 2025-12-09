import os
import shutil

def copy_static(src="static", dest="public"):
    # 1. Remove old `public` directory completely
    if os.path.exists(dest):
        shutil.rmtree(dest)

    # 2. Create fresh public directory
    os.mkdir(dest)

    # 3. Recursively copy everything
    recursive_copy(src, dest)


def recursive_copy(src, dest):
    for entry in os.listdir(src):
        src_path = os.path.join(src, entry)
        dest_path = os.path.join(dest, entry)

        # If it's a directory → make folder + recurse
        if os.path.isdir(src_path):
            os.mkdir(dest_path)
            print(f"[DIR]  {dest_path}")   # not required, but VERY helpful
            recursive_copy(src_path, dest_path)

        # If it's a file → copy directly
        else:
            shutil.copy(src_path, dest_path)
            print(f"[FILE] {dest_path}")
