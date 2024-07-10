characters = "abcdefghijklmnopqrstuvwxyz"

character_count = len(characters)

print("Supported Characters:\n" + characters + "\n")

def encrypt_character(plain, key):
  key_code = characters.index(key)
  plain_code = characters.index(plain)

  cipher_code = (key_code + plain_code) % character_count
  cipher = characters[cipher_code]
  return cipher

def encrypt(plain, key):
  cipher = ""
  for (plain_index, plain_character) in enumerate(plain):

    key_index = plain_index % len(key)
    key_character = key[key_index]
    
    cipher_character = encrypt_character(plain_character, key_character)
    cipher += cipher_character
  return cipher 
def invert_character(character):
  character_code = characters.index(character)
  inverted_character = (character_count - character_code) % character_count
  inverted_character = characters[inverted_character]
return inverted_character

def invert(text):
  inverted_text = ""

for character in text:
  inverted_text += invert_character(character)
  return inverted_text

plaintext = "secretmessage"
keytext = "key"
ciphertext = encrypt(plaintext, keytext)

print("Message: " + plaintext)
print("Password: " + keytext)
print("Output: " + ciphertext)

