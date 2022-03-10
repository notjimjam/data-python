open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     print(line)

# for line in open_file:
#     string = line.split(',')
#     print(string[2])

# for line in open_file:
#     string = line.split(',')
#     v1 = int(string[3])
#     v2 = float(string[4])

#     print(v1*v2)

total = 0

for line in open_file:
    string = line.split(',')
    v1 = int(string[3])
    v2 = float(string[4])

    total = total + (v1*v2)

print(total)

open_file.close()

    