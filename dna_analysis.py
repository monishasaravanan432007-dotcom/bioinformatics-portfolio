dna = "ATGCGTACGTTAGC"

a = dna.count("A")
t = dna.count("T")
c = dna.count("C")
g = dna.count("G")

print("A:", a)
print("T:", t)
print("C:", c)
print("G:", g)

gc = (g + c) / len(dna) * 100
print("GC Content:", gc)

complement = dna.replace("A",
"t").replace("T", "a").replace("C",
"g").replace("G","c")
reverse_complement = complement[::-1].upper()
print("Reverse Complement:", reverse_complement)
