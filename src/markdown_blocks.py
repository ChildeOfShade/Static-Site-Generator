import re
from blocktypes import BlockType

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # Code block → starts and ends with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Heading → 1–6 #'s then space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    # Quote → every line begins with >
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list → every line begins with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list → each line must be:
    # 1. X. text   (incrementing number per line)
    ordered = True
    for i, line in enumerate(lines, start=1):
        if not re.match(fr"^{i}\. ", line):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    # Default → paragraph
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    # Split on double-newlines
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        clean = block.strip()

        # Skip empty results caused by multiple newlines
        if clean:
            blocks.append(clean)

    return blocks
