import os
from gencontent import generate_page
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    content_dir= os.listdir(dir_path_content)
    for dir in content_dir:
        full_path=os.path.join(dir_path_content,dir)
        if os.path.isdir(full_path):
            dest_subdir = os.path.join(dest_dir_path, dir)
            os.makedirs(dest_subdir, exist_ok=True)
            generate_pages_recursive(full_path,template_path,dest_subdir)
        elif os.path.isfile(full_path):
            rel = os.path.relpath(full_path, dir_path_content)
            base, ext = os.path.splitext(rel)
            if ext.lower() != ".md":
                continue
            html_rel = base + ".html"
            dest_path = os.path.join(dest_dir_path, html_rel)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            generate_page(full_path, template_path, dest_path)

    
       