import unittest

from inline_markdown import split_nodes_delimiter
from inline_markdown import extract_markdown_images
from inline_markdown import extract_markdown_links
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

    def test_delimiter_italic(self):
        node = TextNode("This is a text with _italic_ word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertListEqual(
            [
                TextNode("This is a text with ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word", TextType.PLAIN_TEXT),
            ],
            new_nodes
        )

    def test_delimiter_code(self):
        node = TextNode("This is a `text with` some code", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.PLAIN_TEXT),
                TextNode("text with", TextType.CODE_TEXT),
                TextNode(" some code", TextType.PLAIN_TEXT),
            ],
            new_nodes
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)
    

        


if __name__ == "__main__":
    unittest.main()