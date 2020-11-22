from collections import Counter


def repeatedDNASequences(s):

    sequences = (''.join(l) for l in zip(*[s[n:] for n in range(10)]))
    counts = Counter(sequences)
    duplicate_keys = (k for k, v in counts.items() if v > 1)
    return sorted(duplicate_keys)
    