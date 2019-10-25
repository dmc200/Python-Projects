def ten_thousand_oneth_prime():
	primes = []
	for possiblePrime in range(2, 150000):
		isPrime=True
		for num in range(2, possiblePrime):
			if possiblePrime % num == 0:
				isPrime=False
				break
		if isPrime:
			primes.append(possiblePrime)
	return primes



prime_numbers = ten_thousand_oneth_prime()

print(len(prime_numbers))
print(prime_numbers[10001])
