/*	Turner Atwood
 *	10/29/19
 *	Running MoM [4.0] https://open.kattis.com/problems/runningmom
 *	DFS to determine all nodes in cycles, then
 **	DFS for each query to see if it can reach a cycle
 */

// Find all cities inside cycles

#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	unordered_map<string,unordered_set<string> > cities;
	for (int i = 0; i < n; i++) {
		string cityA,cityB;
		cin >> cityA >> cityB;
		if (!cities.count(cityA)) {
			cities[cityA] = unordered_set<string>();
		}
		if (!cities.count(cityB)) {
			cities[cityB] = unordered_set<string>();
		}
		cities[cityA].insert(cityB);
	}

	unordered_set<string> cycles;
	unordered_set<string> notCycles;

	// We will put every city in one of the cycle buckets
	for (unordered_map<string,unordered_set<string> >::iterator it = cities.begin(); it != cities.end(); it++) {
		string startCity = it->first;
		//cout << "Looking at: " << startCity << endl;
		if (cycles.count(startCity) || notCycles.count(startCity)) {
			continue;
		}
		unordered_map<string,string> visited;
		visited[startCity] = "";

		// DFS to find if startCity is part of a cycle
		bool found = false;
		vector<string> stack;
		stack.push_back(startCity);
		string currentCity;
		while (stack.size() && !found) {
			currentCity = stack[stack.size()-1];
			//cout << "\t" << currentCity << "\n";
			stack.pop_back();
			unordered_set<string> currentNeighbors = cities[currentCity];
			for (unordered_set<string>::iterator neigh = currentNeighbors.begin(); neigh != currentNeighbors.end(); neigh++) {
				//cout << "\t\t" << *neigh << endl;
				if (*neigh == startCity) {
					found = true;
					break;
				}

				if (visited.count(*neigh)) {
					continue;
				}

				visited[*neigh] = currentCity;
				stack.push_back(*neigh);
			}
		}

		// Add every part of the found cycle to the cycles set
		if (found) {
			while (currentCity != startCity) {
				cycles.insert(currentCity);
				currentCity = visited[currentCity];
			}
			cycles.insert(startCity);
		}
		// Maybe do more if this is too slow
		else {
			notCycles.insert(startCity);
		}
	}

	// Now we check queried cities to see if they can reach any cycle
	unordered_set<string> reachCycles;
	for (unordered_set<string>::iterator it = cycles.begin(); it != cycles.end(); it++) {
		reachCycles.insert(*it);
	}
	unordered_set<string> notReachCycles;
	string target;
	getline(cin, target);
	while (getline(cin, target)) {
		if (reachCycles.count(target)) {
			cout << target << " safe\n";
			continue;
		}

		// Another DFS
		unordered_map<string,string> visited;
		visited[target] = "";
		bool found = false;
		vector<string> stack;
		stack.push_back(target);
		string currentCity;
		while (stack.size() && !found) {
			currentCity = stack[stack.size()-1];
			stack.pop_back();
			unordered_set<string> currentNeighbors = cities[currentCity];
			for (unordered_set<string>::iterator neigh = currentNeighbors.begin(); neigh != currentNeighbors.end(); neigh++) {
				if (reachCycles.count(*neigh)) {
					found = true;
					break;
				}

				if (visited.count(*neigh)) {
					continue;
				}

				visited[*neigh] = currentCity;
				stack.push_back(*neigh);
			}

		}
		// If found, trace the path back to add to reachCycle
		if (found) {
			while(currentCity != target) {
				reachCycles.insert(currentCity);
				currentCity = visited[currentCity];
			}
			reachCycles.insert(target);
			
		}

		if (reachCycles.count(target)) {
			cout << target << " safe\n";
		}
		else {
			cout << target << " trapped\n";
		}
	}
}