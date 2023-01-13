"""unit tests of snippetconverter_test.py"""
from snippetconverter.snippetconverter import (
    IDE,
    Variable,
    get_variable_lists_from_kate_snippet,
    induce_ide_from_file,
)


def test_get_variable_lists_from_kate_snippet():
    """
    @brief test the get_variable_lists_from_kate_snippet
    """
    content = ["blalba\\%27!@#&^@${foo}):", "${bar}"]
    expected = [
        Variable({"name": "foo", "original_text": "${foo}"}),
        Variable({"name": "bar", "original_text": "${bar}"}),
    ]
    assert expected == get_variable_lists_from_kate_snippet(content)


def test_induce_ide_from_file():
    """
    @brief test the induction of ide from the filename
    """
    # pylint: disable=W1401
    kate_snippet_file_path = (
        "/home/foo/.local/share/ktexteditor_snippets/data/CMake snippets.xml"
    )
    vscode_snippet_file_path = "/home/foo/.config/Code/User/snippets/cmake.json"
    assert IDE.VSCODE == induce_ide_from_file(vscode_snippet_file_path)
    assert IDE.KATE == induce_ide_from_file(kate_snippet_file_path)
