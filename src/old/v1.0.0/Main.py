#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2017 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#===================================
# Criado por: Wolfterro
# Versão: 1.0.0 - Python 2.x
# Data: 30/03/2017
#===================================

# Imports gerais
# ==============
from __future__ import print_function
import sys
import hashlib
import argparse

# Imports do programa
# ===================
from CheckMySum import CheckMySum
from GlobalVars import GlobalVars

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Método de entrada do programa
# =============================
def main():
	if ("-v" in sys.argv or "--version" in sys.argv) and len(sys.argv) <= 2:
		print("==========================")
		print("CheckMySum - Version %s" % (GlobalVars.Version))
		print("==========================\n")
		
		print(" *** This program is licensed under the MIT License ***\n")
		
		print("Copyright (c) 2017 Wolfgang Almeida <wolfgang.almeida@yahoo.com>")
		print("GitHub's repository: %s\n" % ("https://github.com/Wolfterro/CheckMySum"))
		sys.exit(0)

	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--algorithm", choices=hashlib.algorithms_guaranteed, help="Defines the hash algorithm to be used", required=True)
	parser.add_argument("-f", "--files", nargs="+", help="Select the files to be checked", required=True)
	parser.add_argument("-v", "--version", action="store_true", help="Show the programs version and exit", required=False)

	args = parser.parse_args()

	HashAlgorithm = args.algorithm.lower()
	for file in args.files:
		MySum = CheckMySum(HashAlgorithm, file)

# Inicializando programa
# ======================
if __name__ == "__main__":
	main()