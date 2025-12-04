import unittest
from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_to_html_grandchildren(self):
        gc = LeafNode("b", "grandchild")
        child = ParentNode("span", [gc])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_multiple_children(self):
        parent = ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " text "),
            LeafNode("i", "Italic")
        ])
        self.assertEqual(parent.to_html(), "<p><b>Bold</b> text <i>Italic</i></p>")

    def test_no_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "hi")])

    def test_no_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_nested_parentnodes(self):
        deep = ParentNode("ul", [
            ParentNode("li", [LeafNode(None, "One")]),
            ParentNode("li", [LeafNode(None, "Two")])
        ])
        self.assertEqual(deep.to_html(), "<ul><li>One</li><li>Two</li></ul>")


if __name__ == "__main__":
    unittest.main()
