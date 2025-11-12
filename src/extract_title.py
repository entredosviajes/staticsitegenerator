import re

H1_PATTERN = r"^#\s(.*)$"

def extract_title(markdown):
    match = re.search(H1_PATTERN, markdown, re.MULTILINE)
    if not match:
        raise Exception('no title')
    clean_content = match.group(1).strip()
    return clean_content


