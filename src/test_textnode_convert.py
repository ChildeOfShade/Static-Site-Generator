import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode



class TestTextNodeConversion(unittest.TestCase):

    def test_text(self):
        node = TextNode("Hello", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "Hello")

    def test_bold(self):
        node = TextNode("Bold!", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "Bold!")

    def test_italic(self):
        node = TextNode("Italic", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "Italic")

    def test_code(self):
        node = TextNode("print('hi')", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "code")

    def test_link(self):
        node = TextNode("Google", TextType.LINK, "https://google.com")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.props["href"], "https://google.com")

    def test_image(self):
        node = TextNode("cat picture", TextType.IMAGE, "cat.png")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.props["src"], "cat.png")
        self.assertEqual(html.props["alt"], "cat picture")

    def test_invalid_type_raises(self):
        node = TextNode("Unknown", "INVALID")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
