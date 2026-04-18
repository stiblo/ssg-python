from block_markdown import markdown_to_blocks
from block_markdown import block_to_block_type
from block_markdown import BlockType
from htmlnode import ParentNode,LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)

    node_blocks = []

    for md_block in md_blocks:
        block_type = block_to_block_type(md_block)
        match block_type:
            case BlockType.HEADING:
                heading_node = md_heading_to_html_node(md_block)
                node_blocks.append(heading_node)
            case BlockType.UNORDERED_LIST:
                node_blocks.append(md_list_to_html_node(md_block, BlockType.UNORDERED_LIST))
            case BlockType.ORDERED_LIST:
                node_blocks.append(md_list_to_html_node(md_block, BlockType.ORDERED_LIST))
            case BlockType.PARAGRAPH:
                child_nodes = text_to_children(md_block.replace("\n", " "))
                node_blocks.append(ParentNode("p", child_nodes))
            case BlockType.QUOTE:
                node_blocks.append(md_quote_to_html_node(md_block))
            case BlockType.CODE:
                node_blocks.append(md_code_to_html_node(md_block))

    return ParentNode("div", node_blocks)
                
def text_to_children(text):
    list_of_children = text_to_textnodes(text)
    children_nodes = []
    for child in list_of_children:
        children_nodes.append(text_node_to_html_node(child))
    return children_nodes

def md_code_to_html_node(md_block):
    block_text = md_block.removeprefix("```\n")
    block_text = block_text.removesuffix("```") 
    block_text_node = text_node_to_html_node(TextNode(block_text, TextType.PLAIN_TEXT))
    return ParentNode("pre", [ParentNode("code", [block_text_node])])

def md_quote_to_html_node(md_block):
    block_lines = md_block.split("\n")
    quote_inline_text = []
    for line in block_lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        quote_inline_text.append(line.lstrip(">").strip())
    content = " ".join(quote_inline_text)
    children_nodes = text_to_children(content)
    return ParentNode("blockquote", children_nodes)

def md_list_to_html_node(md_block, list_type):
    list_element_nodes = []
    match list_type:
        case BlockType.UNORDERED_LIST:
            list_elements = md_block.split("\n")
            for element in list_elements:
                list_element_node_children = text_to_children(element[2:])
                list_element_node_parent = ParentNode("li", list_element_node_children)
                list_element_nodes.append(list_element_node_parent)
            return ParentNode("ul", list_element_nodes)
        case BlockType.ORDERED_LIST:
            list_elements = md_block.split("\n")
            for element in list_elements:
                list_element_node_children = text_to_children(element[3:])
                list_element_node_parent = ParentNode("li", list_element_node_children)
                list_element_nodes.append(list_element_node_parent)
            return ParentNode("ol", list_element_nodes)


def md_heading_to_html_node(md_block):
    if md_block.startswith("###### "):
        node_children = text_to_children(md_block[7:])
        return ParentNode("h6", node_children)
    elif md_block.startswith("##### "):
        node_children = text_to_children(md_block[6:])
        return ParentNode("h5", node_children)
    elif md_block.startswith("#### "):
        node_children = text_to_children(md_block[5:])
        return ParentNode("h4", node_children)
    elif md_block.startswith("### "):
        node_children = text_to_children(md_block[4:])
        return ParentNode("h3", node_children)
    elif md_block.startswith("## "):
        node_children = text_to_children(md_block[3:])
        return ParentNode("h2", node_children)
    elif md_block.startswith("# "):
        node_children = text_to_children(md_block[2:])
        return ParentNode("h1", node_children)
    else:
        raise ValueError("invalid header start syntax")
    
    