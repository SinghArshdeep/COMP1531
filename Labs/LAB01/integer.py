integers = [1, 2, 3, 4, 5]
integers.append(6)
tot = 0
for i in range(len(integers)):
    tot = tot + integers[i]
print(tot)

print(sum(integers))
