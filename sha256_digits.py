import sys, hashlib
assert len(sys.argv) == 2, 'As input should be filepath.'
data_filepath = sys.argv[1]
file_data = open(data_filepath, 'rb').read().decode('utf-8', errors='ignore')
hash_digits = hashlib.sha256(file_data.encode('utf-8')).hexdigest()
print(hash_digits)
