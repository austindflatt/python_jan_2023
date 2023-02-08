protein_strand = 'ACACGTGTCAGTTGTGCAGTACACGTACGTCAGTCAACTGTGACCAGTTGGTCAGTCAACCAACGTCAGTCAACTGACCACAGTGTCATGACACGTACGT'

# 1. How many times does the sequence ‘AGTC’ appear in the protein_strand?
print(protein_strand.count("AGTC"))

# 2. The sequence ‘CAACGTCA’ will split the strand when matched against its opposite
start = protein_strand.index("CAACGTCA")
end = start + len("CAACGTCA")
split_1 = protein_strand[:start]
split_2 = protein_strand[end:]
print(split_1, split_2)

# 3. Group all characters into groups of 4 and output how many times each sequence appears.
from collections import Counter
groups = [protein_strand[i:i+4] for i in range(0, len(protein_strand), 4)]
group_counts = Counter(groups)
print(group_counts)

# 4. Which group of 4 appears the most?
most_common_group = group_counts.most_common(1)[0][0]
print(f"The most common group of 4 is: {most_common_group}")
