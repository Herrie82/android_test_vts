# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VtsReportMessage.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VtsReportMessage.proto',
  package='android.vts',
  serialized_pb='\n\x16VtsReportMessage.proto\x12\x0b\x61ndroid.vts\"\xe0\x01\n\x18\x41ndroidDeviceInfoMessage\x12\x14\n\x0cproduct_type\x18\x01 \x01(\x0c\x12\x17\n\x0fproduct_variant\x18\x02 \x01(\x0c\x12\x14\n\x0c\x62uild_flavor\x18\x0b \x01(\x0c\x12\x10\n\x08\x62uild_id\x18\x0c \x01(\x0c\x12\x0e\n\x06\x62ranch\x18\x15 \x01(\x0c\x12\x13\n\x0b\x62uild_alias\x18\x16 \x01(\x0c\x12\x11\n\tapi_level\x18\x1f \x01(\x0c\x12\x10\n\x08\x61\x62i_name\x18\x33 \x01(\x0c\x12\x13\n\x0b\x61\x62i_bitness\x18\x34 \x01(\x0c\x12\x0e\n\x06serial\x18\x65 \x01(\x0c\"g\n\x10\x41ndroidBuildInfo\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x0b \x01(\x0c\x12\x12\n\nbuild_type\x18\x0c \x01(\x0c\x12\x0e\n\x06\x62ranch\x18\r \x01(\x0c\x12\x15\n\rbuild_summary\x18\x15 \x01(\x0c\"\x1f\n\x0bVtsHostInfo\x12\x10\n\x08hostname\x18\x01 \x01(\x0c\"\xf5\x01\n\x15TestCaseReportMessage\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x30\n\x0btest_result\x18\x0b \x01(\x0e\x32\x1b.android.vts.TestCaseResult\x12\x17\n\x0fstart_timestamp\x18\x15 \x01(\x03\x12\x15\n\rend_timestamp\x18\x16 \x01(\x03\x12\x34\n\x08\x63overage\x18\x1f \x03(\x0b\x32\".android.vts.CoverageReportMessage\x12\x36\n\tprofiling\x18) \x03(\x0b\x32#.android.vts.ProfilingReportMessage\"\xa0\x02\n\x16ProfilingReportMessage\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.android.vts.VtsProfilingType\x12@\n\x0fregression_mode\x18\x03 \x01(\x0e\x32\'.android.vts.VtsProfilingRegressionMode\x12\x17\n\x0fstart_timestamp\x18\x0b \x01(\x03\x12\x15\n\rend_timestamp\x18\x0c \x01(\x03\x12\r\n\x05label\x18\x15 \x03(\x0c\x12\r\n\x05value\x18\x16 \x03(\x03\x12\x14\n\x0cx_axis_label\x18\x1f \x01(\x0c\x12\x14\n\x0cy_axis_label\x18  \x01(\x0c\x12\x0f\n\x07options\x18) \x03(\x0c\"\xe5\x01\n\x15\x43overageReportMessage\x12\x11\n\tfile_path\x18\x0b \x01(\x0c\x12\x14\n\x0cproject_name\x18\x0c \x01(\x0c\x12\x10\n\x08revision\x18\r \x01(\x0c\x12\x1c\n\x14line_coverage_vector\x18\x17 \x03(\x05\x12\x18\n\x10total_line_count\x18\x65 \x01(\x05\x12\x1a\n\x12\x63overed_line_count\x18\x66 \x01(\x05\x12\x14\n\x08\x64ir_path\x18\x01 \x01(\x0c\x42\x02\x18\x01\x12\x15\n\tfile_name\x18\x02 \x01(\x0c\x42\x02\x18\x01\x12\x10\n\x04html\x18\x03 \x01(\x0c\x42\x02\x18\x01\"\xed\x03\n\x11TestReportMessage\x12\x12\n\ntest_suite\x18\x01 \x01(\x0c\x12\x0c\n\x04test\x18\x02 \x01(\x0c\x12+\n\ttest_type\x18\x03 \x01(\x0e\x32\x18.android.vts.VtsTestType\x12:\n\x0b\x64\x65vice_info\x18\x04 \x03(\x0b\x32%.android.vts.AndroidDeviceInfoMessage\x12\x31\n\nbuild_info\x18\x05 \x01(\x0b\x32\x1d.android.vts.AndroidBuildInfo\x12\x18\n\x10subscriber_email\x18\x06 \x03(\x0c\x12+\n\thost_info\x18\x07 \x01(\x0b\x32\x18.android.vts.VtsHostInfo\x12\x35\n\ttest_case\x18\x0b \x03(\x0b\x32\".android.vts.TestCaseReportMessage\x12\x36\n\tprofiling\x18\x15 \x03(\x0b\x32#.android.vts.ProfilingReportMessage\x12\x17\n\x0fstart_timestamp\x18\x65 \x01(\x03\x12\x15\n\rend_timestamp\x18\x66 \x01(\x03\x12\x34\n\x08\x63overage\x18g \x03(\x0b\x32\".android.vts.CoverageReportMessage*\xb3\x01\n\x0eTestCaseResult\x12\x12\n\x0eUNKNOWN_RESULT\x10\x00\x12\x19\n\x15TEST_CASE_RESULT_PASS\x10\x01\x12\x19\n\x15TEST_CASE_RESULT_FAIL\x10\x02\x12\x19\n\x15TEST_CASE_RESULT_SKIP\x10\x03\x12\x1e\n\x1aTEST_CASE_RESULT_EXCEPTION\x10\x04\x12\x1c\n\x18TEST_CASE_RESULT_TIMEOUT\x10\x05*\x9c\x01\n\x0bVtsTestType\x12\x18\n\x14UNKNOWN_VTS_TESTTYPE\x10\x00\x12\x1e\n\x1aVTS_HOST_DRIVEN_STRUCTURAL\x10\x01\x12\x1b\n\x17VTS_HOST_DRIVEN_FUZZING\x10\x02\x12\x19\n\x15VTS_TARGET_SIDE_GTEST\x10\x03\x12\x1b\n\x17VTS_TARGET_SIDE_FUZZING\x10\x04*\xa3\x01\n\x1aVtsProfilingRegressionMode\x12\x1b\n\x17UNKNOWN_REGRESSION_MODE\x10\x00\x12 \n\x1cVTS_REGRESSION_MODE_DISABLED\x10\x01\x12\"\n\x1eVTS_REGRESSION_MODE_INCREASING\x10\x02\x12\"\n\x1eVTS_REGRESSION_MODE_DECREASING\x10\x03*{\n\x10VtsProfilingType\x12\x1e\n\x1aUNKNOWN_VTS_PROFILING_TYPE\x10\x00\x12 \n\x1cVTS_PROFILING_TYPE_TIMESTAMP\x10\x01\x12%\n!VTS_PROFILING_TYPE_LABELED_VECTOR\x10\x02\x42)\n\x15\x63om.android.vts.protoB\x10VtsReportMessage')

_TESTCASERESULT = _descriptor.EnumDescriptor(
  name='TestCaseResult',
  full_name='android.vts.TestCaseResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_RESULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_PASS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_FAIL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_SKIP', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_EXCEPTION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_TIMEOUT', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1672,
  serialized_end=1851,
)

TestCaseResult = enum_type_wrapper.EnumTypeWrapper(_TESTCASERESULT)
_VTSTESTTYPE = _descriptor.EnumDescriptor(
  name='VtsTestType',
  full_name='android.vts.VtsTestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VTS_TESTTYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_HOST_DRIVEN_STRUCTURAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_HOST_DRIVEN_FUZZING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_TARGET_SIDE_GTEST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_TARGET_SIDE_FUZZING', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1854,
  serialized_end=2010,
)

VtsTestType = enum_type_wrapper.EnumTypeWrapper(_VTSTESTTYPE)
_VTSPROFILINGREGRESSIONMODE = _descriptor.EnumDescriptor(
  name='VtsProfilingRegressionMode',
  full_name='android.vts.VtsProfilingRegressionMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_REGRESSION_MODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_REGRESSION_MODE_DISABLED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_REGRESSION_MODE_INCREASING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_REGRESSION_MODE_DECREASING', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2013,
  serialized_end=2176,
)

VtsProfilingRegressionMode = enum_type_wrapper.EnumTypeWrapper(_VTSPROFILINGREGRESSIONMODE)
_VTSPROFILINGTYPE = _descriptor.EnumDescriptor(
  name='VtsProfilingType',
  full_name='android.vts.VtsProfilingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VTS_PROFILING_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_PROFILING_TYPE_TIMESTAMP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_PROFILING_TYPE_LABELED_VECTOR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2178,
  serialized_end=2301,
)

VtsProfilingType = enum_type_wrapper.EnumTypeWrapper(_VTSPROFILINGTYPE)
UNKNOWN_RESULT = 0
TEST_CASE_RESULT_PASS = 1
TEST_CASE_RESULT_FAIL = 2
TEST_CASE_RESULT_SKIP = 3
TEST_CASE_RESULT_EXCEPTION = 4
TEST_CASE_RESULT_TIMEOUT = 5
UNKNOWN_VTS_TESTTYPE = 0
VTS_HOST_DRIVEN_STRUCTURAL = 1
VTS_HOST_DRIVEN_FUZZING = 2
VTS_TARGET_SIDE_GTEST = 3
VTS_TARGET_SIDE_FUZZING = 4
UNKNOWN_REGRESSION_MODE = 0
VTS_REGRESSION_MODE_DISABLED = 1
VTS_REGRESSION_MODE_INCREASING = 2
VTS_REGRESSION_MODE_DECREASING = 3
UNKNOWN_VTS_PROFILING_TYPE = 0
VTS_PROFILING_TYPE_TIMESTAMP = 1
VTS_PROFILING_TYPE_LABELED_VECTOR = 2



_ANDROIDDEVICEINFOMESSAGE = _descriptor.Descriptor(
  name='AndroidDeviceInfoMessage',
  full_name='android.vts.AndroidDeviceInfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_type', full_name='android.vts.AndroidDeviceInfoMessage.product_type', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_variant', full_name='android.vts.AndroidDeviceInfoMessage.product_variant', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_flavor', full_name='android.vts.AndroidDeviceInfoMessage.build_flavor', index=2,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_id', full_name='android.vts.AndroidDeviceInfoMessage.build_id', index=3,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='branch', full_name='android.vts.AndroidDeviceInfoMessage.branch', index=4,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_alias', full_name='android.vts.AndroidDeviceInfoMessage.build_alias', index=5,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='api_level', full_name='android.vts.AndroidDeviceInfoMessage.api_level', index=6,
      number=31, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='abi_name', full_name='android.vts.AndroidDeviceInfoMessage.abi_name', index=7,
      number=51, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='abi_bitness', full_name='android.vts.AndroidDeviceInfoMessage.abi_bitness', index=8,
      number=52, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial', full_name='android.vts.AndroidDeviceInfoMessage.serial', index=9,
      number=101, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=40,
  serialized_end=264,
)


_ANDROIDBUILDINFO = _descriptor.Descriptor(
  name='AndroidBuildInfo',
  full_name='android.vts.AndroidBuildInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='android.vts.AndroidBuildInfo.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.AndroidBuildInfo.name', index=1,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_type', full_name='android.vts.AndroidBuildInfo.build_type', index=2,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='branch', full_name='android.vts.AndroidBuildInfo.branch', index=3,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_summary', full_name='android.vts.AndroidBuildInfo.build_summary', index=4,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=266,
  serialized_end=369,
)


_VTSHOSTINFO = _descriptor.Descriptor(
  name='VtsHostInfo',
  full_name='android.vts.VtsHostInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='android.vts.VtsHostInfo.hostname', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=371,
  serialized_end=402,
)


_TESTCASEREPORTMESSAGE = _descriptor.Descriptor(
  name='TestCaseReportMessage',
  full_name='android.vts.TestCaseReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.TestCaseReportMessage.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_result', full_name='android.vts.TestCaseReportMessage.test_result', index=1,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='android.vts.TestCaseReportMessage.start_timestamp', index=2,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='android.vts.TestCaseReportMessage.end_timestamp', index=3,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coverage', full_name='android.vts.TestCaseReportMessage.coverage', index=4,
      number=31, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='profiling', full_name='android.vts.TestCaseReportMessage.profiling', index=5,
      number=41, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=405,
  serialized_end=650,
)


_PROFILINGREPORTMESSAGE = _descriptor.Descriptor(
  name='ProfilingReportMessage',
  full_name='android.vts.ProfilingReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.ProfilingReportMessage.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='android.vts.ProfilingReportMessage.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='regression_mode', full_name='android.vts.ProfilingReportMessage.regression_mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='android.vts.ProfilingReportMessage.start_timestamp', index=3,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='android.vts.ProfilingReportMessage.end_timestamp', index=4,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='android.vts.ProfilingReportMessage.label', index=5,
      number=21, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='android.vts.ProfilingReportMessage.value', index=6,
      number=22, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_axis_label', full_name='android.vts.ProfilingReportMessage.x_axis_label', index=7,
      number=31, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_axis_label', full_name='android.vts.ProfilingReportMessage.y_axis_label', index=8,
      number=32, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='android.vts.ProfilingReportMessage.options', index=9,
      number=41, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=653,
  serialized_end=941,
)


_COVERAGEREPORTMESSAGE = _descriptor.Descriptor(
  name='CoverageReportMessage',
  full_name='android.vts.CoverageReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='android.vts.CoverageReportMessage.file_path', index=0,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project_name', full_name='android.vts.CoverageReportMessage.project_name', index=1,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revision', full_name='android.vts.CoverageReportMessage.revision', index=2,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_coverage_vector', full_name='android.vts.CoverageReportMessage.line_coverage_vector', index=3,
      number=23, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_line_count', full_name='android.vts.CoverageReportMessage.total_line_count', index=4,
      number=101, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='covered_line_count', full_name='android.vts.CoverageReportMessage.covered_line_count', index=5,
      number=102, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dir_path', full_name='android.vts.CoverageReportMessage.dir_path', index=6,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='android.vts.CoverageReportMessage.file_name', index=7,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
    _descriptor.FieldDescriptor(
      name='html', full_name='android.vts.CoverageReportMessage.html', index=8,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=944,
  serialized_end=1173,
)


_TESTREPORTMESSAGE = _descriptor.Descriptor(
  name='TestReportMessage',
  full_name='android.vts.TestReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_suite', full_name='android.vts.TestReportMessage.test_suite', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test', full_name='android.vts.TestReportMessage.test', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_type', full_name='android.vts.TestReportMessage.test_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='android.vts.TestReportMessage.device_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_info', full_name='android.vts.TestReportMessage.build_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscriber_email', full_name='android.vts.TestReportMessage.subscriber_email', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host_info', full_name='android.vts.TestReportMessage.host_info', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_case', full_name='android.vts.TestReportMessage.test_case', index=7,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='profiling', full_name='android.vts.TestReportMessage.profiling', index=8,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='android.vts.TestReportMessage.start_timestamp', index=9,
      number=101, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='android.vts.TestReportMessage.end_timestamp', index=10,
      number=102, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coverage', full_name='android.vts.TestReportMessage.coverage', index=11,
      number=103, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1176,
  serialized_end=1669,
)

_TESTCASEREPORTMESSAGE.fields_by_name['test_result'].enum_type = _TESTCASERESULT
_TESTCASEREPORTMESSAGE.fields_by_name['coverage'].message_type = _COVERAGEREPORTMESSAGE
_TESTCASEREPORTMESSAGE.fields_by_name['profiling'].message_type = _PROFILINGREPORTMESSAGE
_PROFILINGREPORTMESSAGE.fields_by_name['type'].enum_type = _VTSPROFILINGTYPE
_PROFILINGREPORTMESSAGE.fields_by_name['regression_mode'].enum_type = _VTSPROFILINGREGRESSIONMODE
_TESTREPORTMESSAGE.fields_by_name['test_type'].enum_type = _VTSTESTTYPE
_TESTREPORTMESSAGE.fields_by_name['device_info'].message_type = _ANDROIDDEVICEINFOMESSAGE
_TESTREPORTMESSAGE.fields_by_name['build_info'].message_type = _ANDROIDBUILDINFO
_TESTREPORTMESSAGE.fields_by_name['host_info'].message_type = _VTSHOSTINFO
_TESTREPORTMESSAGE.fields_by_name['test_case'].message_type = _TESTCASEREPORTMESSAGE
_TESTREPORTMESSAGE.fields_by_name['profiling'].message_type = _PROFILINGREPORTMESSAGE
_TESTREPORTMESSAGE.fields_by_name['coverage'].message_type = _COVERAGEREPORTMESSAGE
DESCRIPTOR.message_types_by_name['AndroidDeviceInfoMessage'] = _ANDROIDDEVICEINFOMESSAGE
DESCRIPTOR.message_types_by_name['AndroidBuildInfo'] = _ANDROIDBUILDINFO
DESCRIPTOR.message_types_by_name['VtsHostInfo'] = _VTSHOSTINFO
DESCRIPTOR.message_types_by_name['TestCaseReportMessage'] = _TESTCASEREPORTMESSAGE
DESCRIPTOR.message_types_by_name['ProfilingReportMessage'] = _PROFILINGREPORTMESSAGE
DESCRIPTOR.message_types_by_name['CoverageReportMessage'] = _COVERAGEREPORTMESSAGE
DESCRIPTOR.message_types_by_name['TestReportMessage'] = _TESTREPORTMESSAGE

class AndroidDeviceInfoMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ANDROIDDEVICEINFOMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.AndroidDeviceInfoMessage)

class AndroidBuildInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ANDROIDBUILDINFO

  # @@protoc_insertion_point(class_scope:android.vts.AndroidBuildInfo)

class VtsHostInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VTSHOSTINFO

  # @@protoc_insertion_point(class_scope:android.vts.VtsHostInfo)

class TestCaseReportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTCASEREPORTMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.TestCaseReportMessage)

class ProfilingReportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROFILINGREPORTMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.ProfilingReportMessage)

class CoverageReportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COVERAGEREPORTMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.CoverageReportMessage)

class TestReportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTREPORTMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.TestReportMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\025com.android.vts.protoB\020VtsReportMessage')
_COVERAGEREPORTMESSAGE.fields_by_name['dir_path'].has_options = True
_COVERAGEREPORTMESSAGE.fields_by_name['dir_path']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
_COVERAGEREPORTMESSAGE.fields_by_name['file_name'].has_options = True
_COVERAGEREPORTMESSAGE.fields_by_name['file_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
_COVERAGEREPORTMESSAGE.fields_by_name['html'].has_options = True
_COVERAGEREPORTMESSAGE.fields_by_name['html']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
# @@protoc_insertion_point(module_scope)
