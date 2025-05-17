class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ""
        if self.props != "" and self.props != None and self.props != {}:
            for item in self.props:
                print(item)
                props_string += f' {item}="{self.props[item]}"'
        return props_string
    
    def __eq__(self, node):
        if(self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props):
            return True
        else:
            return False


    def __repr__(self):
        return f"HTMLNode:(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    

    def to_html(self):
        if self.value == None:
            raise ValueError("value must not be None or empty")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html}>{self.value}</{self.tag}>"