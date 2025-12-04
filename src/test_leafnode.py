import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_link(self):
        node = LeafNode("a", "Click", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click</a>')

    def test_leaf_raises_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("span", None)

    def test_leaf_with_props_multiple(self):
        node = LeafNode("img", "image", {"src": "file.jpg", "alt": "test"})
        self.assertEqual(node.to_html(), '<img src="file.jpg" alt="test">image</img>')


if __name__ == "__main__":
    unittest.main()

