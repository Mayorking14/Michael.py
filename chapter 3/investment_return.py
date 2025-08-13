principal = 1000
rate = 0.07

print(f"year,  amount")

for year in range(1,30):
	first = (1 + rate) ** year
	amount = principal * (first)
	print(f"{year:>5},     {amount:>5}")

