import unittest

from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p")
        self.assertEqual(node.props_to_html(), "")

    def test_one_prop(self):
        node = HTMLNode("p", "Hi there!", None, {"color": "red"})
        self.assertEqual(node.props_to_html(), ' color="red"')

    def test_two_props(self):
        node = HTMLNode("a", "This is a link", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()
