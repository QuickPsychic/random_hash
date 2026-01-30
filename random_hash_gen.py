import hashlib
import random
import string
import sys

def random_hash(length=32):
    
    string_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return hashlib.md5(string_hash.encode()).hexdigest()

for i in range(1, 1000 + 1):
    hash_value = random_hash()
    print(f"Attempt {i}: {hash_value}")

    if hash_value.startswith("00"):
        print("\nSuccess")
        sys.exit(0)

print("\nFailed")
sys.exit(1)
