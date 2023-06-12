import bcrypt

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt(12))

hash = get_hashed_password('Ramchadra32342423re')

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode(), hashed_password)
print(check_password('Ramchadra32342423r', hash))
