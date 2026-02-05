from textnode import *

def main():
    test_node = TextNode("This is some sample text", TextType.LINKS, "https://www.boot.dev")
    output = test_node.__repr__()
    print(output)

main()
