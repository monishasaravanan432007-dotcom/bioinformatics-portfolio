# Smith-Waterman Local Alignment (Simple Version)

def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-1):
    m, n = len(seq1), len(seq2)
    # Create score matrix
    score = [[0] * (n + 1) for _ in range(m + 1)]

    max_score = 0
    max_pos = (0, 0)

    # Fill score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diag = score[i - 1][j - 1] + match
            else:
                diag = score[i - 1][j - 1] + mismatch

            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            score[i][j] = max(0, diag, up, left)

            if score[i][j] > max_score:
                max_score = score[i][j]
                max_pos = (i, j)

    # Traceback
    aligned1, aligned2 = "", ""
    i, j = max_pos

    while score[i][j] != 0:
        current = score[i][j]
        diag = score[i - 1][j - 1]
        up = score[i - 1][j]
        left = score[i][j - 1]

        if current == diag + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            aligned1 = seq1[i - 1] + aligned1
            aligned2 = seq2[j - 1] + aligned2
            i -= 1
            j -= 1
        elif current == up + gap:
            aligned1 = seq1[i - 1] + aligned1
            aligned2 = "-" + aligned2
            i -= 1
        else:
            aligned1 = "-" + aligned1
            aligned2 = seq2[j - 1] + aligned2
            j -= 1

    return aligned1, aligned2, max_score

seq1 = "GATTACA"
seq2 = "GCATGCU"

a1, a2, score = smith_waterman(seq1, seq2)
print("Aligned 1:", a1)
print("Aligned 2:", a2)
print("Score   :", score)
