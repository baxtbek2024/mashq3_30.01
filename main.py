
#1-masala
toplam1 = {1, 3, 7, 5, 3}
toplam2 = {2, 4, 5, 3, 2}
toplam3 = {5, 59, 0, 9, 8}
natija = set()

for i in toplam1:
    if i not in toplam2 and i not in toplam3:
        natija.add(i)

print(natija)

#2-masala
toplam1 = {12, 34 ,54, 11}
toplam2 = {9, 0, 5, 85, 9}


result = []

for x in toplam1:
    if x not in toplam2:
        result.append(x)

for x in toplam2:
    if x not in toplam1:
        result.append(x)

result.sort()
print(result)

#3-masala
lst = [1, 2, 2, 3, 4, 3, 5, 1]

seen = set()
duplicates = set()

for x in lst:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(duplicates)

