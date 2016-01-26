# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from contractvmd import dapp, config

logger = logging.getLogger(config.APP_NAME)

class LindaCore (dapp.Core):
	def __init__ (self, chain, database):
		super (LindaCore, self).__init__ (chain, database)

	def in (self, key, value):
		if self.database.exists (key):
			return
		else:
			self.database.set (key, value)

	def rd (self, query):
		pass

	def out (self, key):
		if not self.database.exists (key):
			return None
		else:
			return self.database.get (key)
