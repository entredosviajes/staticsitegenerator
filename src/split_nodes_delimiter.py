from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception('Unmatched delimiter')
        for i in range(0, len(parts)):
            new_nodes.append(TextNode(parts[i], TextType.PLAIN if i % 2 == 0 else text_type))
    return new_nodes

