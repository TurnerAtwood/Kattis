x = int(input())
y = int(input())
if x > 0 and y > 0: quad = 1
if x < 0 and y > 0: quad = 2
if x < 0 and y < 0: quad = 3
if x > 0 and y < 0: quad = 4
print(quad)