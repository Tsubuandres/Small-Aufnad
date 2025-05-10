import phonefuncs
import phone_var as ph

# Your sentence variable
sentence = input("Input text:  ")

# Extracting words into a list
words = sentence.split()

for i in range(len(words)):

    #Convert to special characters
    words[i] = phonefuncs.normalize_text(words[i])

    #Split word into a list of characters
    word = list(words[i])

    #Remove non-letter characters
    # symbol_removed = False
    # if word[-1] in ph.non_letter_symbols:
    #     symbol = word.pop()
    #     symbol_removed = True

    # word = phonefuncs.schwa_after_glides(word)
    # word = phonefuncs.schwa_between_sonorants(word)
    # word = phonefuncs.schwa_before_n(word)
    # word = phonefuncs.schwa_after_sonorant_between_consonants(word)
    # word = phonefuncs.schwa_in_root(word)
    # word = phonefuncs.break_obstruent_clusters(word)
    # word = phonefuncs.schwa_after_initial_sonorant(word)
    # word = phonefuncs.schwa_before_final_nonnasal_sonorant(word)
    # word = phonefuncs.add_schwa_for_clitics(word)

    #Restore final symbol
    # if symbol_removed:
    #     word.append(symbol)

    #Rejoin the list of characters into a word
    words[i] = ''.join(word)

sentence = ' '.join(words)

# Display the list of words
#print(words)
print(sentence)
