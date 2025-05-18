import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode, text_node_to_html_node
from parentnode import ParentNode
from textnode import TextNode
from textnode import TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq_a(self):
        #tag=None, value=None, children=None, props=None
        prop = {"href":"https://www.google.com", "target":"_blank"}
        prop2 = {"href":"https://www.google.com", "target":"_blank"}
        html = HTMLNode(tag="a",props=prop)
        html2 = HTMLNode(tag="a",props=prop2)
        
        self.assertEqual(html, html2)

    def test_eq_prop(self):
        prop = {"href":"https://www.google.com", "target":"_blank"}
        html = HTMLNode(tag="a",props=prop)

        self.assertEqual(html.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_eq_string_representation(self):
        self.maxDiff = None
        prop = {"href":"https://www.google.com", "target":"_blank"}
        child_html = HTMLNode(tag="p", value="This is a paragraph")
        child_html2 = HTMLNode(tag="p", value="This is different!")
        html = HTMLNode(tag="a", value="55", props=prop, children=[child_html, child_html2])



        self.assertEqual(html.__repr__(), 'HTMLNode:(tag: a, value: 55, children: [HTMLNode:(tag: p, value: This is a paragraph, children: None, props: None), HTMLNode:(tag: p, value: This is different!, children: None, props: None)], props: {\'href\': \'https://www.google.com\', \'target\': \'_blank\'})')
        # return f"HTMLNode:(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


    def test_eq_child(self):
        #tag=None, value=None, children=None, props=None


        child_html = HTMLNode(tag="p", value="This is a paragraph")
        child_html2 = HTMLNode(tag="p", value="This is a paragraph")
        child_html3 = HTMLNode(tag="p", value="This is wrong!")
        child_html4 = HTMLNode(tag="p", value="This is different!")
        child_html5 = HTMLNode(tag="p", value="This is different!")



        html = HTMLNode(tag="p",children=[child_html])
        html2 = HTMLNode(tag="p",children=[child_html2])
        html3 = HTMLNode(tag="p",children=[child_html3])
        html4 = HTMLNode(tag="p",children=[child_html, child_html4])
        html5 = HTMLNode(tag="p",children=[child_html2, child_html5])
        
        self.assertEqual(html, html2)
        self.assertEqual(html4, html5)

        self.assertNotEqual(html, html4)
        self.assertNotEqual(html, html3)

    def test_eq_tag(self):
        html = HTMLNode(tag="p", value="This is a paragraph")
        html2 = HTMLNode(tag="p", value="This is a paragraph")
        html3 = HTMLNode(tag="a", value="This is wrong!")

        self.assertEqual(html, html2)
        self.assertNotEqual(html, html3)



class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value_error(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
        #self.assertEqual(node.to_html(), "Hello, world!")
    


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")


    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props[0], 'href="www.google.com"')

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "www.google.com/img/test.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props[0], 'src="www.google.com/img/test.jpg"')
        self.assertEqual(html_node.props[1], 'alt="This is a text node"')




class TestParnetNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild_A")
        grandchild_node2 = LeafNode("i", "grandchild_B")
        grandchild_node3 = LeafNode("i", "grandchild_C")
        grandchild_node4 = LeafNode("b", "grandchild_D")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        child_node2 = ParentNode("div", [grandchild_node3, grandchild_node4], {"color": "red", "align": "right"})
        child_node3 = LeafNode("b", "childnode")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), '<div><span><b>grandchild_A</b><i>grandchild_B</i></span><div color="red" align="right"><i>grandchild_C</i><b>grandchild_D</b></div><b>childnode</b></div>')

if __name__ == "__main__":
    unittest.main()