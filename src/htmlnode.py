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
