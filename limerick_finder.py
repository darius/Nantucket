import poetry


tokens = poetry.tokenize("proust-swann.txt")


def not_limerick(syllable_counter, current_sylct):  # return true if the word would overflow the line
    if syllable_counter < 8 and current_sylct > 8 - syllable_counter:
        return True
    elif syllable_counter < 16 and current_sylct > 16 - syllable_counter:
        return True
    elif syllable_counter < 21 and current_sylct > 21 - syllable_counter:
        return True
    elif syllable_counter < 26 and current_sylct > 26 - syllable_counter:
        return True
    elif syllable_counter < 35 and current_sylct > 35 - syllable_counter:
        return True
    return False


limericks = []
word_arrays = []
syllable_counters = []
phoneme_arrays = []
i = 0
while i < len(tokens):
    start_word = tokens[i]
    word_arrays.append([start_word])  # Holds the actual words of the potential limerick
    syllable_counters.append(poetry.nsyl(start_word))
    n = i + 1
    give_up = False
    rhyme_scheme = {}  # Tracks the rhyme scheme
    if syllable_counters[i]:
        while n < len(tokens):
            sylct = poetry.nsyl(tokens[n])
            if sylct == False or not_limerick(syllable_counters[i], sylct): break  # break out if a word overflows the line
            word_arrays[i].append(tokens[n])
            syllable_counters[i] += sylct
            phonemes = poetry.phonemes(tokens[n])
            if syllable_counters[i] == 8:
                rhyme_scheme['A'] = phonemes
                word_arrays[i].append("\n")
            elif syllable_counters[i] == 16:
                word_arrays[i].append("\n")
                if not poetry.rhyme_from_phonemes(rhyme_scheme['A'], phonemes): break
            elif syllable_counters[i] == 21:
                rhyme_scheme['B'] = phonemes
                word_arrays[i].append("\n")
            elif syllable_counters[i] == 26:
                word_arrays[i].append("\n")
                if not poetry.rhyme_from_phonemes(rhyme_scheme['B'], phonemes): break
            elif syllable_counters[i] == 35:
                if poetry.rhyme_from_phonemes(rhyme_scheme['A'], phonemes):
                    limericks.append(word_arrays[i])
                break
            n += 1
    i += 1

if limericks == []: print "Sorry, there were no limericks found in your text!"

for limerick in limericks:
    limerick = " ".join(limerick)
    print limerick