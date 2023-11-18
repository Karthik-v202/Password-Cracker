import hashlib

def encrypt_words(words, algorithm):
    encrypted_words = []
    for word in words:
        if algorithm == 'sha256':
            encrypted_word = hashlib.sha256(word.encode()).hexdigest()
        elif algorithm == 'sha512':
            encrypted_word = hashlib.sha512(word.encode()).hexdigest()
        elif algorithm == 'sha3':
            encrypted_word = hashlib.sha3_256(word.encode()).hexdigest()
        else:
            raise ValueError("Invalid encryption algorithm")
        encrypted_words.append(encrypted_word)
    
    return encrypted_words

def crack_encrypted_message():
    encrypted_message = input("Enter the encrypted message to crack: ")

    wordlist_path = input("Enter the path of the wordlist: ")
    with open(wordlist_path, 'r') as file:
        words = file.read().splitlines()

    encryption_algorithms = ['sha256', 'sha512', 'sha3']
    
    for algorithm in encryption_algorithms:
        encrypted_words = encrypt_words(words, algorithm)

        for i, encrypted_word in enumerate(encrypted_words):
            if encrypted_word == encrypted_message:
                print(f"Match found! The original word is: {words[i]}")
                print(f"Encryption algorithm used: {algorithm}")
                return

    print("No match found.")

crack_encrypted_message()
