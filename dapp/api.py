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
			"call": self.method_get,
			"help": {"args": ["key"], "return": {}}
		}

		rpcmethods["out"] = {
			"call": self.method_set,
			"help": {"args": ["key", "value"], "return": {}}
		}

		rpcmethods["rd"] = {
			"call": self.method_set,
			"help": {"args": ["key", "value"], "return": {}}
		}

		errors = { }

		super (LindaAPI, self).__init__(core, dht, rpcmethods, errors)

	def method_rd (self, key):
		pass

	def method_in (self, key):
		v = self.core.get (key)
		if v == None:
			return self.createErrorResponse ('KEY_IS_NOT_SET')
		else:
			return v

	def method_out (self, key, value):
		if self.core.get (key) != None:
			return self.createErrorResponse ('KEY_ALREADY_SET')

		msg = message.LindaMessage.set (key, value)
		return self.createTransactionResponse (msg)
