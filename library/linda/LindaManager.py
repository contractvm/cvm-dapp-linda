# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from ast import literal_eval
from libcontractvm import Wallet, ConsensusManager, DappManager

class LindaManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (LindaManager, self).__init__(consensusManager, wallet)

	def read (self, query):
		t = self.consensusManager.jsonConsensusCall ('linda.rd', [str (query)])['result']
		if t == '':
			return None

		return literal_eval (t)

	def input (self, query):
		t = self.rd (query)

		if t == '':
			return None
			
		cid = self.produceTransaction ('linda.in', [str (query)])
		return (literal_eval (t), cid)

	def output (self, tp):
		cid = self.produceTransaction ('linda.out', [str (tp)])
		return cid
