from Zakharov_functions import *
letters = [chr(i).upper() for i in range(ord('a'), ord('z') + 1)]
numbers = [str(i) for i in range(0,10)]
letters_and_numbers = letters+numbers

table = [['/', 'A', 'D', 'F', 'G', 'V', 'X'],
         ['A', ' ', ' ', ' ', ' ', ' ', ' '],
         ['D', ' ', ' ', ' ', ' ', ' ', ' '],
         ['F', ' ', ' ', ' ', ' ', ' ', ' '],
         ['G', ' ', ' ', ' ', ' ', ' ', ' '],
         ['V', ' ', ' ', ' ', ' ', ' ', ' '],
         ['X', ' ', ' ', ' ', ' ', ' ', ' ']]

while not is_table_filled(table):
    for i in range(1, 7):
        for j in range(1, 7):
            letter = get_random_letter(letters_and_numbers)
            table[i][j] = letter

write_table_in_file(table, 'table.csv')

print('Какую фразу хотите зашифровать?')
phrase = list(input())
indexes = list()

for i in phrase:
    index = find_index(table, i)
    if index:
        indexes += index

secret_word = "CYPHER"

new_table = list()

new_table.append(list(secret_word))

n = len(secret_word)
s = 0
while indexes:
    list_el = list()
    for i in range(n):
        if not indexes:
            break
        el = indexes.pop(0)
        list_el.append(el)
    new_table.append(list_el)

if len(new_table[-1]) < n:
    new_table[-1] += [''] * (n - len(new_table[-1]))

write_table_in_file(new_table, 'new_table.csv')

def transpose_table(table):
    transposed_table = transpose(table)
    transposed_table = map(lambda x: list(x), transposed_table)
    transposed_table = list(transposed_table)
    return transposed_table

transposed_new_table = transpose_table(new_table)

write_table_in_file(transposed_new_table, 'transposed_new_table.csv')

reshufled_transposed_new_table = list()

for i in range(len(secret_word)):
    reshufled_transposed_new_table.append(get_random_letter(transposed_new_table))

write_table_in_file(reshufled_transposed_new_table, 'reshufled_transposed_new_table.csv')

final_table = transpose_table(reshufled_transposed_new_table)

write_table_in_file(final_table, 'final_table.csv')

shifr = ''
for i in range(len(secret_word)):
    for j in range(1, len(reshufled_transposed_new_table[0])):
        shifr += reshufled_transposed_new_table[i][j]
print("Зашифрованная фраза:")
print(shifr)