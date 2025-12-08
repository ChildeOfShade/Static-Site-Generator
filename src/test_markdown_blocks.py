from markdown_blocks import block_to_block_type
from blocktypes import BlockType

def test_heading():
    assert block_to_block_type("# Hello") == BlockType.HEADING

def test_code_block():
    assert block_to_block_type("```\ncode here\n```") == BlockType.CODE

def test_quote_block():
    assert block_to_block_type("> quote line\n> another") == BlockType.QUOTE

def test_unordered_list():
    assert block_to_block_type("- one\n- two\n- three") == BlockType.UNORDERED_LIST

def test_ordered_list():
    assert block_to_block_type("1. first\n2. second\n3. third") == BlockType.ORDERED_LIST

def test_paragraph():
    assert block_to_block_type("Just a regular text block.") == BlockType.PARAGRAPH


def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)

    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )
