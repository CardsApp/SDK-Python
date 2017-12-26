from ctypes import *

class DevicesList(Structure):
    _fields_ = [("names", POINTER(c_char_p)),
                ("count", c_int)]

class CardTapResponse(Structure):
    _fields_ = [("isSuccess", c_int),
                ("errorCode", c_int),
                ("uid", c_char*32)]


CardsBase = windll.LoadLibrary('CardsBase.dll')

createInstanceByName = CardsBase.createInstanceByName
destroyInstance = CardsBase.destroyInstance
runOnCardPresent = CardsBase.runOnCardPresent
getDevicesList = CardsBase.getDevicesList
freeDevicesList = CardsBase.freeDevicesList

getDevicesList.restype = DevicesList
createInstanceByName.restype = c_int
destroyInstance.restype = c_int
runOnCardPresent.restype = None
freeDevicesList.restype = None

CARD_TAP_FUNC = WINFUNCTYPE(None, CardTapResponse)
STATUS_CHANGE_FUNC = WINFUNCTYPE(None, c_int)

def get_devices_list():
    devices_list_struct = getDevicesList()
    devices_list = []

    for i in range(devices_list_struct.count):
    	devices_list.append(devices_list_struct.names[i].decode())

    freeDevicesList(devices_list_struct)
    
    return devices_list

# instance = addressof, a pointer to the instance (address of c_void_p)
# device_name = str
# api_key = str
def create_instance_by_name(instance, device_name, api_key):
    return createInstanceByName(instance, c_char_p(device_name.encode()), c_char_p(api_key.encode()))

# instance = c_void_p
def destroy_instance(instance): 
    return destroyInstance(instance)

# instance = c_void_p
# card_tap_handler = CARD_TAP_FUNC
# status_change_handler = STATUS_CHNAGE_FUNC
def run_on_card_present(instance, card_tap_handler, status_change_handler):
    runOnCardPresent(instance, CARD_TAP_FUNC(card_tap_handler), STATUS_CHANGE_FUNC(status_change_handler))

    
    

