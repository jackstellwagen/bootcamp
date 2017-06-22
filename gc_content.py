#seq = open('data/salmonella_spi1_region.fna')
#seq = 'ATACGTAGCTGCTAGCTGCTGATGCATGTCAG'
block_size = 500

import os
with open('data/salmonella_spi1_region.fna', 'r') as f:

    f_list = f.readlines()

f_list2 = f_list[1:]

for i, line in enumerate(f_list2):
    f_list2[i] = line[:-1]
f_str = ''.join(f_list2)

seq = f_str
#print(f_str)


def gc_blocks(seq, block_size):
    #establishing list
    my_list = []
    for n in range(0, len(seq)//block_size):
        block_n = seq[n*block_size: (n+1)* block_size-1]
        #count g' and c's
        n_gc = block_n.count('G') + block_n.count('C')
        #divide for g,c content
        gc_content = n_gc/block_size
        #add each gc content to my list
        my_list.append(gc_content)
        #establish my list and make it a tuple
    return tuple(my_list)


my_list = gc_blocks(seq,block_size)
print (my_list)
