from textnode import TextType, TextNode

def test_func(a, b):
    return a + b

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []

    for node in old_nodes:
        new_nodes = []
        text_old_nodes = node.text.split(delimiter)

        if len(text_old_nodes) % 2 == 0:
            raise Exception("invalid markdown: closing delimiters not found")
        
        if node.text_type is not TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue

        for index in range(len(text_old_nodes)):
            if index % 2 == 1:
                new_nodes.append(TextNode(text_old_nodes[index], text_type))
                continue
            new_nodes.append(TextNode(text_old_nodes[index], TextType.PLAIN_TEXT))


        result_list.extend(new_nodes)
                
    return result_list
        

        