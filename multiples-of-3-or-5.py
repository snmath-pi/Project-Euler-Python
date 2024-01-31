# this way is O(1000)
total_sum = 0
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print(total_sum)


# this is O(1) using math (AP)
val1 = 999//3 * (3 + 999) // 2
val2 = 999//5 * (5 + 995) // 2
val3 = 999//15 * (30 + (999//15-1) * 15) // 2

print(val1 + val2 - val3)