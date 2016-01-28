# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from . import message
from contractvmd import dapp, config, proto

logger = logging.getLogger(config.APP_NAME)

class LindaAPI (dapp.API):
	def __init__ (self, core, dht, api):
		self.api = api
		rpcmethods = {}

		rpcmethods["in"] = {
			"call": self.method_in,
			"help": {"args": ["query"], "return": {}}
		}

		rpcmethods["out"] = {
			"call": self.method_out,
			"help": {"args": ["tuple"], "return": {}}
		}

		rpcmethods["rd"] = {
			"call": self.method_rd,
			"help": {"args": ["query"], "return": {}}
		}

		errors = { }

		super (LindaAPI, self).__init__(core, dht, rpcmethods, errors)

	def method_rd (self, q):
		t = self.core.read (q)
		if t == None:
			return ''
		return t

	def method_in (self, q):
		msg = message.LindaMessage.insert (q)
		return self.createTransactionResponse (msg)

	def method_out (self, t):
		msg = message.LindaMessage.output (t)
		return self.createTransactionResponse (msg)
