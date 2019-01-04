#!/usr/bin/python3
import sys, getopt

class bcolors:
	NC='\033[0m'
	Bold='\033[1m'
	Underlined='\033[4m'
	Blink='\033[5m'
	Inverted='\033[7m'
	Hidden='\033[8m'
	Black='\033[1;30m'
	Red='\033[1;31m'
	Green='\033[1;32m'
	Yellow='\033[1;33m'
	Blue='\033[1;34m'
	Purple='\033[1;35m'
	Cyan='\033[1;36m'
	LightGray='\033[1;37m'
	DarkGray='\033[1;30m'
	LightRed='\033[1;31m'
	LightGreen='\033[1;32m'
	LightYellow='\033[1;93m'
	LightBlue='\033[1;34m'
	LightPurple='\033[35m'
	LightCyan='\033[1;36m'

	White='\033[1;97m'
	BckgrDefault='\033[49m'
	BckgrBlack='\033[40m'
	BckgrRed='\033[41m'
	BckgrGreen='\033[42m'
	BckgrYellow='\033[43m'
	BckgrBlue='\033[44m'
	BckgrPurple='\033[45m'
	BckgrCyan='\033[46m'
	BckgrLightGray='\033[47m'
	BckgrDarkGray='\033[100m'
	BckgrLightRed='\033[101m'
	BckgrLightGreen='\033[102m'
	BckgrLightYellow='\033[103m'
	BckgrLightBlue='\033[104m'
	BckgrLightPurple='\033[105m'
	BckgrLightCyan='\033[106m'
	BckgrWhite='\033[107m'	
	#Typical format
	Achtung=LightRed+Bold+Blink
	Error=LightRed+Bold


def usage():
	print(bcolors.LightRed +sys.argv[0] + bcolors.LightPurple+ '[-h -v --errocode -i --input -o --ouput]' +bcolors.NC)
	print(bcolors.LightGreen +"\tWhere:")
	print(bcolors.LightPurple +"\t-i|--input"+bcolors.LightCyan+"\tinput file")
	print(bcolors.LightPurple +"\t-o|--ouput"+bcolors.LightCyan+"\toutput file")
	print(bcolors.LightGreen +"\n\n\tDescription:")
	print(bcolors.LightCyan +"\tConvert snippets from one IDE to another")	
	print(bcolors.LightGreen +"\n\n\tExample of use:")
	print(bcolors.LightRed +"\t"+sys.argv[0] + bcolors.LightPurple+' --input '+bcolors.LightCyan+"$HOME/.local/share/ktexteditor_snippets/CMake.xml"+ bcolors.LightPurple+' --ouput '+bcolors.LightCyan+"$HOME/.config/Code/User/snippets/cmake.json")       
	print(bcolors.NC)
	
def errorlist():
	print(bcolors.Red+"--------------------------------------------------------")
	print("EXIT CODE       |MEANING")
	print("--------------------------------------------------------")
	print("0               |Success")
	print("1               |Error when parsing argument")
	print("255             |Exit returning information (help, version, list of error codes etc)"+bcolors.NC)

def CheckAndQuitUponFolderMissing(folderlist,errorcode):
	for folder in folderlist:
		if (not os.path.isdir(folder)):
			print(bcolors.LightRed+"Exit error code "+str(errorcode)+": folder "+folder+" does not exist"+bcolors.NC)
			sys.exit(errorcode)


from enum import Enum
class IDE(Enum):
	UNKNOWN= 1
	KATE = 2
	VSCODE = 3
	

def InduceIDEFromFile(filename):
	if "ktexteditor" in filename or "kdevelop" in filename:
		return IDE.KATE 
	if "Code/User" in filename:		#TODO implement some better ways .(document what other IDE have for name, to ensure we won't have double match if using only *.json)
		return IDE.VSCODE 
	return IDE.UNKNOWN
	
	
class Snippet: 
	def __init__(self,name,content):
		self.name=name 
		self.content=content
	

def ConvertKateToVScode(katensippet,vscodesnippet):
	snippets=list()
	import xml.etree.ElementTree as ET
	import json 
	tree = ET.parse(katensippet)
	root = tree.getroot()
	for items in root.findall("item"):
		try: 
			match=items.find("match")
			fillin=items.find("fillin")
			snippets.append(Snippet(match.text,fillin.text))
		except Exception as e:
			print(e)		
			pass
	
	pass

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["errorcode","input=","ouput="])
		
	except getopt.GetoptError:
		usage
		sys.exit(1)
		
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
			
		if opt == '--errorcode' :
			errorlist()
			sys.exit()
			
		elif opt in ("-i", "--input"):
			inputfile = arg
			
		elif opt in ("-o", "--ouput"):
			outputfile = arg
	#Write the code below, bare in minde functions must be forwarde declared

	
	#Quit if inputfile does not exist
	import os.path
	if (not os.path.isfile(inputfile)):
		raise FileNotFoundError(str("File: {} does not exist".format(inputfile)))

	ide_in=InduceIDEFromFile(inputfile)
	ide_out=InduceIDEFromFile(outputfile)
	if ide_in==IDE.UNKNOWN :
		raise Exception(str("Could not find which IDE the file {} comes from.".format(inputfile)))
	if ide_out==IDE.UNKNOWN :
		raise Exception(str("Could not find which IDE the file {} comes from.".format(outputfile)))
	

	if InduceIDEFromFile(inputfile)==IDE.KATE and InduceIDEFromFile(outputfile)==IDE.VSCODE :
		ConvertKateToVScode(inputfile,outputfile)


if __name__ == "__main__":
        main(sys.argv[1:])
