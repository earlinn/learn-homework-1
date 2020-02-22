# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове "{word}": {word[-1]}')


# Вывести количество букв "а" в слове
word = 'Архангельск'
letter_in_word = word.lower().count('а')
print(f'Количество букв "а" в слове "{word}": {letter_in_word}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
lower_case_word, vowels_in_word = word.lower(), 0
vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
for vowel in vowels:
    if vowel in lower_case_word:
        vowels_in_word += lower_case_word.count(vowel)
print(f'Количество гласных букв в слове "{word}": {vowels_in_word}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words_num = len(sentence.split())
print(f'Количество слов в предложении "{sentence}": {words_num}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f'Выведем первую букву каждого слова в предложении "{sentence}" на отдельной строке:')
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence_splited = sentence.split()
len_words_in_sentence = [len(word) for word in sentence_splited]
average_len_of_a_word = sum(len_words_in_sentence) / len(sentence_splited)
print(f'Усредненная длина слова в предложении "{sentence}": {average_len_of_a_word}')
