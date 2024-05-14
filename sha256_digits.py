import sys, hashlib
assert len(sys.argv) == 2, 'As input should be filepath.'
data_filepath = sys.argv[1]
hash_digits = hashlib.sha256(open(data_filepath, 'rb').read()).hexdigest()
print(hash_digits)
