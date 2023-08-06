import pytest
from snippetconverter.languages import LANGUAGES,induce_language_from_file_name , get_language_identifier_for_vscode

def test_induce_language_from_file_name():
    filename="cpp.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.CPP

    filename="Python.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.PYTHON

    filename="Bibtex.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.BIBTEX

    filename="CMake.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.CMAKE

    filename="Makefile.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.MAKEFILE

    filename="Markdown.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.MARKDOWN

    filename="Latex.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.TEX

    filename="Javascript.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.JAVASCRIPT

    filename="JSON.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.JSON

    filename="html.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.HTML

    filename="Powershell.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.POWERSHELL

    filename="Windows-batch.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.BAT

    filename="C snippets.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.C

    filename="Bash.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.SHELLSCRIPT

    filename="SQL.xml"
    assert induce_language_from_file_name(filename) == LANGUAGES.SQL

    filename="foo.bar"
    with pytest.raises(Exception):
        induce_language_from_file_name(filename)