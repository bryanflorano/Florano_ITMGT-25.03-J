def shift_letter(letter, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    adjusted_shift = shift % 26
    if letter.isspace():
        return ' '
    else:
        current_pos = alphabet.index(letter)
        new_pos = (current_pos + adjusted_shift) % 26
    return alphabet[new_pos]

def caesar_cipher(message, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_message = []
    adjusted_shift = shift % 26
    for i in message:
        if i == ' ':
            shifted_message.append(' ')
        else:
            current_pos = alphabet.index(i)
            new_pos = (current_pos + adjusted_shift) % 26
            shifted_message.append(alphabet[new_pos])
    return ''.join(shifted_message)

def shift_by_letter(letter, letter_shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter.isspace():
        return ' '
    else:
        letter_shift_value = alphabet.index(letter_shift)
        current_pos = alphabet.index(letter)
        new_pos = (current_pos + letter_shift_value) % 26
    return alphabet[new_pos]
    
def vigenere_cipher(message, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    adjusted_key = (key * (len(message) // len(key) + 1))[:len(message)]
    shifted_message = []
    j = 0
    for i in message:
        if i == ' ':
            shifted_message.append(' ')
            j += 1
        else:
            current_pos = alphabet.index(i)
            current_key_pos = alphabet.index(adjusted_key[j])
            new_pos = (current_pos + current_key_pos) % 26
            shifted_letter = alphabet[new_pos]
            shifted_message.append(shifted_letter)
            j += 1 
    return ''.join(shifted_message)

def scytale_cipher(message, shift):
    encrypted_message = []
    message_length = len(message)
    if message_length % shift == 0:
        adjust_count = 0
    else:
        adjust_count = (shift * ((len(message) // shift) + 1)) - len(message)
    new_message = message + ("_" * adjust_count)
    for i in range(len(new_message)):
        character_index = (i // shift) + (len(new_message) // shift) * (i % shift)
        character_to_encode = new_message[character_index]
        encrypted_message.append(character_to_encode)
    return ''.join(encrypted_message)

def scytale_decipher(message, shift):
    decrypted_message = []
    for i in range(len(message)):
        character_index = (i // (len(message) // shift)) + shift * (i % (len(message) // shift))
        character_to_decode = message[character_index]
        decrypted_message.append(character_to_decode)
    return ''.join(decrypted_message)