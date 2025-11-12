from markdown_to_blocks import *
from parentnode import *
from leafnode import *
from text_to_textnodes import *
from textnode import *
import re

QUOTE_PATTERN = r'^>\s*(.*)$'
H_PATTERN = r'^(#{1,6})\s*(.*)$'


def text_to_children(text):
    inline_nodes = text_to_textnodes(text)
    html_nodes = []
    for i in inline_nodes:
        if i.text_type == TextType.PLAIN:
            html = LeafNode(None, i.text)
        if i.text_type == TextType.BOLD:
            html = LeafNode('b', i.text)
        if i.text_type == TextType.ITALIC:
            html = LeafNode('i', i.text)
        if i.text_type == TextType.LINK:
            html = LeafNode('a', i.text, {'href': i.url})
        if i.text_type == TextType.IMAGE:
            html = LeafNode('img', '', {'src': i.url, 'alt': i.text})
        if i.text_type == TextType.CODE:
            html = LeafNode('code', i.text)
        html_nodes.append(html)
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            html_node = ParentNode('p', children)
        if block_type == BlockType.QUOTE:
            quoted_lines = re.findall(QUOTE_PATTERN, block, re.MULTILINE)
            html_node = ParentNode('blockquote', quoted_lines)
        if block_type == BlockType.HEADING:
            hashes, content = re.findall(H_PATTERN, block, re.MULTILINE)[0]
            level = len(hashes)
            clean_content = content.strip()
            children = text_to_children(clean_content)
            html_node = ParentNode(f'h{level}', children)
        if block_type == BlockType.CODE:
            print('code block ->', block)
            html_node = LeafNode('code', block.replace('`', ''))
        if block_type == BlockType.UNORDERED_LIST:
            list_items = map(
                lambda x: x.strip(),
                re.findall(r'^[\*\+\-]\s+(.*)$', block, re.MULTILINE)
            )
            lis = []
            for item in list_items:
                children = text_to_children(item)
                lis.append(ParentNode('li', children))
            html_node = ParentNode('ul', lis)
        if block_type == BlockType.ORDERED_LIST:
            list_items = map(
                lambda x: x.strip(),
                re.findall(r'^\d+\.\s+(.*)$', block, re.MULTILINE)
            )
            lis = []
            for item in list_items:
                children = text_to_children(item)
                lis.append(ParentNode('li', children))
            html_node = ParentNode('ol', lis)
        html_nodes.append(html_node)
    return ParentNode('div', html_nodes)
