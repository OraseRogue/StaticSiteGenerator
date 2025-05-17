import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    
    def test_ne(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        

    def test_eq_method(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK)
        node4 = TextNode("This is a new text", TextType.LINK)
        node5 = TextNode("This is a text node", TextType.LINK, "http://google.com")
        node6 = TextNode("This is a text node", TextType.LINK, "http://google.com")
        node7 = TextNode("This is a new text", TextType.LINK, "http://google.com")


        self.assertTrue(node.__eq__(node2))
        self.assertFalse(node.__eq__(node3))
        self.assertFalse(node3.__eq__(node4))

        self.assertTrue(node5.__eq__(node6))
        self.assertFalse(node5.__eq__(node7))
        self.assertFalse(node5.__eq__(node))

    def test_string_representation(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK, "http://google.com")
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, bold, None)")
        self.assertEqual(node2.__repr__(), "TextNode(This is a text node, link, http://google.com)")



if __name__ == "__main__":
    unittest.main()