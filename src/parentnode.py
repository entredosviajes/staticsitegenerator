from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children)
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError('tag is missing')
        if self.children == None:
            raise ValueError('children is missing')
        props = self.props_to_html()
        childrenStr = ''
        for child in self.children:
            print(child)
            childrenStr += child.to_html()
        return f"<{self.tag}{props}>{childrenStr}</{self.tag}>"


