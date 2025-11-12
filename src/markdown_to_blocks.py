import re
from enum import Enum

HEADING_PATTERN = r'(#{1,6}\s+.+)'
CODE_BLOCK_PATTERN = r'```(?:\w*)\s*```'
QUOTE_PATTERN = r'>\s?.*'
UNORDERED_LIST_PATTERN = r'-\s{1}.+'
ORDERED_LIST_PATTERN = r'\d+\.\s{1}.+'

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = map(lambda x: x.strip(), blocks)
    blocks = filter(lambda x: x != "", blocks)
    res = list(blocks)
    return res

def block_to_block_type(markdown):
    if re.findall(CODE_BLOCK_PATTERN, markdown):
        return BlockType.CODE
    if re.findall(QUOTE_PATTERN, markdown):
        return BlockType.QUOTE
    if re.findall(UNORDERED_LIST_PATTERN, markdown):
        return BlockType.UNORDERED_LIST
    if re.findall(ORDERED_LIST_PATTERN, markdown):
        return BlockType.ORDERED_LIST
    if re.findall(HEADING_PATTERN, markdown):
        return BlockType.HEADING
    return BlockType.PARAGRAPH
