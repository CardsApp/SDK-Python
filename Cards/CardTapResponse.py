class CardTapError:
	"""Card Tap Error Enum"""
	InternetError = 1
	ApiKeyInvalid = 2
	TransactionTokenInvalid = 3
	UserNotAssociatedWithCardReader = 4
	NoSuchTPID = 5
	TransactionTokenMissing = 6
	TransactionTokenDoesntExist = 7
	TransactionTokenAlreadyUsed = 8
	TransactionTokenAlreadyValidated = 9
	
class CardTapResponse:
	"""Card Tap Response Class"""
	def __init__(self, is_success, error, card_details):
		self.is_success = is_success
		self.error = error
		self.card_details = card_details