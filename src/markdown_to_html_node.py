from blocktype import BlockType
from htmlnode import HTMLNode
from text_to_nodes import text_to_textnodes
from textnode_to_html_node import text_node_to_html_node
from markdown_blocks import markdown_to_blocks, block_to_block_type   # if separate modules

############################################################
# Convert full markdown doc → HTMLNode <div> containing children
############################################################

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html(block))

        elif block_type == BlockType.HEADING:
            children.append(heading_to_html(block))

        elif block_type == BlockType.CODE:
            children.append(codeblock_to_html(block))

        elif block_type == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html(block))

        elif block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html(block))

        elif block_type == BlockType.QUOTE:
            children.append(quote_to_html(block))

    return HTMLNode("div", children=children)


############################################################
# Inline → HTML child list generator
############################################################

def text_to_children(text: str) -> list[HTMLNode]:
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in nodes]


############################################################
# Block conversions
############################################################

def paragraph_to_html(block: str) -> HTMLNode:
    # Paragraphs can span multiple lines → join with spaces
    text = " ".join(block.split("\n"))
    return HTMLNode("p", children=text_to_children(text))


def heading_to_html(block: str) -> HTMLNode:
    level = 0
    while level < len(block) and block[level] == "#":
        level += 1
    text = block[level:].strip()
    return HTMLNode(f"h{level}", children=text_to_children(text))


def codeblock_to_html(block: str) -> HTMLNode:
    # Strip ``` fence lines cleanly
    stripped = block.strip()[3:-3].strip("\n")
    code = HTMLNode("code", value=stripped + "\n")  # newline preserved for tests
    return HTMLNode("pre", children=[code])


def unordered_list_to_html(block: str) -> HTMLNode:
    items = block.split("\n")
    li_nodes = []
    for item in items:
        li_nodes.append(HTMLNode("li", children=text_to_children(item[2:])))
    return HTMLNode("ul", children=li_nodes)


def ordered_list_to_html(block: str) -> HTMLNode:
    items = block.split("\n")
    li_nodes = []
    for item in items:
        # Remove "1. " format
        text = item.split(". ", 1)[1]
        li_nodes.append(HTMLNode("li", children=text_to_children(text)))
    return HTMLNode("ol", children=li_nodes)


def quote_to_html(block: str) -> HTMLNode:
    lines = [line[1:].strip() for line in block.split("\n")]
    text = " ".join(lines)
    return HTMLNode("blockquote", children=text_to_children(text))
