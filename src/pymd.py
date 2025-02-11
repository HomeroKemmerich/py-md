def dict_to_md(obj: dict):
    """
    Convert a dictionary to a markdown file.
    """
    md = ''
    for key, value in obj.items():
        if key[0] == 'h':
            md += f'{"#" * int(key[1])} {value}\n\n'
        elif key == 'p':
            md += f'{value}\n\n'
        elif key == 'ul':
            for item in value:
                md += f'- {item}\n'
            md += '\n'
        elif key == 'ol':
            for i, item in enumerate(value):
                md += f'{i + 1}. {item}\n'
            md += '\n'

    return md