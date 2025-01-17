
total_chars = 0
words = ['sky', 'war', 'Water', 'coin', 'forest']


####### popcet znakov v touple #################################################
for i in words:
    ##pass ## pouziva sa ked loop nie je dokonceny, nevyhodi chybu
    total_chars = total_chars + len(i)


print(total_chars)


####### pocet znakov len slov zacinajucich na w ###################################
for i in words:

    if i.startswith('w'):
        total_chars = total_chars + len(i)


print(total_chars)


####### pocet znakov len slov zacinajucich na w w ###################################
for i in words:

    if i.startswith(('w', 'W') ):
        total_chars = total_chars + len(i)


print(total_chars)



####### pocet znakov len slov ktore maju 3 znaky ###################################
for i in words:

    if len(i) == 3:
        total_chars = total_chars + len(i)


print(total_chars)
