def prime_sieve():
D = {}
q = 2
while True:
    if q not in D:
	yield q
	D[q * q] = [q]
    else:
	for p in D[q]:
            D.setdefault(p+q, []).append(p)
        del D[q]
    q += 1

def binarySearch(input, target):
	if not input or not target:
		return False
	first = 0
	last = len(input) - 1
	found = False
	while (first <= last) and not found:
		midpoint = (first + last) // 2
		if last == first:
			return False
		if input[midpoint] < target:
			first = midpoint + 1
			continue
		if input[midpoint] > target:
			last = midpoint
			continue
		else: 
			found = True
		return found

def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

def is_prime(primeList, n):
	return binarySearch(primeList, n)

def primePair(primeList, z)
for i in primeList:
	a = z - i
	if is_Prime(primeList, a):
		return i, a
	else: 
		continue
else:
	print "Goldbach's conjecture disproved"
	print z
	return False

def tic():
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    else:
        print "Toc: start time not set"

evenList = filter(even, range(4, 10**7))

primeList = []

i = 0

tic()
for primeNumber in prime_sieve():
	if i <= 664579:
		primeList.append(primeNumber)
	else:
		break
	i += 1

for q in evenList:
	i, a = primePair(primeList, q)
	print("even number: q with prime integers %i and %a" % q, i, a)
toc()