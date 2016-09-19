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

from vts.runners.host import const
from vts.runners.host import asserts
from vts.runners.host import base_test_with_webdb
from vts.runners.host import test_runner
from vts.utils.python.controllers import android_device


class SyscallExistenceTest(base_test_with_webdb.BaseTestWithWebDbClass):
    """Tests to verify kernel syscall interface."""
    TEST_SHELL_NAME = "my_shell1"
    AARCH64__NR_name_to_handle_at = 264
    AARCH64__NR_open_by_handle_at = 265
    AARCH64__NR_uselib = 1077

    def setUpClass(self):
        self.dut = self.registerController(android_device)[0]
        self.dut.shell.InvokeTerminal(self.TEST_SHELL_NAME)

    def tearDownTest(self):
        self.dut.shell.InvokeTerminal(self.TEST_SHELL_NAME)
        results = getattr(self.dut.shell, self.TEST_SHELL_NAME).Execute("which ls")
        logging.info(str(results[const.STDOUT]))
        asserts.assertEqual(len(results[const.STDOUT]), 1)
        asserts.assertEqual(results[const.STDOUT][0].strip(), "/system/bin/ls")
        asserts.assertEqual(results[const.EXIT_CODE][0], 0)

    def testSyscall_name_to_handle_at(self):
        """Testcase to verify syscall [name_to_handle_at] is disabled."""
        logging.info("testing syscall: name_to_handle_at [%d]",
                     self.AARCH64__NR_name_to_handle_at)
        asserts.assertTrue(self.SyscallDisabled(self.AARCH64__NR_name_to_handle_at),
                           "syscall [name_to_handle_at] should be disabled")

    def testSyscall_open_by_handle_at(self):
        """Testcase to verify syscall [open_by_handle_at] is disabled."""
        logging.info("testing syscall: open_by_handle_at [%d]",
                     self.AARCH64__NR_open_by_handle_at)
        asserts.assertTrue(self.SyscallDisabled(self.AARCH64__NR_open_by_handle_at),
                           "syscall [open_by_handle_at] should be disabled")

    def testSyscall_uselib(self):
        """Testcase to verify syscall [uselib] is disabled."""
        logging.info("testing syscall: uselib [%d]",
                     self.AARCH64__NR_uselib)
        asserts.assertTrue(self.SyscallDisabled(self.AARCH64__NR_uselib),
                           "syscall [uselib] should be disabled")

    def SyscallDisabled(self, syscallid):
        """Helper function to check if a syscall is disabled."""
        target = "/data/local/tmp/64/vts_test_binary_syscall_exists"
        results = getattr(self.dut.shell, self.TEST_SHELL_NAME).Execute([
            "chmod 755 %s" % target,
            "%s %d" % (target, syscallid)
        ])
        return len(results[const.STDOUT]) == 2 and results[const.STDOUT][1].strip() == "n"


if __name__ == "__main__":
    test_runner.main()