from enum import Enum
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks_list = markdown.split("\n\n")

    filtered_blocks = []

    for block in blocks_list:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks

def block_to_block_type(block):
    
    #HEADERS
    if block.startswith(("#","##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    #CODE BLOCK
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")

    #QUOTE
    if lines[0].startswith((">", "> ")):
        result = True
        for line in lines:
            if line.startswith((">", "> ")) is False:
                result = False
        if result:
            return BlockType.QUOTE
        
    #UNORDERED LIST
    if lines[0].startswith("- "):
        result = True
        for line in lines:
            if line.startswith("- ") is False:
                result = False
        if result:
            return BlockType.UNORDERED_LIST
    
    #ORDERED LIST
    ordered_list_result = False
    for i in range(len(lines)):
        if lines[i].startswith(f"{i + 1}. "):
            ordered_list_result = True
        else:
            return BlockType.PARAGRAPH
    
    if ordered_list_result:
        return BlockType.ORDERED_LIST
    
    #PARAGRAPH 
    
        



