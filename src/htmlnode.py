class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('to_html not implemented')
    
    def props_to_html(self):
        result_string = ""
        if not self.props or self.props == None:
            return ""
        for prop in self.props:
            result_string += f' {prop}="{self.props[prop]}"'
        return result_string

    def __repr__(self):
        return f'HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError('value not provided, all leaf nodes must have a value')
        if self.tag is None:
            return self.value
        if not self.props or self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        html_props = self.props_to_html()
        return f'<{self.tag}{html_props}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'HTMLNode(tag: {self.tag}, value: {self.value}, props: {self.props})'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid html: tag missing")
        if self.children is None:
            raise ValueError("invalid html: children missing")
        
        html_content = ''

        for child in self.children:
            html_content += child.to_html()
        
        return f'<{self.tag}{self.props_to_html()}>{html_content}</{self.tag}>'
        
    

