"""
/*  Turner Atwood
 *  10/25/2020
 *  Coversation Log [2.7] open.kattis.com/problems/coversationlog
 *  Use maps to count how many times each person has a word.
 ** Find the intersection of all of the words and sort based on counts.
 */
"""

from sys import stdin

def main():
    M = int(stdin.readline())

    people_words = dict()
    for i in range(M):
        line = stdin.readline().split()
        name = line[0]
        cur_words = line[1:]

        if name not in people_words:
            people_words[name] = dict()
        word_counts = people_words[name]

        for word in cur_words:
            if not word in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1

    common_words = dict()
    first = True

    for name in people_words:
        cur_words = people_words[name]

        if first:
            common_words = cur_words
            first = False
            continue

        for word in list(common_words):
            if word in cur_words:
                common_words[word] += cur_words[word]
            else:
                del common_words[word]

    # Sort the common words
    words = [(-1*common_words[word], word) for word in common_words]

    out = [word for count,word in sorted(words)]
    if out:
        print("\n".join(out))
    else:
        print("ALL CLEAR")

if __name__ == "__main__":
    main()

