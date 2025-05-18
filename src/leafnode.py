from htmlnode import HTMLNode
from textnode import TextNode, TextType


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    

    def to_html(self):
        if self.value == None:
            raise ValueError("value must not be None")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props=[f'href="{text_node.url}"'])
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props=[f'src="{text_node.url}"', f'alt="{text_node.text}"'])
    raise TypeError(f"Invalid type of TextNode: {text_node}")