import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_2(self):
        node = HTMLNode()
        node.props = {"href":"https://boot.dev", "title":"Bootdev"}
        expected_node = ' href="https://boot.dev" title="Bootdev"'
        self.assertEqual(node.props_to_html(), expected_node)

    def test_props_to_html_1(self):
        node = HTMLNode()
        node.props = {"href":"https://boot.dev"}
        expected_node = ' href="https://boot.dev"'
        self.assertEqual(node.props_to_html(), expected_node)

    def test_empty_props(self):
        node = HTMLNode()
        expected_node = ""
        self.assertEqual(node.props_to_html(), expected_node)

    def test_repr(self):
        node = HTMLNode("p","This is a dummy value", None, {'class':'primary'})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag: p, value: This is a dummy value, children: None, props: {'class': 'primary'})"
        )
        

    

if __name__ == "__main__":
    unittest.main()