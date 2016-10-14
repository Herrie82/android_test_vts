#include "hardware/interfaces/nfc/1.0/vts/types.vts.h"
#include "hardware/interfaces/nfc/1.0/vts/types.vts.h"

using namespace android::hardware;
using namespace android::hardware::nfc::V1_0;

namespace android {
namespace vts {

void profile__NfcEvent(VariableSpecificationMessage* arg_name,
NfcEvent arg_val_name) {
    arg_name->set_type(TYPE_ENUM);
    arg_name->mutable_enum_value()->add_scalar_value()->set_uint32_t(static_cast<uint32_t>(arg_val_name));
    arg_name->mutable_enum_value()->set_scalar_type("uint32_t");
}

void profile__NfcStatus(VariableSpecificationMessage* arg_name,
NfcStatus arg_val_name) {
    arg_name->set_type(TYPE_ENUM);
    arg_name->mutable_enum_value()->add_scalar_value()->set_uint32_t(static_cast<uint32_t>(arg_val_name));
    arg_name->mutable_enum_value()->set_scalar_type("uint32_t");
}

}  // namespace vts
}  // namespace android