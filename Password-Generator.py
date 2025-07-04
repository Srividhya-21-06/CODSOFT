import random
import string
def generate_password(pass_length):
    if length_of_password < 4:
        return "❌ Password should be at least 4 characters long."
    alphabets = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation
    password = [
        random.choice(alphabets),
        random.choice(numbers),
        random.choice(characters)
    ]
    all_characters = alphabets + numbers + characters
    password += random.choices(all_characters, k=length_of_password - 3)
    random.shuffle(password)
    return ''.join(password)
while True:
    print("\n🔐 Password Generator")
    try:
        length_of_password = int(
            input("Enter desired password length (minimum 4): "))
        password = generate_password(length_of_password)
        print(f"✅ Your generated password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")
    redo = input("Generate another? (yes/no): ").lower()
    if redo != 'yes':
        print("👋 Exiting Password Generator. Stay secure!")
        break
