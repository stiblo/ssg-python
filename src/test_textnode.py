import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a dummy text", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a dummy text", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def text_neq_url(self):
        node = TextNode("This is a dummy image", TextType.IMAGES, "https://imgs.xkcd.com/comics/satellite_pollution_2x.png")
        node2 = TextNode("This is a dummy image", TextType.IMAGES, None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()