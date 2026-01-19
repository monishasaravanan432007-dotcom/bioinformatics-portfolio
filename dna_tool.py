dna = input("Enter DNA sequence: ").upper()

a = dna.count("A")
t = dna.count("T")
c = dna.count("C")
g = dna.count("G")

gc_content = ((g + c) / len(dna)) * 100

complement = dna.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
reverse_complement = complement[::-1].upper()

print("\nBase Count")
print("A:", a)
print("T:", t)
print("C:", c)
print("G:", g)

print("\nGC Content:", round(gc_content, 2), "%")
print("Reverse Complement:", reverse_complement)
