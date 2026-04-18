import unittest

from block_markdown import markdown_to_blocks
from block_markdown import block_to_block_type
from block_markdown import BlockType

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
            md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_md_to_block_type(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

```
this
is a code
block
```

> With a quote
>following

- Just a simple ordered list
- So we can test that out too

1. And an ordered 
2. List to
3. Round it all up

"""        
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))
        
        self.assertListEqual(
             block_types,
             [
                  BlockType.PARAGRAPH,
                  BlockType.PARAGRAPH,
                  BlockType.CODE,
                  BlockType.QUOTE,
                  BlockType.UNORDERED_LIST,
                  BlockType.ORDERED_LIST,
             ]
        )