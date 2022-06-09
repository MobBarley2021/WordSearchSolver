invalid_input = True
locations = {}

rows = input("What are the dimensions of the cross word puzzle? [rows]\n>>")
rows = int(rows.strip())


def cubify_puzzle(words: str, columns_number: int):
    puzzle = []
    while len(words) >= columns_number:
        puzzle.append(words[:columns_number])
        words = words[columns_number:]
    return puzzle


while invalid_input:
    letters = input("Type in the letters in your cross word puzzle!\n>>")
    if len(letters) / rows != rows:
        print(f"Your dimensions of row: {rows} and columns {rows} is wrong or\n" +
              " you put in the wrong amount of letters for your cross word puzzle!")
    else:
        invalid_input = False

invalid_input = True

while invalid_input:
    words = input("What are the words you want to find? Separate them with a comma.\n>>").replace(" ", "").split(",")
    verify = input("Are these the words you want? Type 'yes' for yes.\n>>")
    if verify == "yes":
        invalid_input = False

puzzle = cubify_puzzle(letters, rows)
for id, row in enumerate(puzzle):
    for word in words:
        if word in row:
            column = row.index(word) + 1
            locations[word] = [(column, id + 1), (column + len(word) - 1, id + 1)]

        elif word[::-1] in row:
            column = row.index(word[::-1]) + 1
            locations[word] = [(column + len(word) - 1, id + 1), (column, id + 1)]

i = 0
while i < rows:
    for word in words:
        columnWord = ""
        for row in puzzle:
            columnWord += row[i]

        if word in columnWord:
            column = columnWord.index(word) + 1
            locations[word] = [(column + len(word) - 1, i + 1), (column, i + 1)]

        if word[::-1] in columnWord:
            column = columnWord.index(word[::-1]) + 1
            locations[word] = [(column, i + 1), (column + len(word) - 1, i + 1)]

    sentence = ""
    side_sentence = ""
    loc = i
    row_num = 0
    while loc < rows and row_num < rows:
        sentence += puzzle[row_num][loc]
        side_sentence += puzzle[loc][row_num]

        row_num += 1
        loc += 1

    sentence_right = ""
    side_sentence_right = ""
    loc = rows - i - 1
    loc_alt = i
    row_num = 0
    row_num_alt = rows - 1
    while loc >= 0 and row_num < rows:
        sentence_right += puzzle[row_num][loc]
        side_sentence_right += puzzle[loc_alt][row_num_alt]

        row_num += 1
        row_num_alt -= 1
        loc_alt += 1
        loc -= 1

    for word in words:
        if word in sentence:
            row = sentence.index(word) + 1
            locations[word] = [(row + i, row), (i + len(word), row + len(word) - 1)]

        if word[::-1] in sentence:
            row = sentence.index(word[::-1]) + 1
            locations[word] = [(i + len(word), row + len(word) - 1), (row + i, row)]

        if word in sentence_right:
            row = sentence_right.index(word) + 1
            locations[word] = [(rows - i - row + 1, row), (rows - i - row - len(word) + 2, row + len(word) - 1)]

        if word[::-1] in sentence_right:
            row = sentence_right.index(word[::-1]) + 1
            locations[word] = [(rows - i - row - len(word) + 2, row + len(word) - 1), (rows - i - row + 1, row)]

        if word in side_sentence:
            row = side_sentence.index(word) + 1
            locations[word] = [(row, i + row), (row + len(word) - 1, i + row + len(word) - 1)]

        if word[::-1] in side_sentence:
            row = side_sentence.index(word[::-1]) + 1
            locations[word] = [(row + len(word) - 1, i + row + len(word) - 1), (row, i + row)]

        if word in side_sentence_right:
            row = side_sentence_right.index(word) + 1
            locations[word] = [(rows - row + 1, row + i), (rows - row - len(word) + 2, row + len(word) - 1 + i)]

        if word[::-1] in side_sentence_right:
            row = side_sentence_right.index(word[::-1]) + 1
            locations[word] = [(rows - row - len(word) + 2, row + len(word) - 1 + i), (rows - row + 1, row + i)]
    i += 1

print(locations)
