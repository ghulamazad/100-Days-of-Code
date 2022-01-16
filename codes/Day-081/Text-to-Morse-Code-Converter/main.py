morse_code = {
    'A': '•–', 'B': '–•••', 'C': '–•–•', 'D': '–••', 'E': '•', 'F': '••–•', 'G': '––•', 'H': '••••', 'I': '••', 'J': '•–––', 'K': '–•–', 'L': '•–••', 'M': '––', 'N': '–•', 'O': '––––', 'P': '•––•', 'Q': '––•–',
    'R': '•–•', 'S': '•••', 'T': '–', 'U': '••–', 'V': '•••–', 'W': '•––', 'X': '–••–', 'Y': '–•––', 'Z': '––••', '0': '–––––', '1': '•––––', '2': '••–––', '3': '•••––', '4': '••••–', '5': '•••••', '6': '–••••',
    '7': '––•••', '8': '–––••', '9': '––––•'
}

print("".center(30, "="))
print("WELCOME".center(30, " "))
print("Text to Morse code Converter")
print("".center(30, "="), end="\n\n")

text = input("Enter Text: ").upper()

print("Morse Code: ", end="")
for char in text:
    print(morse_code.get(char) or char, end=" ")
