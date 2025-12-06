from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    # Safety check: must be a TextNode-like object
    if not hasattr(text_node, "text_type"):
        raise ValueError("Invalid input: expected a TextNode")

    t = text_node.text_type

    if t == TextType.TEXT:
        return LeafNode(None, text_node.text)

    elif t == TextType.BOLD:
        return LeafNode("b", text_node.text)

    elif t == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    elif t == TextType.CODE:
        return LeafNode("code", text_node.text)

    elif t == TextType.LINK:
        if not text_node.url:
            raise ValueError("LINK TextNodes must contain a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})

    elif t == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("IMAGE TextNodes must contain a URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    else:
        raise Exception(f"Unknown TextType: {t}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split raw TEXT nodes — leave others unchanged
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # If delimiter not present → no splitting needed
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        # Split the text by delimiter
        split_text = node.text.split(delimiter)

        # If we don't have an even number of delimiters → missing closing tag
        if len(split_text) % 2 == 0:
            raise Exception(f"Invalid markdown, no closing delimiter for {delimiter}")

        # Build new nodes — alternate TEXT, special, TEXT, special, ...
        for i, chunk in enumerate(split_text):
            if i % 2 == 0:  # even index = normal text
                if chunk:
                    new_nodes.append(TextNode(chunk, TextType.TEXT))
            else:           # odd index = formatted text
                new_nodes.append(TextNode(chunk, text_type))

    return new_nodes