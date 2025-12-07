import unittest
from textnode import TextNode, TextType
from text_to_nodes import text_to_textnodes


class TestTextToNodes(unittest.TestCase):

    def test_full_parse(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi](link1) and a [site](link2)"
        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi", TextType.IMAGE, "link1"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("site", TextType.LINK, "link2"),
        ])
