from cards import *


"""Handles Card Tap event.
This event is raised when a user taps his phone on the reader.
"""
def card_tap_handler(card_info):
    if not card_info.is_success:
        print('Failed reading card, error: %d' % card_info.error)
        return

    print('Card read, user ID: %s' % card_info.card_details.user_id)

    '''
    Your code goes here!
    Do whatever you want with the accepted User ID!

    -----------------------
    Example: Open the door, if the user is authorized
    -----------------------
    if YourSystem.IsAuthorizedToOpenDoor(card_info.card_details.user_id, Doors.Hallway):
        YourSystem.OpenDoor(Doors.Hallway)

    -----------------------
    Example: Remove balance
    ----------------------
    YourSystem.Users.ChangeBalance(card_info.card_details.user_id, -10);
    '''


"""Handles reader status change."""
def status_change_handler(status):
    if status is ReaderStatus.Disconnected:
        print('Card reader has been disconnected')
    elif status is ReaderStatus.Connected:
        print('Card reader has been connected')
    else:
        print('Error: unknown status change')


def main():
    # Initialize the ReaderCredentials and ReaderSettings objects with wanted / needed parameters
    reader_credentials = ReaderCredentials('ABCD1234ABCD1234ABCD1234')
    reader_settings = ReaderSettings('ACS - ACR122U PICC Interface')

    # Initialize the CardReader object with ReaderCredentials and ReaderSettings.
    card_reader = CardReader(reader_settings, reader_credentials)

    # Set the on_card_tap and on_status_change events
    card_reader.on_card_tap = card_tap_handler
    card_reader.on_status_change = status_change_handler

    # Start listening
    card_reader.listen()


if __name__ == "__main__":
    main()
