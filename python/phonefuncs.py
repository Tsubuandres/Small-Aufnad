import phone_var as ph

def normalize_text(word) :
    characters = "CDKLPTLMNRZ"
    #ĊċḲḳĻļṖṗṬṭ

    normalized_word = ""

    for letter in word:
        normalized_letter = letter
        if letter in characters:
            match letter:
                case "C":
                    normalized_letter = "ċ"
            match letter:
                case "K":
                    normalized_letter = "ḳ"
            match letter:
                case "L":
                    normalized_letter = "ḷ"
            match letter:
                case "P":
                    normalized_letter = "ṗ"
            match letter:
                case "T":
                    normalized_letter = "ṭ"
            match letter:
                case "D":
                    normalized_letter = "þ"
            match letter:
                case "M":
                    normalized_letter = "ṁ"
            match letter:
                case "N":
                    normalized_letter = "ṅ"
            match letter:
                case "R":
                    normalized_letter = "ṙ"
            match letter:
                case "Z":
                    normalized_letter = "ļ"
        
        normalized_word += normalized_letter

    return normalized_word

def schwa_after_glides(word):

    #Account for the fact that adding a schwa increased list length
    for i in range(len(word) + word.count('y') + word.count('w')):
        char = word[i]

        if char in "yw":
            word.insert(i+1, "ə")
            i -= 1
    
    return word

def schwa_between_sonorants(word):
    i = 0
    while i < (len(word) - 1):
        #Check in non-glide sonorants appear together
        if word[i] in ph.non_glide_sonorant and word[i + 1] in ph.non_glide_sonorant:
            word.insert(i+1, "ə")
        i += 1
    
    return word

def schwa_before_n(word):
    i = 0
    #Do not include last character
    while i < (len(word) - 1):
        #Check if non-initial "n"
        if i > 0 and word[i] in "Nn":
            #Check the sorrounding phonemes
            if word[i-1] != "ə" and word[i+1] != "ə":
                word.insert(i, "ə")
        i += 1
    
    return word

def schwa_after_sonorant_between_consonants(word):
    i = 0
    #Do not include last character
    while i < (len(word) - 1):
        #Check if non-initial sonorant
        if i > 0 and word[i] in ph.non_glide_sonorant:
            #Check the sorrounding phonemes
            if word[i-1] != "ə" and word[i+1] != "ə":
                word.insert(i+1, "ə")
        i += 1
    
    return word

def schwa_in_root(word):
    i = 0
    cluster_length = 0
    obstruent_found = False
    num_of_obstruents = 0

    #Find number of obstruents in word
    for char in word:
        if char in ph.obstruents:
            num_of_obstruents += 1
    
    #Apply rule on for content words (which have more than one obstruent)
    if num_of_obstruents > 1:
        while i < (len(word)):
            # When the first obstruent is found
            if word[i] in ph.obstruents and not obstruent_found:
                first_obstruent_index = i
                obstruent_found = True
            # Cluster length increases for each obstruent found
            if word[i] in ph.obstruents and obstruent_found:
                cluster_length += 1
            
            #When the obstruent cluster ends
            if obstruent_found and (not (word[i] in ph.obstruents) or i == len(word) - 1):
                cluster_odd = True if cluster_length % 2 != 0 else False
                #Adjust index so that the onset_lenght is one more that coda_lenth. 
                schwa_index = cluster_length/2 + first_obstruent_index
                schwa_index = int(schwa_index + 0.5) if cluster_odd else int(schwa_index + 0)

                break
            
            i += 1
    if obstruent_found: 
        word.insert(schwa_index, "ə")

    return word

def break_obstruent_clusters(word):
    i = 0

    #Deal with fricative and plosive clusters
    while i < (len(word)):

        #Check for plosive clusters of 3 or more phonemes
        if word[i] in ph.plosives and i < len(word) - 2:
            if word[i+1] in ph.plosives:
                if word[i+2] in ph.plosives:
                    word.insert(i+2, "ə")
                    i += 1
                    continue
        #Check for fricative clusters of 3 or more phonemes
        elif word[i] in ph.fricatives and i < len(word) - 2:
            if word[i+1] in ph.fricatives:
                if word[i+2] in ph.fricatives:
                    word.insert(i+2, "ə")
                    i += 1
                    continue
        else:
            i += 1
            continue
        
        i += 1
    
    #Deal with obstruent clusters of 4 or more phonemes
    i = 0
    while i < (len(word)):
        if word[i] in ph.obstruents and i < len(word) - 3:
            if word[i+1] in ph.obstruents:
                if word[i+2] in ph.obstruents:
                    if word[i+3] in ph.obstruents:
                        word.insert(i+3, "ə")
                        i += 1
                    continue
        i += 1

    return word

def schwa_after_initial_sonorant(word):
    if word[0] in ph.non_glide_sonorant and word[1] != "ə":
        word.insert(1, "ə")
    return word

def schwa_before_final_nonnasal_sonorant(word):
    if word[-1] in ph.non_nasal_sonorant and word[-2] != "ə":
        word.insert(-1, "ə")
    return word

def add_schwa_for_clitics(word):
    if len(word) == 1:
        word.append("ə")
    return word


            




