
# Simple Pairwise Sequence Alignment (Global – basic)

seq1 = "ATGCTAG"
seq2 = "ATGCG"

match = 1
mismatch = -1
gap = -2

score = 0
aligned1 = ""
aligned2 = ""

min_len = min(len(seq1), len(seq2))

for i in range(min_len):
    if seq1[i] == seq2[i]:
        score += match
    else:
        score += mismatch
    aligned1 += seq1[i]
    aligned2 += seq2[i]

# Gap penalty for remaining characters
score += gap * abs(len(seq1) - len(seq2))

print("Sequence 1:", aligned1)
print("Sequence 2:", aligned2)
print("Alignment Score:", score)

