import hashlib

# User creates a password
password = input("Enter your password: ")

# Convert password to MD5 hash
hash_object = hashlib.md5(password.encode())
password_hash = hash_object.hexdigest()

print("\nYour password is stored as MD5 hash:")
print(password_hash)

# Login simulation
login_password = input("\nEnter password again to login: ")
login_hash = hashlib.md5(login_password.encode()).hexdigest()

if login_hash == password_hash:
    print("✅ Login successful")
else:
    print("❌ Wrong password")
