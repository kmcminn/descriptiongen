from __future__ import absolute_import

import re
import string


class LTemplate(string.Formatter):
    """Formatter class which enables a custom string format for use with product
    descriptions.

    Both keys/values for specifications are most often capitalized and it better to
    leave them in their natural format and have the templates for rendering descriptions
    make sure that the strings get the right treatment instead of pushing them to a higher
    level in the application.

    Example:

        template = "The {name} is available in {color:l}"
        data = { 'name': 'Cuddle Bear', 'color': 'Blue' }
        print LTemplate().format(template, **data)
    """
    def format_field(self, value, spec):
        if spec.endswith('l'):
            value = value.lower()
            spec = spec[:-1] + 's'
        return super(LTemplate, self).format_field(value, spec)


def formatter_tokens(text):
    formatter = string.Formatter()
    tokens = []
    for segment in formatter.parse(text):
        if type(segment) is not tuple:
            continue
        _text, _key, _fmt, _rr = segment
        if _key is not None:
            tokens.append(_key)
    return tokens


def is_valid_data_for_template(template, template_inputs):
    for key in formatter_tokens(template):
        if key not in template_inputs:
            return False, key

    return True, None


def simplestr(text):
    """convert a string into a scrubbed lower snakecase. Intended use is converting
    human typed field names deterministically into a string that can be used for a
    key lookup.

    :param text: type str text to be converted
    """
    text = text.strip()
    text = text.replace(' ', '_')
    text = text.lower()
    return re.sub('\W+', '', text)


def to_lines(text):
    """Convert any text to a list of strings less all surrounding whitespace and
    only if it contains some chars

    :param text: type str loose text
    """
    final = []
    lines = text.split("\n")
    for line in lines:
        ll = line.strip()
        if len(ll) > 0:
            final.append(ll)
    return final


def parse_colon_lines(lines):
    """convert a list of strings into a dict converting the key use simplestr

    :param lines: type list the list of strings to be converted
    """
    result = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':')
            result[simplestr(key)] = value.strip()

    return result


def upper_all(line):
    words = [word.upper() for word in line.split()]
    return ' '.join(words)


def capitalize_all(line):
    words = [word.capitalize() for word in line.split()]
    return ' '.join(words)


def repr_dict(dict_obj):
    """Human readable repr for a dictonary object. Turns a dict into a newline delimited
    string. Intended use is for loading up sample specifications into the starting buffer of an editor

    :param dict_obj: type dict dictionary to format"""
    res = ''
    for k, v in dict_obj.iteritems():
        res += '{0:<12} {1:>8}\n'.format(k + ':', v)
    return res


lformat = LTemplate().format  # ready to rock formatter object
