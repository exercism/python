import re


def parse_markdown(markdown):
    lines = markdown.split('\n')
    html = ''
    in_list = False
    for line in lines:
        res = parse_line(line, in_list)
        html += res['line']
        in_list = res['in_list']
    if in_list:
        html += '</ul>'
    return html


def wrap(line, tag):
    return '<{tag}>{line}</{tag}>'.format(line=line, tag=tag)


def check_headers(line):
    pattern = '# (.*)'
    for i in range(6):
        if re.match(pattern, line):
            return wrap(line[(i + 2):], 'h' + str(i + 1))
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


def parse_line(line, in_list):
    res = check_headers(line)

    list_match = re.match(r'\* (.*)', res)

    if (list_match):
        if not in_list:
            res = '<ul>' + wrap(list_match.group(1), 'li')
            in_list = True
        else:
            res = wrap(list_match.group(1), 'li')
    else:
        if in_list:
            res += '</ul>'
            in_list = False

    if not re.match('<h|<ul|<li', res):
        res = wrap(res, 'p')

    if list_match is None:
        res = re.sub('(.*)(<li>)(.*)(</li>)(.*)', r'\1\2<p>\3</p>\4\5', res)

    while check_bold(res):
        res = check_bold(res)
    while check_italic(res):
        res = check_italic(res)

    return {
        'line': res,
        'in_list': in_list
    }
