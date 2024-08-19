def word_lenght(word):
    return len(word)

vegies = ["patato","onion","beans","pumpkin"]
lenghts = map(word_lenght,vegies)

lenght_list = list(lenghts)
print(lenght_list)