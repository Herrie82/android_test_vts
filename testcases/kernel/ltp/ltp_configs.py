#!/usr/bin/env python3.4
#
# Copyright (C) 2016 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

from vts.testcases.kernel.ltp import ltp_enums

# Environment paths for ltp test cases
# string, ltp build root directory on target
LTPDIR = '/data/local/tmp/ltp'
# Directory for environment variable 'TMP' needed by some test cases
TMP = os.path.join(LTPDIR, 'tmp')
# Directory for environment variable 'TMPBASE' needed by some test cases
TMPBASE = os.path.join(TMP, 'tmpbase')
# Directory for environment variable 'LTPTMP' needed by some test cases
LTPTMP = os.path.join(TMP, 'ltptemp')
# Directory for environment variable 'TMPDIR' needed by some test cases
TMPDIR = os.path.join(TMP, 'tmpdir')
# Path where ltp test binary exists
LTPBINPATH = os.path.join(LTPDIR, 'testcases/bin')
# Add LTP's binary path to PATH
PATH = '/system/bin:%s' % LTPBINPATH

# File system type for loop device
LTP_DEV_FS_TYPE = 'ext4'

# Binaries required by LTP test cases that should exist in PATH
EXTERNAL_BINS = [
    'export',
    'cd',
    'mktemp',
    'cp',
    'chmod',
    'chown',
    'ls',
    'mkfifo',
]

# Requirement to testcase dictionary.
REQUIREMENTS_TO_TESTCASE = {
    ltp_enums.Requirements.LOOP_DEVICE_SUPPORT: [
        'syscalls-mount01',
        'syscalls-fchmod06',
        'syscalls-ftruncate04',
        'syscalls-ftruncate04_64',
        'syscalls-inotify03',
        'syscalls-link08',
        'syscalls-linkat02',
        'syscalls-mkdir03',
        'syscalls-mkdirat02',
        'syscalls-mknod07',
        'syscalls-mknodat02',
        'syscalls-mmap16',
        'syscalls-mount01',
        'syscalls-mount02',
        'syscalls-mount03',
        'syscalls-mount04',
        'syscalls-mount06',
        'syscalls-rename11',
        'syscalls-renameat01',
        'syscalls-rmdir02',
        'syscalls-umount01',
        'syscalls-umount02',
        'syscalls-umount03',
        'syscalls-umount2_01',
        'syscalls-umount2_02',
        'syscalls-umount2_03',
        'syscalls-utime06',
        'syscalls-utimes01',
        'syscalls-mkfs01',
    ],
}

# Requirement for all test cases
REQUIREMENT_FOR_ALL = [ltp_enums.Requirements.LTP_TMP_DIR]

# Requirement to test suite dictionary
REQUIREMENT_TO_TESTSUITE = {}

# Staging tests are for debugging and verifying fixed tests
# Test specified here can be in format: testsuite-testname,
# or testsuite-testname_**bit, or just testname. Using just testname
# is not recommended
STAGING_TESTS = [
    # Bug#30675453
    'syscalls-perf_event_open02',
    # Bug#30688551
    'syscalls-lstat03_64',
    'syscalls-lstat03',
    # Bug#30688061
    'input-input03',
    # Bug#30688056
    'cpuhotplug-cpuhotplug04',
    # Bug#30699880
    'mm-mtest01w',
    'mm-mtest01',
    # Bug#30688574
    'syscalls-accept4_01',
    # Bug#30689411
    'mm-mmapstress03',
    # Tests currently only failing on sailfish and marlin,
    # these will be inspected soon
    'syscalls-fcntl34',
    'syscalls-fcntl34_64',
    'syscalls-open14',
    'syscalls-openat03',
    # Recently fixed
    'connectors-Connectors',
    'cpuhotplug-cpuhotplug02',
    'kernel_misc-kmsg01',
    'syscalls-access01',
    'syscalls-add_key01',
    'syscalls-add_key02',
    'syscalls-chdir03',
    'syscalls-chroot01',
    'syscalls-creat01',
    'syscalls-creat01',
    'syscalls-creat03',
    'syscalls-creat04',
    'syscalls-creat05',
    'syscalls-creat07',
    'syscalls-creat08',
    'epoll_create1_01',
    'epoll_ctl01',
    'epoll_ctl02',
    'fcntl07',
    'fcntl07_64',
    'syscalls-getrusage03',
    'syscalls-getrusage04',
    'madvise05',
    'mkdir02',
    'mkdir04',
    'pause01',
    'pipe01',
    'pipe02',
    'pipe03',
    'posix_fadvise01',
    'posix_fadvise01_64',
    'posix_fadvise03',
    'posix_fadvise03_64',
    'ppoll01',
    'preadv01',
    'preadv01_64',
    'preadv02_64',
    'pwritev01',
    'pwritev02_64',
    'recvmsg02',
    'rename09',
    'syscall01',
    'utime03',
    # Fail on lab device but pass on local device
    'syscalls-execl01',
    'syscalls-execle01',
    'syscalls-execlp01',
    'syscalls-execv01',
    'syscalls-execve01',
    'syscalls-execve04',
    'syscalls-execvp01',
    'syscalls-ioctl01_02',
    'syscalls-move_pages01',
    'syscalls-move_pages02',
    'syscalls-move_pages04',
    'syscalls-move_pages05',
    'syscalls-move_pages06',
    'syscalls-move_pages07',
    'syscalls-move_pages08',
    'syscalls-move_pages09',
    'syscalls-move_pages10',
    'syscalls-setpgid03',
    'mm-mtest05',
    'sched-sched_cli_serv',
    'admin_tools-at_deny01',
    'admin_tools-at_allow01',
    'numa-move_pages01',
    'numa-move_pages02',
    'numa-move_pages04',
    'numa-move_pages05',
    'numa-move_pages06',
    'numa-move_pages07',
    'numa-move_pages08',
    'numa-move_pages09',
    'numa-move_pages10',
    # The following tests are failing on 64bit version
    'mm-overcommit_memory01_64bit',
    'mm-overcommit_memory02_64bit',
    'mm-overcommit_memory03_64bit',
    'mm-overcommit_memory04_64bit',
    'mm-overcommit_memory05_64bit',
    'mm-overcommit_memory06_64bit',
]

# Tests disabled
# Based on external/ltp commit 5f01077afe994f4107b147222f3956716d4a8fde
DISABLED_TESTS = [
    # The following test case is designed only for i386
    'f00f',
    # The following test cases are uncategorized
    'inotify06',
    'abort01',
    'chmod05',
    'chmod07',
    'chown01_16',
    'chown02_16',
    'chown03_16',
    'chown05_16',
    'fchmod01',
    'fchmod02',
    'fchmod05',
    'fchmod06',
    'fchown01_16',
    'fchown02_16',
    'fchown03_16',
    'fchown04_16',
    'fchown05_16',
    'fsync01',
    'ftruncate04',
    'ftruncate04_64',
    'getcwd02',
    'getcwd03',
    'getegid01_16',
    'getegid02_16',
    'geteuid01_16',
    'geteuid02_16',
    'getgid01_16',
    'getgid03_16',
    'getgroups01_16',
    'gethostbyname_r01',
    'getuid01_16',
    'getuid03_16',
    'ioctl03',
    'inotify03',
    'kill11',
    'lchown01_16',
    'lchown02_16',
    'lchown03_16',
    'link08',
    'linkat02',
    'mkdir03',
    'rmdir02',
    'mkdirat02',
    'mknod07',
    'mknodat02',
    'mmap16',
    'mount01',
    'mount02',
    'mount03',
    'mount04',
    'mount06',
    'move_pages03',
    'move_pages11',
    'mprotect01',
    'nftw01',
    'nftw6401',
    'nice04',
    'open01',
    'open08',
    'open10',
    'open11',
    'madvise01',
    'madvise02',
    'madvise06',
    'pathconf01',
    'preadv02',
    'process_vm_readv01',
    'process_vm_writev01',
    'pwritev01_64',
    'pwritev02',
    'quotactl01',
    'readlink04',
    'rename11',
    'renameat01',
    'request_key01',
    'request_key02',
    'rt_sigprocmask01',
    'sbrk03',
    'setfsgid01_16',
    'setfsgid02_16',
    'setfsgid03_16',
    'setfsuid01_16',
    'setfsuid02_16',
    'setfsuid03_16',
    'setfsuid04_16',
    'setgid01_16',
    'setgid02_16',
    'setgid03_16',
    'setgroups01_16',
    'setgroups02_16',
    'setgroups03_16',
    'setgroups04_16',
    'setregid01_16',
    'setregid02_16',
    'setregid03_16',
    'setregid04_16',
    'setresgid01_16',
    'setresgid02_16',
    'setresgid03_16',
    'setresgid04_16',
    'setresuid01_16',
    'setresuid02_16',
    'setresuid03_16',
    'setresuid04_16',
    'setresuid05_16',
    'setreuid01_16',
    'setreuid02_16',
    'setreuid03_16',
    'setreuid04_16',
    'setreuid05_16',
    'setreuid06_16',
    'setreuid07_16',
    'setuid01_16',
    'setuid02_16',
    'setuid03_16',
    'setuid04_16',
    'splice02',
    'sysconf01',
    'syslog01',
    'syslog02',
    'syslog03',
    'syslog04',
    'syslog05',
    'syslog06',
    'syslog07',
    'syslog08',
    'syslog09',
    'syslog10',
    'umask02',
    'umask03',
    'umount01',
    'umount02',
    'umount03',
    'umount2_01',
    'umount2_02',
    'umount2_03',
    'utime06',
    'utimes01',
    'utimensat01',
    'waitpid05',
    'gf01',
    'gf02',
    'gf03',
    'gf04',
    'gf05',
    'gf06',
    'gf07',
    'gf08',
    'gf09',
    'gf10',
    'gf11',
    'gf14',
    'gf15',
    'gf16',
    'gf17',
    'gf18',
    'gf19',
    'gf20',
    'gf21',
    'gf22',
    'gf23',
    'gf24',
    'gf25',
    'gf26',
    'gf27',
    'gf28',
    'gf29',
    'gf30',
    'rwtest01',
    'rwtest02',
    'rwtest03',
    'rwtest04',
    'rwtest05',
    'iogen01',
    'fs_inod01',
    'ftest06',
    'isofs',
    'fsx_linux',
    'ddio04',
    'ddio10',
    'aio01',
    'aio02',
    'mtest06',
    'shm_test01',
    'mallocstress01',
    'mmapstress04',
    'mmapstress07',
    'vma03',
    'min_free_kbytes',
    'pipeio_1',
    'pipeio_3',
    'pipeio_4',
    'pipeio_5',
    'pipeio_6',
    'pipeio_8',
    'trace_sched01',
    'float_bessel',
    'float_exp_log',
    'float_iperb',
    'float_power',
    'float_trigo',
    'pty01',
    'mqns_01_clone',
    'mqns_02_clone',
    'mqns_03_clone',
    'mqns_04_clone',
    'netns_netlink',
    'netns_breakns_ns_exec_ipv4_netlink',
    'netns_breakns_ns_exec_ipv6_netlink',
    'netns_breakns_ns_exec_ipv4_ioctl',
    'netns_breakns_ns_exec_ipv6_ioctl',
    'netns_breakns_ip_ipv4_netlink',
    'netns_breakns_ip_ipv6_netlink',
    'netns_breakns_ip_ipv4_ioctl',
    'netns_breakns_ip_ipv6_ioctl',
    'netns_comm_ns_exec_ipv4_netlink',
    'netns_comm_ns_exec_ipv6_netlink',
    'netns_comm_ns_exec_ipv4_ioctl',
    'netns_comm_ns_exec_ipv6_ioctl',
    'netns_comm_ip_ipv4_netlink',
    'netns_comm_ip_ipv6_netlink',
    'netns_comm_ip_ipv4_ioctl',
    'netns_comm_ip_ipv6_ioctl',
    'netns_sysfs',
    'shmnstest_none',
    'shmnstest_clone',
    'shmnstest_unshare',
    'shmem_2nstest_none',
    'shmem_2nstest_clone',
    'shmem_2nstest_unshare',
    'mesgq_nstest_none',
    'mesgq_nstest_clone',
    'mesgq_nstest_unshare',
    'sem_nstest_none',
    'sem_nstest_clone',
    'sem_nstest_unshare',
    'semtest_2ns_none',
    'semtest_2ns_clone',
    'semtest_2ns_unshare',
    'BindMounts',
    'Filecaps',
    'Cap_bounds',
    'FCNTL_LOCKTESTS',
    'su01',
    'cron02',
    'cron_deny01',
    'cron_allow01',
    'cron_dirs_checks01',
    'Numa_testcases',
    'move_pages03',
    'move_pages11',
    'hugemmap05_1',
    'hugemmap05_2',
    'hugemmap05_3',
    'ar',
    'ld',
    'ldd',
    'nm',
    'objdump',
    'file',
    'tar',
    'cron',
    'logrotate',
    'mail',
    'cpio',
    'unzip01',
    'cp_tests01',
    'ln_tests01',
    'mkdir_tests01',
    'mv_tests01',
    'size01',
    'sssd01',
    'sssd02',
    'sssd03',
    'du01',
    'mkfs01',
    'which01',
    'lsmod01',
    'wc01',
    'smt_smp_enabled',
    'smt_smp_affinity',
    'zram03',
    'ext4_uninit_groups',
    'ext4_persist_prealloc',
    'pipeio_1',
    'pipeio_4',
    'pipeio_5',
    'pipeio_6',
    'pipeio_8',
    'cpuhotplug03',
    'cpuhotplug06',
    'input06',
    'dio10',
    'fsx_linux',
    'dio04',
    'Numa_testcases',
    'ext4_uninit_groups',
    'ext4_persist_prealloc',
    'connect01',
    'prot_hsymlinks',
    'fs-ftest01',
    'fs-ftest03',
    'fs-ftest04',
    'fs-ftest05',
    'fs-ftest07',
    'fs-ftest08',
    'fs-inode02',
    'ipc-signal_test_01',
    'mm-data_space',
    'mm-mmapstress01',
    'mm-mmapstress03',
    'mm-mmapstress09',
    'mm-mmapstress10',
    'syscalls-clock_nanosleep01',
    'syscalls-clone04',
    'syscalls-fcntl14',
    'syscalls-fcntl14',
    'syscalls-fcntl14_64',
    'syscalls-fcntl17',
    'syscalls-fcntl17_64',
    'syscalls-getdomainname01',
    'syscalls-kill12',
    'syscalls-setdomainname01',
    'syscalls-setdomainname02',
    'syscalls-setdomainname03',
    'syscalls-sighold02',
    'syscalls-sigpending02',
    'syscalls-sigrelse01',
    'syscalls-vfork02',
]
