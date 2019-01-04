from enum import Enum
from itertools import count

Languages=Enum("Languages",zip(['ABAP','BAT','BIBTEX','CLOJURE','COFFEESCRIPT','C','CPP','CSHARP','CSS','DIFF','DOCKERFILE','FSHARP','GITCOMMIT','GITREBASE','GO','GROOVY','HANDLEBARS','HTML','INI','JAVA','JAVASCRIPT','JAVASCRIPTREACT','JSON','JSONC','LATEX','LESS','LUA','MAKEFILE','MARKDOWN','OBJECTIVEC','OBJECTIVECPP','PERL','PHP','POWERSHELL','JADE','PYTHON','R','RAZOR','RUBY','RUST','SCSS','SHADERLAB','SHELLSCRIPT','SQL','SWIFT','TYPESCRIPT','TYPESCRIPTREACT','TEX','VB','XML','XSL','YAML'],count()))


def InduceLanguageFromFileName(filename):
	if "C++" in filename or "c++" in filename or "cpp" in filename or "Cpp" in filename:
		return Languages.CPP
	if "Python" in filename or "python" in filename:
		return Languages.PYTHON 
	
	raise Exception("Could not induce language from filename {}".format(filename))

def getLanguageIdentifierforVSCode(Language):
	languageidentifier=dict({"ABAP":"abap", "BAT": "bat", "BIBTEX": "bibtex", 
						  "CLOJURE": "clojure", "COFFEESCRIPT": "coffeescript", "C": "c", "CPP": "cpp", "CSHARP": "csharp", "CSS": "css", 
						  "DIFF": "diff", "DOCKERFILE": "dockerfile",
						  "FSHARP": "fsharp",
						  "GITCOMMIT": "git-commit", "GITREBASE": "git-rebase", "GO":	"go", "GROOVY": "groovy",
						  "HANDLEBARS": "handlebars", "HTML": "html",
						  "INI": "ini",
						  "JAVA": "java", "JAVASCRIPT": "javascript", "JAVASCRIPTREACT": "javascriptreact", "JSON": "json", "JSONC":"jsonc", 
						  "LATEX": "latex", "LESS": "less", "LUA": "lua", 
						  "MAKEFILE": "makefile", "MARKDOWN": "markdown",
						  "OBJECTIVEC": "objective-c", "OBJECTIVECPP": "objective-cpp",
						  "PERL": "perl", "PHP": "php", "POWERSHELL": "powershell", "PYTHON": "python",
						  "JADE": "jade",
						  "R": "r","RAZOR": "razor", "RUBY": "ruby", "RUST": "rust",
						  "SCSS": "scss", "SHADERLAB": "shaderlab", "SHELLSCRIPT": "shellscript", "SQL": "sql", "SWIFT": "swift", 
						  "TYPESCRIPT": "typescript", "TYPESCRIPTREACT": "typescriptreact","TEX": "tex",
						  "VB": "vb",
						  "XML": "xml", "XSL": "xsl",
						  "YAML":"yaml" })
	try:
		return languageidentifier[Language.name]
	except ValueError:
		print("No known VSCode language identifier for language {}".format(Language))
		raise ValueError
		













