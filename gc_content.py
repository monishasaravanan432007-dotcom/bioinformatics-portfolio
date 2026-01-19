def gc_content(sequence):
    sequence = sequence.upper()
    g = sequence.count("G")
    c = sequence.count("C")
    total = len(sequence)
    if total == 0:
        return 0
    return ((g + c) / total) * 100

seq = input("Enter DNA sequence: ")
gc = gc_content(seq)
print("GC Content: {:.2f}%".format(gc))
