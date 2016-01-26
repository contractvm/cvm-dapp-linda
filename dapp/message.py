# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from contractvmd.chain import message
from . import proto

class LindaMessage (message.Message):
	def insert (q):
		m = LindaMessage ()
		m.Query = q
		m.DappCode = proto.LindaProto.DAPP_CODE
		m.Method = proto.LindaProto.METHOD_IN
		return m

	def output (t):
		m = LindaMessage ()
		m.Tuple = t
		m.DappCode = proto.LindaProto.DAPP_CODE
		m.Method = proto.LindaProto.METHOD_OUT
		return m

	def toJSON (self):
		data = super (LindaMessage, self).toJSON ()

		if self.Method == proto.LindaProto.METHOD_IN:
			data['query'] = self.Query
		elif self.Method == proto.LindaProto.METHOD_OUT:
			data['tuple'] = self.Tuple
		else:
			return None

		return data
