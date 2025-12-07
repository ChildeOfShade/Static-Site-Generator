import re

def extract_markdown_images(text):
    # Pattern for ![alt text](url)
    pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, text)
    return matches  # already tuples


def extract_markdown_links(text):
    # Pattern for [link text](url)
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, text)

    # But this pattern also matches images, so filter those out
    images = extract_markdown_images(text)
    image_set = set(images)

    # Only return ones that aren't images
    return [m for m in matches if m not in image_set]
