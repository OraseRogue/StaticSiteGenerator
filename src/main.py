from textnode import *


def main():
    test_textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_textnode.__repr__())
    

main()