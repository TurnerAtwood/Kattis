"""
/*  Turner Atwood
 *  9/19/2021
 *  Cafeteria (Easy) [4.2]: (https://open.kattis.com/problems/cafeteriaeasy)
 *  Ad-hoc - Plenty of index manipulation of arrays and computing ratios
 */
"""
PAT = [0,1,10,11]

def main():
    # Keep the food orders but group them by monster
    inp = [int(i) if i != "_" else -1 for i in (input() + " " + input()).split()]
    foods = [inp[2*j + PAT[i]] for j in range(5) for i in range(4)]
    
    # Just go until we've found all of the foods
    while foods.count(-1) > 0:
        # Get all of the ratios we can currently find from the plates
        ratios = find_all_ratios(foods)
    
        # Attempt to apply every ratio to every plate
        for rat in ratios:
            for mon in range(5):
                ind1, ind2 = 4*mon+rat[0], 4*mon+rat[1]
                foods[ind1], foods[ind2] = apply_ratio(ratios[rat], [foods[ind1], foods[ind2]])

    # Format array back into the provided format
    new_foods = [""]*20
    for i in range(5):
        for j in range(4):
            new_foods[PAT[j] + 2*i] = str(foods[4*i+j])
    foods = new_foods

    print(" ".join(foods[0:10]))
    print(" ".join(foods[10:20]))
    
def apply_ratio(ratio, foods):
    if foods.count(-1) != 1:
        pass
    elif foods[1] == -1:
        foods[1] = foods[0] * ratio[1] // ratio[0]
    else:
        foods[0] = foods[1] * ratio[0] // ratio[1]
    return foods


def find_all_ratios(foods):
    ratios = dict()
    for i in range(5):
        ratios.update( find_ratios(foods[4*i:4*(i+1)]) )
    return ratios

def find_ratios(p):
    found = dict()
    for f1 in range(4):
        for f2 in range(f1+1,4):
            if p[f1] != -1 and p[f2] != -1:
                g = gcd(p[f1], p[f2])
                found[(f1, f2)] = (p[f1] // g, p[f2] // g)
                
    return found

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

if __name__ == "__main__":
    main()
