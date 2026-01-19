seq1 = input("Enter Sequence 1: ").upper()
seq2 = input("Enter Sequence 2: ").upper()

score = 0

for a, b in zip(seq1, seq2):
    if a == b:
        score += 1
    else:
        score -= 1

print("Sequence 1:", seq1)
print("Sequence 2:", seq2)
print("Alignment Score:", score)
