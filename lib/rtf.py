from __future__ import absolute_import


def to_rtf(body, fields):
    """Construct a rtf document from two plain

    :param body: type str, text intended to be split up by newlines, inserted at top of rtf document
    :param fields: type str, lines of key/value pairs which will be split by newline and then by colon

    rtf document start char {rtf1
    rtf document newline: /line/
    rft document format: \bBOLDTEXT\b0
    rtf document end char: }

    fyi: docstrings tend to do weird things when mixing curlys, newlines and escapes
    """

    result = ''
    result += """{\\rtf1
"""
    line_fmt_field = """\\b {0}\\b0: {1}\line\ """
    line_fmt_body = """{0} \line\ """

    for line in body.split('\n'):
        if len(line) > 0:
            result += line_fmt_body.format(line)

    result += """ \line\ """

    for line in fields.split('\n'):
        if ':' in line:
            name, desc = line.split(':')
            result += line_fmt_field.format(name.strip(), desc.strip())

    result += """}
    """
    return result
