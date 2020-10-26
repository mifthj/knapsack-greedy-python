import operator

print("Hari ini adalah hari panen! Ternyata jumlah buah yang panen melebihi ekspektasi Budi.. " )
print("Mari kita bantu Budi memilih buah yang memiliki profit tertinggi!")
n = int(input('Masukan jumlah total buah yang ada: '))
profits = list(map(int, input('Masukan profit dari tiap buah (Rp, dalam satuan ribu): ').split())) #10 = Rp 10.000,-
weights = list(map(int, input('Masukan berat dari tiap produk (kg): ').split()))
capacity = int(input('Masukan kapasitas maksimal tas (kg): '))

#buat list untuk table (profit, weight)
l = []
for i in range(n):
    l.append([profits[i], weights[i]])

#sorting
l = sorted(l, reverse = True, key = operator.itemgetter(1))

max_profits = 0
fractional_obj = 0

for i in range(n):
    if capacity > 0 and l[i][1] < capacity:
        capacity -= l[i][1]
        max_profits += l[i][0]
    else:
        fractional_obj = i
        break
if capacity > 0:
    max_profits += capacity*(l[fractional_obj][0]/(l[fractional_obj][1]))

print("Berarti total profit dari buah yang dapat Budi bawa dengan kapasitas tas 10 kg adalah.." + str(max_profits))