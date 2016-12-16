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

LOCAL_PATH := $(call my-dir)

# TODO(trong): enable for mips and x86.
ifeq (,$(findstring mips, $(TARGET_ARCH)))
ifeq (,$(findstring x86, $(TARGET_ARCH)))

include $(CLEAR_VARS)

module_name := ILightSetLight_fuzzer
module_src_files := ILightSetLight_fuzzer.cpp
module_shared_libraries := \
    android.hardware.light@2.0 \

include test/vts/testcases/hal/common/fuzz/Android.hal_fuzzer_blind.mk

endif
endif
