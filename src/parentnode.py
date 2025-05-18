from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("tag must not be None")
        elif self.children == None or self.children == []:
            raise ValueError("Children must not be None or empty")
        else:
            childString = ""
            for child in self.children:
                childString += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{childString}</{self.tag}>"