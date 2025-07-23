import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

def generate_password(user_input):
    try:
        words = user_input.split()
        if len(words) < 2:
            raise ValueError("Enter at least two words for password generation.")

        
        part1 = random.choice(words).capitalize()
        part2 = random.choice(words).lower()
        symbols = string.punctuation
        numbers = ''.join(random.choices(string.digits, k=2))
        symbol = random.choice(symbols)
        password = part1 + part2 + numbers + symbol
        if len(password) < 8:
            password += ''.join(random.choices(string.ascii_letters + string.digits, k=8 - len(password)))

        return password

    except Exception as e:
        print("Error:", e)
        return None

# Main Program
try:
    uid = input("Enter User ID: ")
    name = input("Enter your name: ")
    words_input = input("Enter some random words (min 2 words): ")
    password = generate_password(words_input)

    if password:
        user = User(uid, name, password)
        print("User created successfully!")
        print("Details:", user.details)
    else:
        print("Password generation failed.")

except Exception as e:
    print("An unexpected error occurred:", e)
