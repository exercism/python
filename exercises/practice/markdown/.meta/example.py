import re


def parse(markdown):
    lines = markdown.split('\n')
    html = ''
    in_list = False
    in_list_append = False
    for line in lines:
        result = parse_line(line, in_list, in_list_append)
        html += result['line']
        in_list = result['in_list']
        in_list_append = result['in_list_append']
    if in_list:
        html += '</ul>'
    return html


def wrap(line, tag):
    return '<{tag}>{line}</{tag}>'.format(line=line, tag=tag)


def check_headers(line):
    pattern = '# (.*)'
    for index in range(6):
        if re.match(pattern, line):
            return wrap(line[(index + 2):], 'h' + str(index + 1))
        pattern = '#' + pattern
    return line


def check_bold(line):
    bold_pattern = '(.*)__(.*)__(.*)'
    bold_match = re.match(bold_pattern, line)
    if bold_match:
        return bold_match.group(1) + wrap(bold_match.group(2), 'strong')\
            + bold_match.group(3)
    else:
        return None


def check_italic(line):
    italic_pattern = '(.*)_(.*)_(.*)'
    italic_match = re.match(italic_pattern, line)
    if italic_match:
        return italic_match.group(1) + wrap(italic_match.group(2), 'em')\
            + italic_match.group(3)
    else:
        return None


def parse_line(line, in_list, in_list_append):
    result = check_headers(line)

    list_match = re.match(r'\* (.*)', result)

    if list_match:
        if not in_list:
            result = '<ul>' + wrap(list_match.group(1), 'li')
            in_list = True
        else:
            result = wrap(list_match.group(1), 'li')
    else:
        if in_list:
            in_list_append = True
            in_list = False

    if not re.match('<h|<ul|<li', result):
        result = wrap(result, 'p')

    if list_match is None:
        result = re.sub('(.*)(<li>)(.*)(</li>)(.*)',
                        r'\1\2<p>\3</p>\4\5', result)

    while check_bold(result):
        result = check_bold(result)
    while check_italic(result):
        result = check_italic(result)

    if in_list_append:
        result = '</ul>' + result
        in_list_append = False

    return {
        'line': result,
        'in_list': in_list,
        'in_list_append': in_list_append
    }
