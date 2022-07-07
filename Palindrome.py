# Pake string
def isPalindrome(x: int) -> bool:
	xs = str(x)
	nsx = xs[::-1]
	return xs == nsx

# print(isPalindrome(121))


# Tanpa di convert ke string
def isPalindrome(x: int) -> bool:
	if x < 0:
		return False

	reverse = 0
	num = x

	while num:
		lastdigit = num % 10 # 1
		reverse = reverse * 10 + lastdigit #1
		num = num // 10 #12

	hasil = reverse == x
	print(f"\nHasil = {reverse} || {x} -> {hasil}\n")

isPalindrome(int(input("Masukkan Angka: ")))
