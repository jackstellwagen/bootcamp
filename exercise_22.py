import os
with open('data/salmonella_spi1_region.fna', 'r') as f:

    f_list = f.readlines()

f_list2 = f_list[1:]

for i, line in enumerate(f_list2):
    f_list2[i] = line[:-1]
f_str = ''.join(f_list2)

print(f_str)
