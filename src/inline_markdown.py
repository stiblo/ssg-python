import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            result_list.append(old_node)
            continue

        split_nodes = []
        node_sections = old_node.text.split(delimiter)

        if len(node_sections) % 2 == 0:
            raise Exception("invalid markdow: syntax invalid, closing delimiter not found")
        
        for i in range(len(node_sections)):
            if node_sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(node_sections[i], TextType.PLAIN_TEXT))
            else:
                split_nodes.append(TextNode(node_sections[i], text_type))
        
        result_list.extend(split_nodes)

    return result_list


def extract_markdown_images(text):
    regex_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern , text)
    return matches

def extract_markdown_links(text):
    regex_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern, text)
    return matches

def split_nodes_image(old_nodes):
    result_list = []
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)

        if node.text_type != TextType.PLAIN_TEXT:
            result_list.append(node)
            continue

        if len(extracted_images) == 0:
            result_list.append(node)
            continue
        
        temp_text = node.text

        for i in range(len(extracted_images)):
            image_alt, image_url = extracted_images[i]
            sections = temp_text.split(f"![{image_alt}]({image_url})")
            if len(sections) != 2:
                raise Exception("invalid markdown: syntax invalid, closing image section not found")
            if sections[0] != "":
                result_list.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            result_list.append(TextNode(image_alt, TextType.IMAGES, image_url))
            
            temp_text = sections[1]

        if temp_text != "":
            result_list.append(TextNode(temp_text, TextType.PLAIN_TEXT))


    return result_list

def split_nodes_link(old_nodes):
    result_list = []
    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)
        
        if node.text_type != TextType.PLAIN_TEXT:
            result_list.append(node)
            continue
    
        if len(extracted_links) == 0:
            result_list.append(node)
            continue
        
        temp_text = node.text

        for i in range(len(extracted_links)):
            link_alt, link_url = extracted_links[i]
            sections = temp_text.split(f"[{link_alt}]({link_url})")
            if len(sections) != 2:
                raise Exception("invalid markdown: syntax invalid, closing link section not found")
            if sections[0] != "":
                result_list.append(TextNode(sections[0], TextType.PLAIN_TEXT))            
            result_list.append(TextNode(link_alt, TextType.LINKS, link_url))
            
            temp_text = sections[1]

        if temp_text != "":
            result_list.append(TextNode(temp_text, TextType.PLAIN_TEXT))

    return result_list

def text_to_textnodes(text):
    result_list = split_nodes_delimiter([TextNode(text, TextType.PLAIN_TEXT)], "_", TextType.ITALIC_TEXT)
    result_list = split_nodes_delimiter(result_list, "**", TextType.BOLD_TEXT)
    result_list = split_nodes_delimiter(result_list, "`", TextType.CODE_TEXT)


    result_list = split_nodes_image(result_list)
    result_list = split_nodes_link(result_list)

    return result_list



        

        