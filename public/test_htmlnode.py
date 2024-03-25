import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node1 = HTMLNode("a tag", "a value", None, {"class": "a", "href": "prop"})
        self.assertEqual(node1.props_to_html(),' class= a href= prop',)
        
    def test_to_html_no_children(self):
        node1 = LeafNode("p", "Im a LeafNode")
        self.assertEqual(node1.to_html(), "<p>Im a LeafNode</p>")

    def test_to_html_no_tag(self):
        node1 = LeafNode(None, "Im a LeafNode")
        self.assertEqual(node1.to_html(), "Im a LeafNode")

    def test_to_html_with_children(self):
        child_node1 = LeafNode("p", "Im a LeafNode")
        parent_node1 = ParentNode("hi", [child_node1])
        self.assertEqual(parent_node1.to_html(), "<hi><p>Im a LeafNode</p></hi>")

    def test_to_html_with_2_children(self):
        child_node1 = LeafNode("p", "Im a LeafNode")
        child_node2 = LeafNode("p", "Im a LeafNode too")
        parent_node1 = ParentNode("hi", [child_node1, child_node2])
        self.assertEqual(parent_node1.to_html(), "<hi><p>Im a LeafNode</p><p>Im a LeafNode too</p></hi>")

    def test_to_html_with_parent(self):
        child_node1 = LeafNode("p","LeafNode")
        parent_node1 = ParentNode("hi", [child_node1])
        parent_node2 = ParentNode("hi2",[parent_node1])
        self.assertEqual(parent_node2.to_html(), "<hi2><hi><p>LeafNode</p></hi></hi2>")

    

if __name__ == "__main__":
    unittest.main()