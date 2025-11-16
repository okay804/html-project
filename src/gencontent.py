from markdown_blocks import markdown_to_html_node 
from extract_title import extract_title
import os
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} -> {dest_path} using {template_path}")
    # python
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_text=f.read()
    html_string=markdown_to_html_node(markdown_text).to_html()
    title=extract_title(markdown_text)
    page_html=template_text.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    dirpath = os.path.dirname(dest_path)
    os.makedirs(dirpath, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f: 
        f.write(page_html)

