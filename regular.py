import re
from sys import argv

if len(argv) != 2 or not re.match(r".*\.asm", argv[1]):
	print("Usage: python regular.py <filename.asm>")
	exit(0)

COMMENTS = r"//.*" 
DECIMAL = r"\d+"
SYMBOL = r"[a-zA-Z_.$][\w.$]*"
## A instructions
AINSTR = r"@({}|{})".format(DECIMAL, SYMBOL)
## (SYMBOL) instructions
LABEL = r"\({}\)".format(SYMBOL)
## C instructions
DEST = r"null|A?M?D|A?M|A"
UNARY = r"[!-]?[01AMD]"
BINARY = r"[AMD][&|+-][01AMD]"
JUMP = r"null|JGT|JEQ|JGE|JLT|JNE|JLE|JMP"
COMPUTATION = r"{}|{}".format(BINARY, UNARY) # apparently you can't put unary first, oops
CINSTR = r"(?:{}=)?(?:{});(?:{})|(?:{})=(?:{})".format(DEST, COMPUTATION, JUMP, DEST, COMPUTATION)

## Hack is regular with the following regex:
reg = r"(\s*(?:{}|{}|{})?\s*(?:{})?\s*(?:\n|$))*".format(AINSTR, CINSTR, LABEL, COMMENTS)
# print("HACK: {}".format(reg))

with open(argv[1], "r") as f:
	file = f.read()
	match = re.fullmatch(reg, file) # this is where the matching actually happens
	if match:
		print("{} is a valid HACK Assembly file".format(argv[1]))
	else:
		print("{} is not a valid HACK Assembly file".format(argv[1]))
