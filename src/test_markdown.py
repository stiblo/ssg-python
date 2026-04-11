import unittest

from markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestMarkdown(unittest.TestCase):
    def test_init(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            new_nodes[0],
            TextNode("This is text with a ", TextType.PLAIN_TEXT)
        )
        self.assertEqual(
            new_nodes[1],
            TextNode("code block", TextType.CODE_TEXT)
        )
        


if __name__ == "__main__":
    unittest.main()