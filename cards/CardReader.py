from cards.ReaderSettings import ReaderSettings
from cards.ReaderCredentials import ReaderCredentials
from cards.NativeBaseDriver import *
from cards.CardDetails import CardDetails
from cards.CardTapResponse import CardTapResponse


class ReaderStatus:
    """Card Tap Error Enum"""
    Disconnected = 1
    Connected = 2
    AlreadyInUse = 3


class CardReader:
    def __init__(self, reader_settings, reader_credentials):
        self.reader_credentials = reader_credentials
        self.on_card_tap = None
        self.on_status_change = None

        if reader_settings is None:
            self.reader_settings = ReaderSettings(get_devices_list()[0])
        else:
            self.reader_settings = reader_settings

        self.__instance = create_instance_by_name(self.reader_settings.device_name, self.reader_credentials.api_key)

    def __del__(self):
        destroy_instance(self.__instance)

    def listen(self):
        run_on_card_present(self.__instance, self.__get_internal_card_tap_handler(), self.on_status_change)

    def __get_internal_card_tap_handler(self):
        def internal_card_tap_handler(card_tap_response):
            response = CardTapResponse(card_tap_response.isSuccess, card_tap_response.errorCode, CardDetails(card_tap_response.uid[:24].decode()))

            self.on_card_tap(response)

        return internal_card_tap_handler
