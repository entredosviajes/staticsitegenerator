import re

# links
regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_links(text):
    matches = re.findall(regex, text)
    return matches

