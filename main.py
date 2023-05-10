eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print('Выберите операцию, введя соответствующую цифру: 1 - зашифровать, 2 - расшифровать ')
operation = int(input())
print('Выберите алфавит, введя соответствующую цифру: 1 - русский, 2 - английский')
language = int(input())
print('Введите шаг сдвига: ')
shift = int(input())

new_text = ''

if operation == 1:
    if language == 1:
        print('Введите исходный тескт на русском языке, который требуется зашифровать:')
        text = input()
        for c in text:
            if c in rus_lower_alphabet:
                c_ind = rus_lower_alphabet.index(c)
                new_text += rus_lower_alphabet[(c_ind + shift) % 32]
            elif c in rus_upper_alphabet:
                c_ind = rus_upper_alphabet.index(c)
                new_text += rus_upper_alphabet[(c_ind + shift) % 32]
            else:
                new_text += c
        print('Зашифрованный текст:', new_text, sep="\n")
    else:
        print('Введите исходный тескт на английском языке, который требуется зашифровать:')
        text = input()
        for c in text:
            if c in eng_lower_alphabet:
                c_ind = eng_lower_alphabet.index(c)
                new_text += eng_lower_alphabet[(c_ind + shift) % 26]
            elif c in eng_upper_alphabet:
                c_ind = eng_upper_alphabet.index(c)
                new_text += eng_upper_alphabet[(c_ind + shift) % 26]
            else:
                new_text += c
        print('Зашифрованный текст:', new_text, sep="\n")
else:
    if language == 1:
        print('Введите зашифрованный тескт на русском языке, который требуется расшифровать:')
        text = input()
        for c in text:
            if c in rus_lower_alphabet:
                c_ind = rus_lower_alphabet.index(c)
                new_text += rus_lower_alphabet[(c_ind - shift) % 32]
            elif c in rus_upper_alphabet:
                c_ind = rus_upper_alphabet.index(c)
                new_text += rus_upper_alphabet[(c_ind - shift) % 32]
            else:
                new_text += c
        print('Расшифрованный тект:', new_text, sep="\n")
    else:
        print('Введите зашифрованный тескт на английском языке, который требуется расшифровать:')
        text = input()
        for i in range(shift):
            new_text = ''
            for c in text:
                if c in eng_lower_alphabet:
                    c_ind = eng_lower_alphabet.index(c)
                    new_text += eng_lower_alphabet[(c_ind - i) % 26]
                elif c in eng_upper_alphabet:
                    c_ind = eng_upper_alphabet.index(c)
                    new_text += eng_upper_alphabet[(c_ind - i) % 26]
                else:
                    new_text += c
            print(i + 1, ")", new_text, sep=" ", end="\n")

