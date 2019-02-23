from collections import defaultdict, deque
import sys
from copy import deepcopy


'''
Determines whether a given sequence of words is a word ladder
from a given word word_1 to a given word word_2, that is,
a sequence of words all in the provided dictionary, of minimal length,
starting with word_1, ending in word_2, and such that two consecutive words
in the sequence differ by exactly one letter.

Assume that word_1 and word_2 are sequences of uppercase letters.

Note that a single test will examine many potential sequences at once,
so no form of hardcoding will achieve anything...

Hint to make the solution efficient enough:
- Check whether the given sequence can be a word ladder because:
   . its first word is word_1;
   . its last word is word_2;
   . any pair of consecutive words are in the dictionary and differ by exactly one letter.
- Then compute the length of some word ladder between word_1 and word_2, if any,
  giving up in case it can no longer be at most equal to the length of the given sequence,
  and check whether it is equal to the length of the given sequence.
'''


dictionary_file = 'dictionary.txt'

def get_words_and_word_relationships():
    try:
        with open(dictionary_file) as dictionary:
            lexicon = set()
            contextual_slots = defaultdict(list)
            for word in dictionary:
                word = word.rstrip()
                lexicon.add(word)
                for i in range(len(word)):
                    contextual_slots[word[: i], word[i + 1: ]].append(word)
            closest_words = defaultdict(set)
            for slot in contextual_slots:
                for i in range(len(contextual_slots[slot])):
                    for j in range(i + 1, len(contextual_slots[slot])):
                        closest_words[contextual_slots[slot][i]].add(contextual_slots[slot][j])
                        closest_words[contextual_slots[slot][j]].add(contextual_slots[slot][i])
            return lexicon, closest_words
    except FileNotFoundError:
        print(f'Could not open {dictionary_file}. Giving up...')
        sys.exit()

    
def is_word_word_ladder(word_1, word_2, candidate_ladder):
    '''
    >>> is_word_word_ladder('AAA', 'AAA', ['AAA'])
    False
    >>> is_word_word_ladder('DAY', 'MEW', ['DAY', 'DAW', 'DEW', 'MEW'])
    False
    >>> is_word_word_ladder('COLD', 'WARM', ['COLD', 'CALD', 'CARD', 'WARD', 'WARM'])
    False
    >>> is_word_word_ladder('COLD', 'WARM', ['COLD', 'CORD', 'WORD', 'WARD', 'WARP', 'WARM'])
    False
    >>> is_word_word_ladder('TABLE', 'TABLE', ['TABLE'])
    True
    >>> is_word_word_ladder('DAY', 'MEW', ['DAY', 'HAY', 'HEY', 'HEW', 'MEW'])    
    True
    >>> is_word_word_ladder('COLD', 'WARM', ['COLD', 'CORD', 'WORD', 'WARD', 'WARM'])
    True
    '''
    # Note how get_words_and_word_relationships() is called below.
    # Insert your code here
    if word_1 in lexicon and word_2 in lexicon and candidate_ladder[0] == word_1 and candidate_ladder[-1] == word_2:
    #     current = word_1
    #     for i in candidate_ladder[1:]:
    #         if i not in closest_words[current]:
    #             return False
    #         if i != word_2 and word_2 in closest_words[current]:
    #             return False
    #         current = i
    # else:
    #     return False
    # return True
        if word_1 == word_2:
#            [word_1] = candidate_ladder
            return [word_1] == candidate_ladder    # if candidate_ladder == [word_1]  return TRUE, verse vice
        found = False
        answer = []
        run = True
        result = [[word_1]]
        current_length = 0
        while run:
            head = result[0]        #  head = [word_1]
            result = result[1:]      #    result = []
            closest = closest_words['MEW']
            print(closest)
            closest = closest_words[head[-1]]
            print(head)
#            print(closest)
            for i in closest:
                new_list = deepcopy(head)    #  indepent copy [word_1]
                new_list.append(i)
                if i == word_2:
                    if not found:
                        current_length = len(new_list)
                        found = True
                        answer.append(new_list)
                    if found and len(new_list) == current_length:
                        answer.append(new_list)
                if found and len(new_list) > current_length:
                    run = False
                    break
                result.append(new_list)
                # print(new_list)
        # print(answer)
        return candidate_ladder in answer
    return False
lexicon, closest_words = get_words_and_word_relationships()

is_word_word_ladder('DAY', 'MEW', ['DAY', 'HAY', 'HEY', 'HEW', 'MEW'])
#print(get_words_and_word_relationships())
# if __name__ == '__main__':
# #     # lexicon is a set that records all words in the dictionary.
# #     # closest_words is a dictionary that maps any word w in the dictionary
# #     # to the set of all words that differ from w by exactly one letter.
#     lexicon, closest_words = get_words_and_word_relationships()
#     import doctest
#     doctest.testmod()
