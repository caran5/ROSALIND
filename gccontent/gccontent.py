from Bio import SeqIO

# create a dictionary 
sequences = {}
gc_content_dict = {}
current_id = ""

with open("gccontent/rosalind_gc.txt", "r") as file:
    for line in file: 
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            sequences[current_id] = ""
        else: 
            sequences[current_id] += line

for seq_id, dna in sequences.items():
    gc_count = 0
    overall_count = 0
    for base in dna: 
        if base == "G" or base == "C":
            gc_count += 1
            overall_count +=1
        else: 
            overall_count += 1
        gc_content = (gc_count / overall_count) * 100
        gc_content_dict[seq_id] = gc_content

gc_max_val = -1 
gc_max_key = None
for seq, gc in gc_content_dict.items():
    if gc > gc_max_val: 
        gc_max_val = gc
        gc_max_key = seq
print(gc_max_key)
print(gc_max_val)

