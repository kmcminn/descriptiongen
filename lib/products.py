from __future__ import absolute_import

from collections import OrderedDict
"""
Product Data entry is the process of a human manually examining a product that is to go into a store
and concisely enumerating the details or specifications of that product. Products have a specifications template which
must be filled out correctly and consistently in order to use them in a template.

These specification templates are used by the description generator to ease the use of writing the
longform product copy. Every product has to have its specifications at a bare minimum. For
others it is best to have a long-hand description in addition to the specifications. That is what
this file is about.

The templates below use the product specifications as inputs. The specifications are parsed in another
tool to extract the fields. The names of the fields are 1:1 and in the template they are lower-cased.

"""
templates = {}
templates['animal'] = {}  # description templates for stuffed animals
templates['puzzle'] = {}  # description templates for puzzles

sample_specifications = {}  # sample [finished] data entry of specifications like what you'd see on live product page

specification_templates = {}  # the required specification structure for any given product type

PRODUCT_TYPES = ['animal', 'puzzle']  # these must stay consistent between samples, spec templates and description templates


# ############## ANIMAL DESCRIPTION TEMPLATES #########################
templates['animal']['aa'] = """The {name} is available in {color:l} and comes with {accessories:l}). This {type:l} features a {style:l} style."""
templates['animal']['bb'] = """This {type:l} is very cute! It would look great on any bed or next to a window with its {accessories:l}. """

# ############# PUZZLE DESCIPTION TEMPLATES ###################
templates['puzzle']['aa'] = """The {name} is a adorable {pieces} {type:l} great for the whole family."""
templates['puzzle']['bb'] = """This {size} {type:l} is the perfect addition to anybody that loves having a beautiful finished {pieces} piece puzzle! """

# ############## SAMPLES #####################
sample_specifications['animal'] = """
Name: Stuffed Valentines Bear
Type: Stuffed Animal
Size: 7.5 x 4 x 3/4 inches
Accessories: Red Ribbons and Boots
Style: Valentines
Color: White
"""

sample_specifications['puzzle'] = """
Name: Italy Romantic Puzzle
Style: Landscape
Type: Cardboard Puzzle
Thickness: 2mm
Pieces: 1000
Size: 24 x 48 inches
"""

# ############ SPECIFICATION SCHEMA TEMPLATE ######################
animal_spec = OrderedDict()
animal_spec['Name'] = "the name of the item, as it will be entered in the store"
animal_spec['Type'] = "the proper description for the item, usually \"Stuffed Animal\""
animal_spec['Size'] = "the size for this item in inches"
animal_spec['Accessories'] = "accessories that come with it"
animal_spec['Style'] = "the singular style we invent as a way to describe the item, i.e. Valentine or Cute: adjective"
animal_spec['Color'] = "the major colors of this item"
specification_templates['animal'] = animal_spec

puzzle_spec = OrderedDict()
puzzle_spec['Name'] = 'the name of this item'
puzzle_spec['Style'] = 'a 1-3 word singular to describe its style: flower, porcelain: adjective'
puzzle_spec['Type'] = 'the type, typically cardboard puzzle or wood puzzle'
puzzle_spec['Thickness'] = 'how thick the puzzle is in mm or inches'
puzzle_spec['Pieces'] = 'how many pieces the puzzle is'
puzzle_spec['Size'] = 'dimensions of the puzzle in inches'
specification_templates['puzzle'] = puzzle_spec
