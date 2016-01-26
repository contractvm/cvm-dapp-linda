# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from contractvmd import dapp, config

logger = logging.getLogger(config.APP_NAME)

class LindaCore (dapp.Core):
	def __init__ (self, chain, database):
		super (LindaCore, self).__init__ (chain, database)

	def _query (self, q):
		return None

	def insert (self, q):
		r = self._query (q)
		# delete r
		if self.database.exists (key):
			return
		else:
			self.database.set (key, value)

	def read (self, q):
		r = self._query (q)
		return r

	def output (self, tp):
		if not self.database.exists (key):
			return None
		else:
			return self.database.get (key)
