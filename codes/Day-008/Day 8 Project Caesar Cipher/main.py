from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift_amount, caesar_direction):
    shift_amount = shift_amount % 25
    result_text = ''
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if caesar_direction == 'encode':
                new_position = position + shift_amount
                if new_position >= len(alphabet):
                    new_position -= len(alphabet)
            elif caesar_direction == 'decode':
                new_position = position - shift_amount
                if new_position < 0:
                    new_position += len(alphabet)
            print(f"new Position:{new_position}")
            new_letter = alphabet[new_position]
            result_text += new_letter
        else:
            result_text += char

    print(f"The {caesar_direction} text is {result_text}")


print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    caesar(text, shift_amount, direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")
