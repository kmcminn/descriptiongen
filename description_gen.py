#!/usr/bin/env python
import argparse
import copy
import os
import subprocess  # noqa
import sys

from lib.colors import red, green, cyan
from lib.rtf import to_rtf
from lib.stdin_util import iter_read_line, read_from_editor
from lib.string_util import (
    lformat,
    repr_dict,
    parse_colon_lines,
    to_lines,
    is_valid_data_for_template
)
from lib import products


def template_product(product_type, templates, stdin=True, rtf=False):
    spec_template = products.specification_templates[product_type]
    if stdin:
        print "{0} a product description. Hit {1} a few times after pasting. Press {2} to continue".format(green('PASTE'), green('ENTER'), green('CTRL+C'))
        result = raw_input("--> Ready to paste the product description? [y/n]: ")
    else:
        result = raw_input("--> Ready to create a product description? [y/n]: ")
    print

    if result.lower() != 'y':
        print 'User cancelled paste. Abort'
        return 1

    if stdin:
        lines = iter_read_line()
    else:
        _buffer = 'Format specifications according to template below, delete all extra text. :wq when done:\n\n'
        _buffer += repr_dict(spec_template)
        editor_buffer = read_from_editor(start_buffer=_buffer)

    lines = editor_buffer.split('\n') if not stdin else lines
    lines = [line.strip() for line in lines if ':' in line]  # only keep lines with a ":" in them
    editor_lines = '\n'.join(copy.deepcopy(lines))

    data = parse_colon_lines(lines)  # parse the lines and reduce into a dictionary
    print data

    i = 1
    numbers = str(i) + ', '
    lformats = {}
    for template in templates:
        _is_valid, _missing_key = is_valid_data_for_template(template, data)
        if not _is_valid:
            print 'Inputted product description is missing key {0}'.format(red(_missing_key))
            print 'Aborting'
            return 1

        lformats[i] = lformat(template, **data)

        print '---- {0} #{1} ----'.format(cyan('Product Description'), i)
        print lformats[i]
        print
        numbers += str(i) + ', '
        i += 1

    result = raw_input('{0} the {1} product description to use, or {2} to go custom: [0-9/a-z] '.format(cyan('Enter'), green('Number'), green('any letter')))
    if result.isdigit():
        description = lformats[int(result)]
    else:
        _buffer = 'Write a product description, generated ones are below. Delete this text when done. :wq to continue\n\n\n'
        _buffer += '\n\n'.join(["#{0} {1}".format(k, v) for k, v in lformats.iteritems()])
        description_lines = read_from_editor(start_buffer=_buffer)
        description = '\n'.join(to_lines(description_lines))

    final_doc = to_rtf(description, editor_lines) if rtf else description + "\n" + "\n" + editor_lines

    print
    print '------------------ Product Description: {0} -------------------'.format(data['name'])
    print
    print final_doc

    result = raw_input('{0} product description+specs to {1}? [y/n] '.format(cyan('Send'), green('clipboard')))
    if result.lower() == 'y':
        # subprocess.call(['echo', '-e', description + '\n' + editor_lines, '|', 'pbcopy'], shell=True)
        if rtf:
            # -Prefer isn't required passing rtf formatted chars through shells and python barely works
            cmd = "bash -c 'echo \"{0}\"' | pbcopy -Prefer rtf".format(final_doc)
        else:
            cmd = "bash -c 'echo -e \"{0}\"' | pbcopy".format(final_doc)

        os.system(cmd)
        print 'Successfully saved to clipboard'
    return 0


def main():
    ptypes = ' '.join(['"{0}"'.format(x) for x in products.PRODUCT_TYPES])
    parser = argparse.ArgumentParser()
    parser.add_argument('gen', default=None, help='generate product descriptions: {0} and "example"'.format(ptypes))
    parser.add_argument('--editor', default=False, action='store_true', help='create a new product description using editor')
    parser.add_argument('--rtf', default=False, action='store_true', help='product rtf formatted output')
    args = parser.parse_args()

    if args.gen == 'example':
        for product_type in products.PRODUCT_TYPES:
            tmpl = products.templates[product_type].itervalues().next()  # get 1 template

            print '---- Sample {0} Specs & Description ----'.format(green(product_type.capitalize()))
            print products.sample_specifications[product_type]
            data = parse_colon_lines(to_lines(products.sample_specifications[product_type]))  # parse the lines and reduce into a dictionary
            print lformat(tmpl, **data)
            print

        return 0

    if args.gen:
        """fetch the template in products.templates and copy it. print descriptions"""
        templates = copy.deepcopy(products.templates[args.gen])
        return template_product(args.gen, [v for v in templates.itervalues()], stdin=not args.editor, rtf=args.rtf)


if __name__ == '__main__':
    sys.exit(main())
