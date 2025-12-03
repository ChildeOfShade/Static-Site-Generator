import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_basic(self):
        node = HTMLNode("a", "Click", None, {"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "Link", None, {
            "href": "https://google.com",
            "target": "_blank"
        })
        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )

    def test_props_to_html_none(self):
        node = HTMLNode("p", "hello")
        self.assertEqual(node.props_to_html(), "")

    # Optional but recommended extra test: __repr__
    def test_repr(self):
        node = HTMLNode("p", "Hello")
        self.assertIn("HTMLNode", repr(node))
        self.assertIn("Hello", repr(node))


if __name__ == "__main__":
    unittest.main()
