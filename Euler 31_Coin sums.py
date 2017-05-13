# In England the currency is made up of pound, $, and pence, p, and
# there are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
#
# It is possible to make 2 in the following way:
#
#     1x$1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can $2 be made using any number of coins?

target_value = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
unique_ways = [1] + [0] * target_value
print unique_ways
for coin in coins:
    for i in range(coin, target_value + 1):
        unique_ways[i] += unique_ways[i - coin]
print unique_ways[target_value]
# SOLVED
