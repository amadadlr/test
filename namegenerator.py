import random

stores= (
"Barneys New York",
"Bloomingdale's",
"Lord & Taylor",
"Saks Fifth Avenue",
"J. C. Penney",
"Kohl's",
"Macy's",
"Neiman Marcus",
"Bergdorf Goodman",
"Nordstrom",
"Sears",
"Big Lots",
"Costco",
"Dollar Tree",
"Family Dollar",
"HomeGoods",
"Kmart",
"Ross",
"Target",
"T.J. Maxx",
"Walmart",
"Sam's Club")

secure_random = random.SystemRandom()
print(secure_random.choice(stores))
