import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    # Provided test
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    # Test different text should NOT be equal
    def test_not_eq_text(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Goodbye", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    # Test different text_type should NOT be equal
    def test_not_eq_type(self):
        node1 = TextNode("Same text", TextType.TEXT)
        node2 = TextNode("Same text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    # Test URL default is None and equality still works
    def test_url_none(self):
        node1 = TextNode("Check URL default", TextType.LINK)
        node2 = TextNode("Check URL default", TextType.LINK, None)
        self.assertEqual(node1, node2)

    # Optional extra (good to include): URLs differ → objects NOT equal
    def test_not_eq_url(self):
        node1 = TextNode("URL test", TextType.LINK, "https://example.com")
        node2 = TextNode("URL test", TextType.LINK, "https://different.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
