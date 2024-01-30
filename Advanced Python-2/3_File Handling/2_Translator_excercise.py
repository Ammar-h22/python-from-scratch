# We have to create a translator:
from translate import Translator

# translator = Translator(to_lang='hi')  # Converting into hindi
# translator = Translator(to_lang='mr')  # Converting into marathi
# translator = Translator(to_lang='ur')  # Converting into urdu
translator = Translator(to_lang='ja')  # Converting into japanese

# This will print the translated version of the file
# try:
#     with open('textbook.txt', 'r') as my_file:
#         text = my_file.read()
#         translation = translator.translate(text)
#         print(translation)
# except FileNotFoundError:
#     print('File not found!')


# We can also put the translated version in another file:
try:
    with open('textbook.txt', 'r') as my_file2:
        text = my_file2.read()
        translation = translator.translate(text)
        with open('japanese_book.txt', 'w', encoding='utf-8') as my_file3:
            my_file3.write(translation)
except FileNotFoundError:
    print('File not found!')
