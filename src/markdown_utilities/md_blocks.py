def h1(content: str) -> dict:
    return {
        'type': 'h1',
        'content': content
    }

def h2(content: str) -> dict:
    return {
        'type': 'h2',
        'content': content
    }

def h3(content: str) -> dict:
    return {
        'type': 'h3',
        'content': content
    }

def h4(content: str) -> dict:
    return {
        'type': 'h4',
        'content': content
    }

def h5(content: str) -> dict:
    return {
        'type': 'h5',
        'content': content
    }

def h6(content: str) -> dict:
    return {
        'type': 'h6',
        'content': content
    }

def p(content: str) -> dict:
    return {
        'type': 'p',
        'content': content
    }

def code(content: str, language: str = '') -> dict:
    return {
        'type': 'code',
        'content': content,
        'options': {
            'language': language
        }
    }

def ul(content: list, marker: str = '-') -> dict:
    return {
        'type': 'ul',
        'content': content,
        'options': {
            'marker': marker
        }
    }

def ol(content: list) -> dict:
    return {
        'type': 'ol',
        'content': content
    }

def checklist(content: list) -> dict:
    return {
        'type': 'checklist',
        'content': content
    }

def quote(content: str) -> dict:
    return {
        'type': 'quote',
        'content': content
    }

