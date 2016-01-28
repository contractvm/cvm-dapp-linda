# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging

from contractvmd import dapp, config
from . import api, core, proto, message

logger = logging.getLogger(config.APP_NAME)

class linda (dapp.Dapp):
	def __init__ (self, chain, db, dht, apiMaster):
		self.core = core.LindaCore (chain, db)
		apiprov = api.LindaAPI (self.core, dht, apiMaster)
		super (linda, self).__init__(proto.LindaProto.DAPP_CODE, proto.LindaProto.METHOD_LIST, chain, db, dht, apiprov)

	def handleMessage (self, m):
		if m.Method == proto.LindaProto.METHOD_IN:
			logger.pluginfo ('Found new message %s: IN %s', m.Hash, m.Data['query'])
			self.core.insert (m.Data['query'])

		elif m.Method == proto.LindaProto.METHOD_OUT:
			logger.pluginfo ('Found new message %s: OUT %s', m.Hash, m.Data['tuple'])
			self.core.output (m.Data['tuple'])
