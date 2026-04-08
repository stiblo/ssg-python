import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_link_text(self):
        node = TextNode("Learn more", TextType.LINKS, "https://en.wikipedia.org/wiki/Library_of_Alexandria")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://en.wikipedia.org/wiki/Library_of_Alexandria">Learn more</a>'
            )
        
    def test_img_text(self):
        node = TextNode("Dummy image", TextType.IMAGES, "https://imgs.xkcd.com/comics/satellite_pollution_2x.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://imgs.xkcd.com/comics/satellite_pollution_2x.png" alt="Dummy image"></img>'
        )

if __name__ == "__main__":
    unittest.main()