import bcrypt
from . import db
from matchFinder.models import password
from . import txt_parser

def get_hashed_password(plain_text_password):
    '''Hash a password for the first time.
    (Using bcrypt, the salt is saved into the hash itself)'''

    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
	'''Check hashed password.
	Using bcrypt, the salt is saved into the hash itself'''

	return bcrypt.checkpw(
    	plain_text_password.encode('utf-8'),
    	hashed_password)

def create_passwords():
	'''inserts hashed passwords from txt file into db.'''

	keys = txt_parser.load_passwords()
	for key in keys:
		hashed_password = get_hashed_password(key)
		pw = password.Password(password=hashed_password)
		db.session.add(pw)
	db.session.commit()