import re
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []
    pattern = r"!\[([^\]]+)\]\(([^)]+)\)"   # groups: (alt)(url)

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(pattern, text))

        if not matches:
            new_nodes.append(node)
            continue

        idx = 0
        for match in matches:
            start, end = match.span()
            alt, url = match.groups()

            if start > idx:
                new_nodes.append(TextNode(text[idx:start], TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            idx = end

        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"    # groups: (text)(url)

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(pattern, text))

        if not matches:
            new_nodes.append(node)
            continue

        idx = 0
        for match in matches:
            start, end = match.span()
            anchor, url = match.groups()

            if start > idx:
                new_nodes.append(TextNode(text[idx:start], TextType.TEXT))

            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            idx = end

        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split raw TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)

        # If count of delimiter splits is even → unbalanced markdown
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {text}")

        # Rebuild split results into TextNodes
        for i, part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))       # outside delimiter
            else:
                new_nodes.append(TextNode(part, text_type))           # inside delimiter

    return new_nodes
