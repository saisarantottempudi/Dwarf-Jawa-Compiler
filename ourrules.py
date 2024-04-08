class Consts(object):
    # Tokens

    # 'var' is for a variable and 'num' is for a number
    tokens = {
        'unit': 'i',
        ' ': 's',
        'main': 'm',
        '(': 'a',
        ')': 'b',
        '\n': 'n',
        'begin': 'e',
        'L': 'l',
        '[': 'g',
        ']': 'h',
        'end': 'w',
        ';': 'c',
        'for': 'f',
        'maxval': 'v',
        '=': 'q',
        '-': 'p',
        '>': 'u',
        'i': 'j',
        'to': 't',
        'num': 'o',
        'n': 'k',
        'do': 'd',
        'if': 'r',
        'endif': 'x',
        'endfor': 'y',
        'return': 'z'

    }

    # Rules
    rules = [
        ['P', 'S'],
        ['S', 'ismabnT'],
        ['T', 'enislgohcnU'],
        ['U', 'lsvqlgohcnV'],
        ['V', 'fsjqostskposdnW'],
        ['W', 'rslgjhuvnX'],
        ['X', 'vqlgjhcnxnY'],
        ['Y', 'ynzavbnwn'],

    ]
