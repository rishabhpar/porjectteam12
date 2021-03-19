class BaseConfig(object):
	DEBUG = True
	DEVELOPMENT = False
	SECRET_KEY = b'\xda\xba[\x7f\xa4\xbe\x0ce8\xde>*#6"='
	MONGODB_SETTINGS = {
		# 'USERNAME': None,
		# 'PASSWORD': None,
		'HOST': '127.0.0.1',
		'PORT': 27017,
		'DB': 'user_acct_info'
	}

class ProductionConfig(object):
	DEBUG = False
	DEVELOPMENT = False