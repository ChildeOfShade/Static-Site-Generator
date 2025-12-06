import unittest
from textnode import TextNode, TextType, split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):

    def test_basic_code_split(self):
        node = TextNode("Hello `code` block", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[1].text, "code")

    def test_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[1].text, "bold")

    def test_italic_split(self):
        node = TextNode("Here is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(result[1].text_type, TextType.ITALIC)

    def test_no_delimiter_no_change(self):
        node = TextNode("No formatting here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result[0].text, "No formatting here")
        self.assertEqual(len(result), 1)

    def test_error_if_no_closing_tag(self):
        node = TextNode("This has `no end", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
