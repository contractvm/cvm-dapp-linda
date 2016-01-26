# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, ConsensusManager, DappManager

class LindaManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (BlockstoreManager, self).__init__(consensusManager, wallet)


	def rd (self, query):
		return self.consensusManager.jsonConsensusCall ('linda.rd', [query])['result'])

	def in (self, query):
		t = self.rd (query)
		cid = self.produceTransaction ('linkda.out', [query])
		return (t, cid)

	def out (self, tp):
		cid = self.produceTransaction ('linda.set', [tp])
		return cid
