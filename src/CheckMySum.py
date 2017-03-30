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

import os
import sys
import hashlib

# Imports do programa
# ===================
from GlobalVars import GlobalVars

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Classe Principal do programa
# ============================
class CheckMySum(object):
	# Inicializando a classe com o tipo de algoritmo e nome do arquivo
	# ================================================================
	def __init__(self, Algorithm, Filename):
		self.Algorithm = Algorithm
		self.Filename = Filename
		self.Hash = ""
		self.ProcessFile()

	# Iniciando processo de checksum do arquivo selecionado
	# =====================================================
	def ProcessFile(self):
		if self.CheckFileAvailability(self.Filename):
			self.GetCheckSum()
			self.PrintCheckSum()

	# Verificando a existência do arquivo selecionado
	# ===============================================
	def CheckFileAvailability(self, Filename):
		if not os.path.isfile(os.path.abspath(self.Filename)):
			print("Error! File '%s' not available! Skipping..." % (self.Filename))
			return False

		return True

	# Resgatando o checksum do arquivo selecionado
	# ============================================
	def GetCheckSum(self):
		if self.Algorithm == "md5":
			Algo = hashlib.md5()
		elif self.Algorithm == "sha1":
			Algo = hashlib.sha1()
		elif self.Algorithm == "sha224":
			Algo = hashlib.sha224()
		elif self.Algorithm == "sha256":
			Algo = hashlib.sha256()
		elif self.Algorithm == "sha384":
			Algo = hashlib.sha384()
		elif self.Algorithm == "sha512":
			Algo = hashlib.sha512()
		else:
			Algo = hashlib.md5()

		print("Checking...", end="")
		try:
			with open(os.path.abspath(self.Filename), "rb") as file:
				for f in file:
					Algo.update(f)
		
			self.Hash = Algo.hexdigest()
		except Exception as e:
			self.Hash = "N/A - %s" % (e)

	# Imprimindo o checksum do arquivo escolhido
	# ==========================================
	def PrintCheckSum(self):
		print("\r%s - %s" % (self.Filename, self.Hash))