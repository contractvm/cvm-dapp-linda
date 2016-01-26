# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from contractvmd.chain import message
from . import proto

class LindaMessage (message.Message):
	def set (key, value):
		m = LindaMessage ()
		m.Key = key
		m.Value = value
		m.DappCode = proto.LindaProto.DAPP_CODE
		m.Method = proto.LindaProto.METHOD_SET
		return m

	def toJSON (self):
		data = super (LindaMessage, self).toJSON ()

		if self.Method == proto.LindaProto.METHOD_IN:
			#data['key'] = self.Key
			#data['value'] = self.Value
			pass
		elif self.Method == proto.LindaProto.METHOD_OUT:
			pass
		else:
			return None

		return data
