def extract_title(markdown):
    lines=markdown.split('\n')
    for i in lines:
        if i.lstrip().startswith('# '):
            s=i.lstrip()
            return s[2:].strip()    
    raise ValueError("no 1 heading aka title") 