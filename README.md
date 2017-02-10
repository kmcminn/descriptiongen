## Description Gen

## About
description_gen.py is a simple tool for writers to write product descriptions.

When I was first getting started writing product descriptions I realized that each product
needed its own custom description as well as a good set of specifications in order to be well represented in a store.
It is time intensive producing accurate valid specifications and copy. This tool doesn't make it faster really but
it does allow you to reuse your product copy with templates which eases the burden considerably.

## Setup
- make sure you have python 2.* (this is only tested on python 2.7)
- clone into this repository
- cd into this directory
    - requires python 2.7, just stdlib


# Workflows

### Setting up your products

Before you can start generating product copy and specifications you'll need to build a format for
your specifications, write some description templates and then assign them to product types:

1. edit products.py
2. Setup your sample specifications
3. Setup your specification templates
3. Write product description templates
4. tie them to your product types

You can copy the samples {animal, puzzle} in products.py for reference.

### Generating specs and copy

1) observe and analyze a product you with to generate for
2) generate specifications in the correct format
3) upload specifications to description_gen.py (copy paste or use the editor, whichever you prefer)
4) pick your favorite copy
5) paste the result into your products description in your catalog

#### description_gen.py
Use this script to do two things

1. print the sample descriptions so I can copy them and edit them for a new product
2. generate descriptions

#### sample workflow with --editor
export EDITOR=<your favorite editor>  # if you don't know what your favorite editor is, use nano or pico
1. `python specifications_gen.py animal`
2. "y" to begin editing
3. edit the specifications as per the template
4. save and exit the editor
5. select the description from the list of generated descriptions
6. say "yes" to send it to the clipboard
7. paste it into your catalog

### sample workflow without --editor
1. `python description_gen.py example`
2. copy a sample specifications
3. edit the sample specifications in an editor, textedit, notepad, etc
4. `python description_gen.py animal`
5. say "y" to begin
6. paste the specifications into the script
7. hit enter a few times
8. hit CTRL+C to continue
9. select the description from the list of generated descriptions
10. say "yes" to send it to the clipboard
11. paste it into your catalog
