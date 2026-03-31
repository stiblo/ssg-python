class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        result_string = ""
        if not self.props or self.props == None:
            return ""
        for prop in self.props:
            result_string += f' {prop}="{self.props[prop]}"'
        return result_string

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    

