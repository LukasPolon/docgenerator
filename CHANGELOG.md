<!---
#######################################
## PyDocGenerator application Changelog
##
## Format: markdown (md)
## Latest versions should be placed as first
##
## Notation: 00.01.02
##      - 00: stable released version
##      - 01: new features
##      - 02: bug fixes and small changes 
##
## Updating schema (mandatory):
##      <empty_line>
##      <version> (dd/mm/rrrr)
##      ----------------------
##      * <item>
##      * <item>
##      <empty_line>
##
## Useful tutorial: https://en.support.wordpress.com/markdown-quick-reference/
##
#######################################
-->

00.00.06 (17/10/2018)
---------------------
* Added: create_table method in FormatterMd class
* Added: unit tests for create_table method

00.00.05 (14/10/2018)
---------------------
* Added: FormatterMd class - formatting text to .md format
* Added: unit tests for FormatterMd class
* Added: configuration file for pylint - .pylintrc

00.00.04 (13/10/2018)
---------------------
* Added: shell.py module - function run() for running the application
* Added cli/ package for application commands
* Added: pydocgen command - application main command
* Changed: requirements.txt - pylint and depedences added
* Changed: setup.py new entry point - pdg
* Added: test_shell and test_pydocgen unit tests

00.00.03 (07/10/2018)
---------------------
* Added: .coveragerc file for unittests configuration
* Added: new Python package tests/
* Changed: coverage==5.0a3 added to requirements.txt file

00.00.02 (07/10/2018)
---------------------
* Fix: deleted corrupted lines from Dockerfile

00.00.01 (07/10/2018)
---------------------
* Added: Dockerfile for production
* Added: setup.py script
* Added: CHANGELOG.md file
* Added: requirements.txt file
* Added: get_latest_version function in setup.py script - getting latest version from CHANGELOG.md file
* Added: get_requirements function in setup.py script - getting required Python modules for installation from requirements.txt file
* Added: src/ empty package
* Changed: README.md - added link to the changelog

00.00.00 (06/10/2018)
---------------------
* Created repository and associated files: LICENSE, README.md, .gitignore
