def plugin_main(*args, **kwargs):
    text = args[0]
    width = args[1]

    text_lines = lines(text, width)
    final_text = ''
    for line in text_lines:
        final_text += line
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



    