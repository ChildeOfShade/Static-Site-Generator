from textnode import TextNode, TextType
from copy_static import copy_static

def main():
    copy_static()
    print("Static files copied successfully!")
    node = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev"
    )
    print(node)

if __name__ == "__main__":
    main()
