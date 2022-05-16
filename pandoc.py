from panflute import Header, Strong, Str, run_filters, stringify
from sys import stderr

headers = []

def bold(document):
    document.replace_keyword("BOLD", Strong(Str("BOLD")))

def headerLevel(element, _):
    if isinstance(element, Header) and element.level > 2:
        return Header(Str(stringify(element).upper()), level=element.level)

def headerExists(element, _):
    if isinstance(element, Header):
        text = stringify(element)
        if text in headers:
            print("Warning: duplicate header: " + text, file = stderr)
        else:
            headers.append(text)

if __name__ == "__main__":
    run_filters([headerExists, headerLevel], prepare=bold)