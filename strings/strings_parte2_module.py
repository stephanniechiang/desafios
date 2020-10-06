import re, textwrap

def plugin_main(*args, **kwargs):
    text = args[0]
    width = args[1]

    text_lines = lines(text, width)
    final_text = ''
    for line in text_lines:
        final_text += justify_string(line,width)
        final_text += '\n'

    print(final_text)
    return final_text
    
def lines(text, width=40):
    whitespace = set(" \n\t\r")
    length = len(text)
    start = 0

    while start < (length - width):
        text_slice = text[start:start+width+1]
        
        if '\n' in text_slice:
            end = start + text_slice.find('\n')
            yield text[start:end]
            start = end+1 
            continue

        for i, ch in enumerate(reversed(text_slice)):
            if ch in whitespace:
                end = (start+width-i)
                yield text[start:end]
                start = end + 1
                break
            else:
                continue 
    yield text[start:]

def items_len(l):
    return sum([ len(x) for x in l] )

lead_re = re.compile(r'(^\s+)(.*)$')

def justify_string(s, width, last_paragraph_line=0):
    m = lead_re.match(s) 
    if m is None:
        left, right, w = '', s, width
    else:
        left, right, w = m.group(1), m.group(2), width - len(m.group(1))

    items = right.split()

    for i in range(len(items) - 1):
        items[i] += ' '

    if not last_paragraph_line:
        left_count = w - items_len(items)
        while left_count > 0 and len(items) > 1:
            for i in range(len(items) - 1):
                items[i] += ' '
                left_count -= 1
                if left_count < 1:  
                    break

    res = left + ''.join(items)
    return res