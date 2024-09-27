import bcrypt

def encrypt_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


# Verify password during login
def check_password(user, password):
    return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))