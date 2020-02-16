"""
/*	Turner Atwood
 *	11/20/19
 *	4Thought [2.8] https://open.kattis.com/problems/4thought
 *	Use a map to save the generated vals and their expression
 */
"""

OPS = ["+","-","*","//"]

# Iterator to generate all permutations with replacement
# This is the same functionality as itertools.product
class product:
	def __init__(self, v, n):
		self.vals = v
		self.size = len(v)
		self.n = n
		self.total = int(self.size**(n))
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		self.index += 1
		if self.index >= self.total:
			raise StopIteration
		res = []
		power = 1
		for i in range(self.n):
			res.append(self.vals[(self.index//power)%self.size])
			power *= self.size
		return res

# Use eval to compute the result then save that in a dictionary
def gen_all():
	result = dict()
	for ops in product(OPS,3):
		expr = ['4',ops[0],'4',ops[1],'4',ops[2],'4']
		val = eval("".join(expr))
		
		expr = ["/" if i=="//" else i for i in expr]
		expr.append("=")
		expr.append(str(val))
		expr = " ".join(expr)
		result[int(val)] = expr
	return result

# Generate all possible values up front
def main():
	possibles = gen_all()

	m = int(input())
	for i in range(m):
		q = int(input())
		if q in possibles:
			print(possibles[q])
		else:
			print("no solution")

if __name__ == "__main__":
	main()