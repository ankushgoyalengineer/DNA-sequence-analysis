from Bio.Seq import Seq

# DNA sequence (Example: Add your sequence here)
dna_sequence = Seq("ATGCGTACGTAGCTAGCTAGCGTAGCTGACTGATCGTACGTTAGCTAGCTAGCTAGTAG")

# Calculate GC content
def calculate_gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

# Transcribe DNA to RNA
rna_sequence = dna_sequence.transcribe()

# Translate RNA to protein
protein_sequence = rna_sequence.translate()

# Print results
print(f"DNA Sequence: {dna_sequence}")
print(f"GC Content: {calculate_gc_content(dna_sequence):.2f}%")
print(f"RNA Sequence: {rna_sequence}")
print(f"Protein Sequence: {protein_sequence}")
