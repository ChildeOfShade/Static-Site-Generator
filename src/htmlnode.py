class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """To be overridden by subclasses later."""
        raise NotImplementedError("to_html() must be implemented by subclass")

    def props_to_html(self):
        """Return HTML attribute string with leading spaces. Example:
           props {"href": "site", "target": "_blank"} → ' href="site" target="_blank"'
        """
        if not self.props:
            return ""
        return "".join(f' {key}="{val}"' for key, val in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Force NO children + require tag+value
        super().__init__(tag=tag, value=value, children=None, props=props)

        if value is None:
            raise ValueError("LeafNode must have a value")

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode has no value")

        # Raw text if no tag
        if self.tag is None:
            return self.value

        # Render tag with optional props
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("parenNode must have a tag")
        if children is None or len(children) == 0:
            raise ValueError("ParentNode must have at least one child")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        if not self.children:
            raise ValueError("ParentNode must have children")
        
        inner_html = "".join(child.to_html() for child in self.children)
        props_str = self.props_to_html()

        return f"<{self.tag}{props_str}>{inner_html}</{self.tag}>"