#
# Copyright 2017 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#

from __future__ import absolute_import

import pytest

from . import netfunctestlib as nftestlib
from network.nettestlib import dummy_device


NETWORK_NAME = 'test-network'


@nftestlib.parametrize_switch
class TestBridge(nftestlib.NetFuncTestCase):

    def test_add_bridge_with_stp(self, switch):
        if switch == 'ovs':
            pytest.xfail('stp is currently not implemented for ovs')

        with dummy_device() as nic:
            NETCREATE = {NETWORK_NAME: {'nic': nic,
                                        'switch': switch,
                                        'stp': True}}
            with self.setupNetworks(NETCREATE, {}, nftestlib.NOCHK):
                self.assertNetworkExists(NETWORK_NAME)
                self.assertNetworkBridged(NETWORK_NAME)
                self.assertBridgeOpts(NETWORK_NAME, NETCREATE[NETWORK_NAME])
