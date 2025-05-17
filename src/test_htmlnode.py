import unittest

from htmlnode import HTMLNode


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



       

if __name__ == "__main__":
    unittest.main()