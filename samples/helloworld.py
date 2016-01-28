#!/usr/bin/python3
# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from linda import LindaManager
import sys

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")

wallet = WalletExplorer.WalletExplorer (wallet_file='test.wallet')
linda = LindaManager.LindaManager (consMan, wallet=wallet)


if __name__ == "__main__":
	if len (sys.argv) == 1:
		print ('usage: helloworld.py publish|read')

	if sys.argv[1] == 'publish':
		linda.output (('hellotupla', 12, 34))
		linda.output (('hellotupla', 12.0, 'hola', 12))

	elif sys.argv[1] == 'read':
		while True:
			print (linda.read ("(%s, %d, %d)"))
			print (linda.read ("('hellotupla', %f, %s, 12)"))
			consMan.waitBlock ()
