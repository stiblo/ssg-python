import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here!", {"href": "https://stiblo.net"})
        self.assertEqual(node.to_html(), '<a href="https://stiblo.net">Click here!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("h3","About me"),
                LeafNode(None,"I am who I am ..."),
                LeafNode("b", " and I am just testing the feature out ..."),
                LeafNode("i", " so I need a lot of children nodes."),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><h3>About me</h3>I am who I am ...<b> and I am just testing the feature out ...</b><i> so I need a lot of children nodes.</i></div>"
        )
        
    def test_to_html_multiple_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "h3",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("b", "Bold text"),
                    ],
                ),
                ParentNode(
                    "h4",
                    [
                        LeafNode("i", "Italic text"),
                        LeafNode(None, "Normal text")
                    ],
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><h3>Normal text<b>Bold text</b></h3><h4><i>Italic text</i>Normal text</h4></div>"
        )

    

if __name__ == "__main__":
    unittest.main()