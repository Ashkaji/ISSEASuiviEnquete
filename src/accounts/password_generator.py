import random
import string

# Define the character sets for the password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()"

# Combine all character sets
all_chars = lowercase + uppercase + digits + symbols


def generate_password(length: int = 12) -> str:
    """
      Generates a random password of the specified length.

      Args:
          length (int, optional): The desired length of the password. Defaults to 12.

      Returns:
          str: The generated password.
      """
    # Generate a random password with at least one character from each set
    password = (
            random.choice(lowercase)
            + random.choice(uppercase)
            + random.choice(digits)
            + random.choice(symbols)
    )

    # Fill the remaining characters with random selections from all characters
    password += ''.join(random.sample(all_chars, length - 4))

    # Shuffle the characters for better randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password
