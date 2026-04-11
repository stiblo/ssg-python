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
        

        