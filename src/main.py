from textnode import TextNode, TextType
from gencontent import generate_page
import os, shutil
from gen_page_rec import generate_pages_recursive
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
def blog_passage(name):
    root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    from_path= os.path.join(root, "content","blog",f"{name}","index.md")
    template_path=os.path.join(root,"template.html")
    dest_path=os.path.join(root,"public","blog",f"{name}","index.html")
    generate_page(from_path, template_path, dest_path)   
def main():
    delete_move()
    root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    from_path= os.path.join(root, "content")
    template_path=os.path.join(root,"template.html")
    dest_path=os.path.join(root,"public")
    generate_pages_recursive(from_path,template_path,dest_path)
if __name__ == "__main__":
    main()