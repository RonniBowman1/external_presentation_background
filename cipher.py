import string

ALPHABET = string.ascii_uppercase

def _prepare_key_shifts(key: str):
    key = key.upper()
    shifts = [ALPHABET.index(ch) for ch in key if ch in ALPHABET]
    if not shifts:
        raise ValueError("Key must contain at least one letter (A–Z).")
    return shifts

def encode(text: str, key: str) -> str:
    shifts = _prepare_key_shifts(key)
    result_chars = []
    key_index = 0

    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            base_ord = ord(base)
            shift = shifts[key_index % len(shifts)]
            key_index += 1
            offset = ord(ch) - base_ord
            new_offset = (offset + shift) % 26
            result_chars.append(chr(base_ord + new_offset))
        else:
            result_chars.append(ch)
    return ''.join(result_chars)

def decode(ciphertext: str, key: str) -> str:
    shifts = _prepare_key_shifts(key)
    result_chars = []
    key_index = 0

    for ch in ciphertext:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            base_ord = ord(base)
            shift = shifts[key_index % len(shifts)]
            key_index += 1
            offset = ord(ch) - base_ord
            new_offset = (offset - shift) % 26
            result_chars.append(chr(base_ord + new_offset))
        else:
            result_chars.append(ch)
    return ''.join(result_chars)

def interactive_cli():
    print("=== Title Cipher ===")
    mode = input("Do you want to (E)ncode or (D)ecode? ").strip().lower()
    if not mode or mode[0] not in ("e", "d"):
        print("Please choose E or D.")
        return

    key = input("Enter the key: ").strip()
    text = input("Enter the text: ")

    if mode[0] == "e":
        result = encode(text, key)
        print("\nEncoded text:")
    else:
        result = decode(text, key)
        print("\nDecoded text:")
    print(result)

if __name__ == "__main__":
    interactive_cli()
