def markdown_to_blocks(markdown):
    blocks_list = markdown.split("\n\n")

    filtered_blocks = []

    for block in blocks_list:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks