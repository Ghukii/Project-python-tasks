from random import randint
import csv
from numpy import transpose

def is_table_filled(table):
    for i in  range(1, 7):
        for j in range(1, 7):
            if table[i][j] == ' ':
                return False
    return True

def get_random_letter(letters_and_numbers):
    n = randint(0, len(letters_and_numbers) - 1)

    n = letters_and_numbers.pop(n)
    return n

def write_table_in_file(table, filename):
    t = list()
    for i in table:
        t.append(i)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        while t:
            writer.writerow(t.pop(0))
    csvfile.close()

def find_index(table, letter):
    if letter == ' ':
        return []
    for i in range(1, 7):
        for j in range(1, 7):
            if table[i][j] == letter.upper():
                return [table[i][0], table[0][j]]