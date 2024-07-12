# Uses progressbar2 module - pip install or refactor to remove dependency

from progressbar import progressbar

RUDE_WORD_FILES = ["data/rude_a.txt", "data/rude_b.txt", "data/rude_c.txt"]
FULL_WORD_FILES = ["data/words_alpha.txt"]
OUTPUT_FILE = "clean_words.txt"
REMOVE_IF_IN = False
REMOVE_IF_STARTS_WITH = True


def words_from_files(file_list, single_words=True):
    # load word file, assumes simple text file with no quotes, option to remove multi-word phases
    words = []
    for file in file_list:
        with open(file) as f:
            words.extend(f.read().splitlines())    

    # make unique, sort
    words = list(set(words))

    if single_words:
        words = [word for word in words if " " not in str(word)] 

    return words

all_words = words_from_files(FULL_WORD_FILES)
rude_words = words_from_files(RUDE_WORD_FILES)

# Get word files not in rude word set
clean_words = list(set(all_words) - set(rude_words))

# Further processing...
if REMOVE_IF_STARTS_WITH and not REMOVE_IF_IN:
    print("Removing words that start with rude words.  Iterating through {} words...".format(len(rude_words)))
    for rude_word in progressbar(rude_words):
        clean_words = [word for word in clean_words if not str(word).startswith(str(rude_word))]
elif REMOVE_IF_IN:
    print("Removing words that contain rude words.  Iterating through {} words...".format(len(rude_words)))
    for rude_word in progressbar(rude_words):        
        clean_words = [word for word in clean_words if str(rude_word) not in str(word)]

clean_words.sort()

print("Got {} clean words.  First words: {}.  Writing to file: {}".format(len(clean_words), clean_words[:10], OUTPUT_FILE))

# write output file
with open(OUTPUT_FILE, 'w') as f:
    for line in clean_words:
        f.write(f"{line}\n")
