from textnode import TextNode, TextType
import os, shutil
def delete_move():
    root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public_path=os.path.join(root_path,"public")
    static_path=os.path.join(root_path,"static")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.makedirs(public_path)
    copy_static(static_path,public_path)

def copy_static(src_dir,dst_dir):
    for file in os.listdir(src_dir):
        src_path=os.path.join(src_dir,file)
        dst_path = os.path.join(dst_dir, file)
        if os.path.isdir(src_path):
            os.makedirs(dst_path, exist_ok=True)
            copy_static(src_path,dst_path)
        elif os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied: {src_path} -> {dst_path}")

def main():
    delete_move()


main()