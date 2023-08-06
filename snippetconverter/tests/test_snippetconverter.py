"""unit tests of snippetconverter_test.py"""
import pytest
import pathlib
from unittest.mock import patch
from unittest.mock import MagicMock
from pathlib import Path
from snippetconverter.snippetconverter import (
    IDE,
    Variable,
    get_variable_lists_from_kate_snippet,
    induce_ide_from_file,
    usage,
    convert_from_kate_to_vscode,
    convert_vscode_to_kate,
    main
)


def test_get_variable_lists_from_kate_snippet():
    """
    @brief test the get_variable_lists_from_kate_sn
    ippet
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
    unknown_snippet_file_path = "/home/foo/.config/Whatever/snippets/cmake.whatever"
    assert IDE.VSCODE == induce_ide_from_file(vscode_snippet_file_path)
    assert IDE.KATE == induce_ide_from_file(kate_snippet_file_path)
    assert IDE.UNKNOWN == induce_ide_from_file(unknown_snippet_file_path)

def test_usage_does_no_throw():
    """
    @brief test that usage does not throw"""
    usage()





DUMMY_XML_CONTENT="""<snippets authors=\"max\" license=\"BSD\" name=\"C snippets\" filetypes=\".c\" namespace=\"\">
<script>function fooFunc() { return document.fileName(); }
</script>
<item>
<match>dolphin_service_menu</match>
<fillin>int ${a};
</fillin>
</item>
</snippets>
"""

EXPECT_C_JSON_CONTENT="""{
    "dolphin_service_menu": {
        "body": [
            "int ${a};",
            ""
        ],
        "description": "",
        "prefix": "dolphin_service_menu",
        "scope": "c"
    }
}"""

def create_temporary_c_snippet_for_kate_and_vscode(tmp_path):
    kate_snippet_folder=tmp_path/ "kdevelop" / "data"
    kate_snippet_folder.mkdir( parents=True)
    kate_snippet_c = kate_snippet_folder / "C snippets.xml"
    kate_snippet_c.write_text(DUMMY_XML_CONTENT)

    code_snippet_folder=tmp_path/ "Code" / "User"/"snippets"
    code_snippet_folder.mkdir( parents=True)
    code_snippet_c = code_snippet_folder / "c.json"

    return [kate_snippet_c,code_snippet_c]

def test_convert_from_kate_to_vscode(tmp_path):
    [kate_snippet_c,code_snippet_c]=create_temporary_c_snippet_for_kate_and_vscode(tmp_path)

    convert_from_kate_to_vscode(kate_snippet_c,code_snippet_c)
    assert code_snippet_c.read_text() == EXPECT_C_JSON_CONTENT


def test_convert_vscode_to_kate(tmp_path):
    [kate_snippet_c,code_snippet_c]=create_temporary_c_snippet_for_kate_and_vscode(tmp_path)
    with pytest.raises(NotImplementedError):
        convert_vscode_to_kate(code_snippet_c,kate_snippet_c)

    

def test_main_throws_if_input_file_does_not_exit():
    argv=['./__main__.py', '-i', 'inexistant_file.xml', '-o', '/home/foo/.config/Code/User/snippets/cmake.json']
    with pytest.raises(FileNotFoundError):
        main(argv)


convert_from_kate_to_vscode_mock=MagicMock()
@patch('snippetconverter.snippetconverter.convert_from_kate_to_vscode')
def test_main_convert_correctly_when_input_is_kate_snippet(convert_from_kate_to_vscode_mock,tmp_path):
    [kate_snippet_c,code_snippet_c]=create_temporary_c_snippet_for_kate_and_vscode(tmp_path)
    argv=['./__main__.py', '-i', str(kate_snippet_c.absolute()), '-o', str(code_snippet_c.absolute())]
    main(argv)
    assert convert_from_kate_to_vscode_mock.called

convert_vscode_to_kate_mock=MagicMock()
@patch('snippetconverter.snippetconverter.convert_vscode_to_kate')
def test_main_convert_correctly_when_input_is_code_snippet(convert_vscode_to_kate_mock,tmp_path):
    [kate_snippet_c,code_snippet_c]=create_temporary_c_snippet_for_kate_and_vscode(tmp_path)
    code_snippet_c.write_text(EXPECT_C_JSON_CONTENT)
    argv=['./__main__.py', '-i', str(code_snippet_c.absolute()), '-o', str(kate_snippet_c.absolute())]
    main(argv)
    assert convert_vscode_to_kate_mock.called
    
def test_main_input_IDE_unknown(tmp_path):
    [kate_snippet_c,code_snippet_c]=create_temporary_c_snippet_for_kate_and_vscode(tmp_path)
    some_file=tmp_path / "foobar.yaml"
    some_file.write_text(DUMMY_XML_CONTENT)
    argv=['./__main__.py', '-i', str(some_file.absolute()), '-o', str(kate_snippet_c.absolute())]
    with pytest.raises(RuntimeError):
        main(argv)
    
def test_main_output_IDE_unknown(tmp_path):
    [kate_snippet_c,code_snippet_c]=create_temporary_c_snippet_for_kate_and_vscode(tmp_path)
    code_snippet_c.write_text(EXPECT_C_JSON_CONTENT)
    argv=['./__main__.py', '-i', str(code_snippet_c.absolute()), '-o', "/home/foo"]
    with pytest.raises(RuntimeError):
        main(argv)
