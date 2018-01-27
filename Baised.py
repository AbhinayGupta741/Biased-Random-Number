import time,math
# add, multi, mod based on Linear Congruential Generator Algorithm
add = 1013904223
multi = 1664525
mod = math.pow(2,32)
c = time.time() # CPU Clock based randomness
def random_number(min_r,max_r):
	global c
	c = (add + c * multi) % mod
	return min_r + int((c / mod) * (max_r - min_r))
min_r = int(input('Enter Minimum Range'))
max_r = int(input('Enter Maximum Range'))
mid_r = (min_r + max_r) // 2
above = []
below = []
for i in range(73):
	above.append(random_number(mid_r + 1, max_r + 1))
for i in range(27):
	below.append(random_number(min_r, mid_r))

final_list = below + above


def main():
	random_pos = random_number(min_r , max_r)
	print(final_list[random_pos])

if __name__=='__main__':
	main()