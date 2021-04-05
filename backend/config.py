class BaseConfig(object):
	DEBUG = True
	DEVELOPMENT = False
	SECRET_KEY = b'\xda\xba[\x7f\xa4\xbe\x0ce8\xde>*#6"='
	MONGODB_SETTINGS = {
		# 'USERNAME': None,
		# 'PASSWORD': None,
		'HOST': '127.0.0.1',
		'PORT': 27017,
		'DB': 'user_acct_info' # name of the database
	}
	# username = "tejalkulkarni@utexas.edu"
	# password = "team12project"
	# client = MongoClient("mongodb+srv://{username}:{password}@user.tsyze.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(username=username,password=password))
	# user_acct_info = client['user']

class ProductionConfig(object):
	DEBUG = False
	DEVELOPMENT = False