import unittest

from markdown_to_blocks import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        expected_list = [
'# This is a heading',
'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
'''- This is the first list item in a list block
- This is a list item
- This is another list item'''
        ]       
        text = '''# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item'''
        blocks = markdown_to_blocks(text)
        print('inside test 3', blocks[2])
        print

        self.assertListEqual(blocks, expected_list)

if __name__ == "__main__":
    unittest.main()
