# HACK Assembly Language Syntax Verifier in Python
 
This program verifies whether or not a given file is valid Hack Assembly Code (as specified by [Nand2Tetris](https://www.nand2tetris.org/project06)). This code was written as second part of the Introduction to Computer Final Project (the first part being the implementation of Chapter 6's homework itself).

Since HACK Assembly itself is a regular language, a program utilizing regex is sufficient in determining its regularity. Proof that HACK Assembly itself is regular can be found [here](https://hackmd.io/gAKe5ocSR2SyUg8Yen3HoA?view#Discoveries-the-Regularity-of-Hack).

Usage: `python regular.py <filename.asm>`.
* If `<filename.asm>` is valid Hack Assembly code, the program prints `<filename.asm> is a valid HACK Assembly file`.
* Otherwise, the program prints `<filename.asm> is not a valid HACK Assembly file`.
