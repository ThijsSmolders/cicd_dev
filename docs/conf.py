"""Sphinx configuration."""
project = "Cicd_Dev"
author = "Thijs Smolders"
copyright = "2022, Thijs Smolders"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
