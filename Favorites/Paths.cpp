/*	Turner Atwood
 *	8/28/2021 - 9/5/2021
 *	Paths [3.5] : (https://open.kattis.com/problems/paths)
 *	Build all color paths of length 2, 3, ... up to K
 **	Every vertex keeps track of how many paths it finds from attempting to combine
 **	its color with every found path of all of its neighbors.
 */

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

void fastscan(int&);
int get_left(int);
int get_right(int);
int add_left(int,int);
int add_right(int,int);
int path_length(int);
int path_reverse(int);
bool path_contains(int,int);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Input
    long path_count = 0;
    int i;
    int N,M,K;
    fastscan(N); fastscan(M); fastscan(K);

    int colors[N];
    // Every vertex has a map of the found paths that end in this vertex and their counts
    unordered_map<int,int> color_paths[N+1];
    vector<pair<int,int>> edges;
    for (i = 0; i < N; i++) {
        fastscan(colors[i]);
        color_paths[i][colors[i]] = 1; // Every vertex has one trivial path (itself) using its color
    }

    int first, second;
    for (i = 0; i < M; i++) {
        fastscan(first); first--;
        fastscan(second); second--;
        if (colors[first] != colors[second])
            edges.push_back(make_pair(first,second));
    }
    
    // Build all paths of length 2, 3, ... up to K
    int path_old, path_new;
    long path_count_new;
    for (int depth = 2; depth <= K; depth++) {
        for (i = 0; i < edges.size(); i++) {
            first = edges[i].first;
            second = edges[i].second;

            // Attach first to second's paths then vice versa
            for (int z = 0; z < 2; z++) {

                // Attempt to attach first's color to every path found ending in second
                for (auto& p_it: color_paths[second]) {
                    path_old = p_it.first;
                    path_count_new = p_it.second;
                    if (path_length(path_old) != depth-1 || path_contains(path_old, colors[first]))
                        continue;

                    // Ensure second's color is on the right
                    path_new = path_old;
                    if (get_right(path_new) != colors[second]) 
                        path_new = path_reverse(path_new);
                    if (get_right(path_new) != colors[second])
                        continue;
                    
                    path_new = add_right(path_new, colors[first]); 
                    if (get_right(path_new) < get_left(path_new))
                        path_new = path_reverse(path_new);

                    if (color_paths[first].count(path_new) == 0)
                        color_paths[first][path_new] = 0;
                    color_paths[first][path_new] += path_count_new;
                    path_count += path_count_new;
                }
                swap(first, second);
            }
        }
    }

    printf("%ld \n", path_count);
}

int get_left(int path) {
    while (path > 10)
        path = path / 10;
    return path;
}

int get_right(int path) {
    return path%10;
}

int add_left(int old_path, int new_color) {
    int base = 10;
    while (base < old_path)
        base *= 10;
    return (new_color*base + old_path);
}

int add_right(int old_path, int new_color) {
    return old_path*10 + new_color;   
}

int path_length(int path) {
    int size = 1;
    int base = 10;
    while (base < path) {
        base *= 10;
        size++;
    }
    return size;
}

int path_reverse(int path) {
    int new_path = 0;
    while (path) {
        new_path = new_path*10 + path%10;
        path /= 10;
    }
    return new_path;
}

bool path_contains(int path, int target) {
    while (path > 0) {
        if ((path % 10) == target)
            return true;
        path /= 10;
    }
    return false;
}

void fastscan(int &number)
{
    //variable to indicate sign of input number
    bool negative = false;
    int c;
  
    number = 0;
  
    // extract current character from buffer
    c = getchar();
    if (c=='-')
    {
        // number is negative
        negative = true;
  
        // extract the next character from the buffer
        c = getchar();
    }
  
    // Keep on extracting characters if they are integers
    // i.e ASCII Value lies from '0'(48) to '9' (57)
    for (; (c>47 && c<58); c=getchar())
        number = number *10 + c - 48;
  
    // if scanned input has a negative sign, negate the
    // value of the input number
    if (negative)
        number *= -1;
}

