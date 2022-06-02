#!/bin/bash 
set -euxo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
vscodesnippetfolder="$HOME/.config/Code/User/"

#Backup former set of snippets from vscode 
cd $vscodesnippetfolder
backupfolder=Backup$(date "+%Y-%m-%d-%H-%m-%S")
mkdir -p $backupfolder
cp *.json ./$backupfolder
zip -r $backupfolder.zip $backupfolder

#Convert all snippets
cd $DIR
./snippetconverter.py -i  $HOME/.local/share/ktexteditor_snippets/data/CMake\ snippets.xml -o $HOME/.config/Code/User/snippets/cmake.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/C\ snippets.xml -o $HOME/.config/Code/User/snippets/c.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/C++\ Textbausteine.xml -o $HOME/.config/Code/User/snippets/cpp.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/Bibtex.xml -o $HOME/.config/Code/User/snippets/bibtex.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/Javascript.xml -o $HOME/.config/Code/User/snippets/javascript.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/LaTeX\ snippets.xml -o $HOME/.config/Code/User/snippets/latex.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/Markdown.xml -o $HOME/.config/Code/User/snippets/markdown.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/Powershell.xml -o $HOME/.config/Code/User/snippets/powershell.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/Makefiles.xml -o $HOME/.config/Code/User/snippets/makefile.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/html.xml -o $HOME/.config/Code/User/snippets/html.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/Windows-batch.xml -o $HOME/.config/Code/User/snippets/bat.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/SQLite.xml -o $HOME/.config/Code/User/snippets/sql.json
./snippetconverter.py -i $HOME/.local/share/ktexteditor_snippets/data/Python\ Textbausteine.xml -o $HOME/.config/Code/User/snippets/python.json


