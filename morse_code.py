import tkinter as tk

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

def encode_to_morse():
    text = entry.get().upper()
    encoded_message = ''
    for char in text:
        if char in morse_code_dict:
            encoded_message += morse_code_dict[char] + ' '
    result_label.config(text=encoded_message.strip())

def decode_from_morse():
    code = entry.get().split()
    decoded_message = ''
    for char in code:
        for key, value in morse_code_dict.items():
            if char == value:
                decoded_message += key
                break
    result_label.config(text=decoded_message)

# GUI setup
window = tk.Tk()
window.title("My MorseCode Translator")

# Entry field
entry = tk.Entry(window, bg="DeepSkyBlue3", fg="black", font=("Times New Roman", 30))
entry.pack(pady=50)

# Buttons
encode_button = tk.Button(window, height=3, width=20, bg="DeepSkyBlue4", fg="white", text="ENCODE" , command=encode_to_morse)
encode_button.pack(pady=10)

decode_button = tk.Button(window, height=3, width=20, bg="DeepSkyBlue4", fg="white", text="DECODE", command=decode_from_morse)
decode_button.pack(pady=10)

# Result label
result_label = tk.Label(window, bg="DeepSkyBlue3", fg="black", font=("Times New Roman", 30), wraplength=300)
result_label.pack(pady=30)

window.mainloop()
