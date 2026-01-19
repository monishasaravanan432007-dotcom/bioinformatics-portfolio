def read_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        name = None
        seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name:
                    sequences[name] = seq
                name = line[1:]
                seq = ""
            else:
                seq += line
        if name:
            sequences[name] = seq
    return sequences

file_path = "sample.fasta"
seqs = read_fasta(file_path)

for name, seq in seqs.items():
    print(f"{name}: {seq}")
