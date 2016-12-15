#!/usr/bin/env python3.4
#
# Copyright (C) 2016 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

from vts.runners.host import base_test_with_webdb
from vts.runners.host import test_runner
from vts.utils.python.controllers import android_device


class NfcHidlBasicTest(base_test_with_webdb.BaseTestWithWebDbClass):
    """A simple testcase for the NFC HIDL HAL."""

    def setUpClass(self):
        self.dut = self.registerController(android_device)[0]
        self.dut.hal.InitHidlHal(target_type="nfc",
                                 target_basepaths=["/system/lib64"],
                                 target_version=1.0,
                                 bits=64)

    def testBase(self):
        """A simple testcase which just calls a function."""
        # TODO: extend to make realistic testcases
        result = self.dut.hal.nfc.open()
        logging.info("result: %s", result.return_type.string_value.message)

    def TestNormla(self):
        """A simple testcase which just calls functions."""
        result = self.dut.hal.nfc.open()
        logging.info("result: %s", result.return_type.string_value.message)
        result = self.dut.hal.nfc.core_initialized(0)
        logging.info("result: %s", result.return_type.string_value.message)
        result = self.dut.hal.nfc.close()
        logging.info("result: %s", result.return_type.string_value.message)


if __name__ == "__main__":
    test_runner.main()
