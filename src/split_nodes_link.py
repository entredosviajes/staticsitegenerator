from textnode import *
from extract_markdown_links import *

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        parts = extract_markdown_links(node.text)
        if len(parts) == 0:
            new_nodes.append(node)
            continue
        sections = []
        for part in parts:
            sections = (node.text if len(sections) == 0 else sections[-1]).split(f"[{part[0]}]({part[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(TextNode(part[0], TextType.LINK, part[1]))

    return new_nodes

