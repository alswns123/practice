import hashlib 
HASH_NAME = "md5" # hash algorithm (md5,sha1,sha224,sha256,sha384,sha512) 
txt = input("Enter the text to convert: ") 
text = txt.encode('utf-8') 
md5 = hashlib.new(HASH_NAME) 
md5.update(text) 
result = md5.hexdigest() 
print("HASH: %s" % result)

