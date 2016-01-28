# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from ast import literal_eval
from contractvmd import dapp, config

logger = logging.getLogger(config.APP_NAME)

class LindaCore (dapp.Core):
	def __init__ (self, chain, database):
		super (LindaCore, self).__init__ (chain, database)
		database.init ('tuplespace', [])


	# The query system allows these query:
	# (,,)			Match a tuple with 3 elements of any types
	# (,%f,)		Match a tuple with 3 elements where the second element is a float (or %s: string, %d: int)
	# ('ciao',,)	Match a tuple with 3 elements where the first element is the string 'ciao'
	def _match (self, t, q):
		q = q.replace ('(', '').replace (')', '').split (',')
		# Length check
		if len (q) != len (t):
			return False

		i = -1
		for qt in q:
			i += 1

			# Empty string: field existence
			if len (qt) == 0:
				continue

			# Start with %, typematch
			if qt[0] == '%':
				if qt[1] == 'f' and type (t[i]) == float:
					continue
				elif qt[1] == 'd' and type (t[i]) == int:
					continue
				elif qt[1] == 's' and type (t[i]) == str:
					continue
				else:
					return False

			# Value match
			else:
				if type(qt) == type (t[i]) and eval (qt) == t[i]:
					continue
				else:
					return False

		return True


	def _query (self, q):
		l = self.database.get ('tuplespace')
		for t in l:
			try:
				if self._match (literal_eval (t), q):
					return t
			except:
				pass

		return None

	def insert (self, q):
		r = self._query (q)
		self.database.listremove ('tuplespace', r)

	def read (self, q):
		r = self._query (q)
		return r

	def output (self, tp):
		self.database.listappend ('tuplespace', tp)
