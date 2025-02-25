# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import datetime
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'sphinx-hoverxref'
year = datetime.datetime.now().year
copyright = f'{year}, Manuel Kaufmann'
author = 'Manuel Kaufmann'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax',
    'sphinx_tabs.tabs',
    'sphinx-prompt',
    'autoapi.extension',
    'hoverxref.extension',
    'versionwarning.extension',
    'notfound.extension',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['refs.bib']

intersphinx_mapping = {
    'readthedocs': ('https://docs.readthedocs.io/en/stable/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'sympy': ('https://docs.sympy.org/latest/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'python': ('https://docs.python.org/3/', None),
}
hoverxref_intersphinx = [
    'readthedocs',
    'sphinx',
    'sympy',
    'numpy',
    'python',
]
hoverxref_intersphinx_types = {
    'readthedocs': 'modal',
    'sphinx': 'tooltip',
}

# Used when building the documentation from the terminal and using a local Read
# the Docs instance as backend
hoverxref_api_host = 'http://localhost:8000'

if os.environ.get('READTHEDOCS') == 'True':
    # Building on Read the Docs
    hoverxref_api_host = 'https://readthedocs.org'

    if os.environ.get('PROXIED_API_ENDPOINT') == 'True':
        # Use the proxied API endpoint
        hoverxref_api_host = '/_'

if os.environ.get('LOCAL_READTHEDOCS') == 'True':
    # Building on a local Read the Docs instance
    hoverxref_api_host = 'http://community.dev.readthedocs.io'

if os.environ.get('NGROK_READTHEDOCS') == 'True':
    # Building on a local Read the Docs instance using NGROK for HTTPS
    hoverxref_api_host = 'https://readthedocs.ngrok.io'

hoverxref_tooltip_maxwidth = 650
hoverxref_auto_ref = True
hoverxref_roles = [
    'confval',
    'term',
]

hoverxref_role_types = {
    'hoverxref': 'tooltip',
    'ref': 'modal',
    'confval': 'tooltip',
    'mod': 'modal',
    'class': 'modal',
    'obj': 'tooltip',
}
hoverxref_domains = [
    'py',
    'cite',
]
hoverxref_sphinxtabs = True
hoverxref_mathjax = True

autosectionlabel_prefix_document = True

autoapi_dirs = ['../hoverxref']
autoapi_add_toctree_entry = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinx-hoverxrefdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'sphinx-hoverxref.tex', 'sphinx-hoverxref Documentation',
     'Manuel Kaufmann', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sphinx-hoverxref', 'sphinx-hoverxref Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'sphinx-hoverxref', 'sphinx-hoverxref Documentation',
     author, 'sphinx-hoverxref', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


def setup(app):
    app.add_object_type(
        'confval',  # directivename
        'confval',  # rolename
        'pair: %s; configuration value',  # indextemplate
    )

    app.add_css_file('css/custom.css')
