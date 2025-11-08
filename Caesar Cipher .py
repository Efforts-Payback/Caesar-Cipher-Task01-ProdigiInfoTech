# Caesar Cipher Implementation
# Task-01 for Internship

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift uppercase letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# --- Main Program ---
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

print("\n--- Results ---")
encrypted = encrypt(message, shift)
print(f"Encrypted Message: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted Message: {decrypted}")
