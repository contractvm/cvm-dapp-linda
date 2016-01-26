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
lindaman = LindaManager.LindaManager (consMan, wallet=wallet)

if __name__ == "__main__":
	print ('usage:', sys.argv[0], 'in|out|rd')
