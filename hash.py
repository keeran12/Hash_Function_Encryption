import hashlib
from termcolor import colored
from pyfiglet import figlet_format
print((colored(figlet_format("Hash Function Encryption Tool", font ="cybermedium", width="15"),color="blue")))
print("Hash functions are widely used in cryptography to ensure the integrity and authenticity of data.")
print(" ")


def hash_sha224(input_string):
    sha224 = hashlib.sha224(input_string.encode())
    return sha224.hexdigest()
    

def hash_sha256(input_string):
    sha256 = hashlib.sha256(input_string.encode())
    return sha256.hexdigest()
   

def hash_sha384(input_string):
    sha384 = hashlib.sha384(input_string.encode())
    return sha384.hexdigest()
    

def hash_sha512(input_string):
    sha512 = hashlib.sha512(input_string.encode())
    return sha512.hexdigest()
    

def hash_md5(input_string):
    md5 = hashlib.md5(input_string.encode())
    return md5.hexdigest()
    

input_string = input("Enter the string to hash: ")

print("SHA224 hash of \"" + input_string + "\": " + hash_sha224(input_string))
print(" ")
print("SHA256 hash of \"" + input_string + "\": " + hash_sha256(input_string))
print(" ")
print("SHA384 hash of \"" + input_string + "\": " + hash_sha384(input_string))
print(" ")
print("SHA512 hash of \"" + input_string + "\": " + hash_sha512(input_string))
print(" ")
print("MD5 hash of \"" + input_string + "\": " + hash_md5(input_string))