##with # na otvorenie suboru >> zabezpeci ze sa subor zavrie



file_name = 'words.txt'

with open(file_name) as fd:

    #text2 = fd.read()
    # print(text2)

    # text = fd.readlines()
    # print(text)
    # print(repr(text))
    # words = text.split('\n')
    # print(words)

### NOT DONE
    # rows = fd.readlines()
    # print(rows)

    # cleaned = []

    # for row in rows:
    #     cleaned.append(row.rstrip())

    

    word = []

    for row in fd:
        word.append(row.rstrip())

    print(word)