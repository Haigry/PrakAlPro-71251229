# =============================================
# Fungsi Fibonacci dengan Rekursif + Memoization
# Lebih optimal: O(n) vs O(2^n) tanpa memo
# =============================================
memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 0:
        hasil = 0
    elif n == 1:
        hasil = 1
    else:
        hasil = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = hasil
    return hasil

# Menampilkan deret Fibonacci
n = int(input("\nMasukkan jumlah suku Fibonacci: "))
print(f"Deret Fibonacci ({n} suku):")
for i in range(n):
    print(fibonacci(i), end=" ")
print()
