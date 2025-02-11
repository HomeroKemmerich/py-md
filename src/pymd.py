NEW_LINE = '\n\n'

from md_blocks import *

def dict_to_md(blocks: list):
    """
    Convert a dictionary to a markdown file.
    """
    md = ''
    for block in blocks:
        if block['type'].startswith('h'):
            md += f'{"#" * int(block["type"][1:])} {block["content"]}{NEW_LINE}'
        elif block['type'] == 'p':
            md += f'{block["content"]}{NEW_LINE}'
        elif block['type'] == 'code':
            md += f'```{block["options"]["language"]}\n{block["content"]}\n```{NEW_LINE}'
        elif block['type'] == 'ul':
            for item in block['content']:
                md += f'{block["options"]["marker"]} {item}\n'
            md += '\n'
        elif block['type'] == 'ol':
            for item in block['content']:
                md += f'1. {item}\n'
            md += '\n'

    return md