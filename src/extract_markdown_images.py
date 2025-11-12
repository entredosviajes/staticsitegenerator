import re

# links
regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_images(text):
    matches = re.findall(regex, text)
    return matches

