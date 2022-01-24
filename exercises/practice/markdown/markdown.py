import re
def parse(markdown):
    """ Markup
Input: would be a markdown phrase for an example
Output: expected to pass a HTML equivalent for the same
Sample: "#exercism.org is a useful practice ground"
you syntax should return <h1>exercism.org is a useful practice ground </h1>
Hint: Try exporing regular expressions. Makes life simple
"""
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        '''
        handle other cases here similar to <h6>
        '''
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                '''
                handle the cases here too
                '''
            '''
            handle other cases here also
            '''
        else:
            if in_list:
                in_list_append = True
                in_list = False
        m = re.match('<h|<ul|<p|<li', i)
        '''
        handle more cases here too
        '''
    if in_list:
        res += '</ul>'
    return res