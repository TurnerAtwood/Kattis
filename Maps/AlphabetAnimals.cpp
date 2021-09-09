/*  Turner Atwood
 *  7/6/2021
 *  Alphabet Animals [4.2]: (https://open.kattis.com/problems/alphabetanimals)
 *  Check beginnings of all words versus endings of valid options. Store with map for fast retrieval
 */

#include <iostream>
#include <stdio.h>
#include <unordered_set>
#include <unordered_map>
#include <vector>

using namespace std;

string alphabet_animals(void) { 
    string line;
    getline(cin, line);
    char start_char = line[line.size()-1];

    int n;
    getline(cin, line);
    n = stoi(line);

    // Keep track of all beginning characters and if they appear more than once
    unordered_map<char,int> all_begins;

    // Remember the valid choices to go through later once all_begins is filled
    vector<string> pot_words;

    for (int i = 0; i < n; i++) {
        getline(cin, line);
        if (all_begins.count(line[0] == 0))
            all_begins[line[0]] = 0;
        all_begins[line[0]] += 1;

        if (line[0] == start_char)
            pot_words.push_back(line);
    }

    // If we found no valid choices we are done
    if (pot_words.size() == 0)
        return "?";

    char first, last;
    for (const auto& word : pot_words) {
        first = word[0];
        last = word[word.size()-1];
        
        // If nothing begins with this end or if our end = begin and nothing ELSE begins with our end
        if ((all_begins.count(last) == 0) || (first == last && all_begins[last] == 1))
            return word+"!";
    }

    return pot_words[0];
}

int main() {
    printf("%s\n", alphabet_animals().c_str());
}

