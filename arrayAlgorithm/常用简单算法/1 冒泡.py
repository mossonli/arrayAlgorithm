"""

"""

li = [4, 3, 5, 9, 6, 8, 1]
l = len(li)
for i in range(l):
    for j in range(i + 1, l):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]
print(li)
