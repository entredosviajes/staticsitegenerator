class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or len(list(self.props)) == 0:
            return ""
        return "".join(map(lambda x: f' {x}="{self.props[x]}"', self.props))

    def __repr__(self):
        props_part = self.props_to_html()
        children_and_closing_tag = f'>{self.children}</{self.tag}>' if self.children != None and len(list(self.children)) > 0 else f'>{self.value}</{self.tag}>' if self.value != None else '/>'
        return f'<{self.tag}{props_part}{children_and_closing_tag}'
