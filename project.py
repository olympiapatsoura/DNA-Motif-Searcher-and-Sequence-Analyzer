import sys


def main():
    print("=== DNA Sequence Analyzer & Motif Searcher ===")

    # Prompt user for the target DNA sequence
    dna = input("Enter DNA sequence: ").strip().upper()
    if not validate_dna(dna):
        print("Error: Invalid DNA sequence! Sequence must contain only A, C, G, T.")
        sys.exit(1)

    # Prompt user for the target motif sequence
    motif = input("Enter motif sequence to search: ").strip().upper()
    if not validate_dna(motif):
        print("Error: Invalid motif sequence! Sequence must contain only A, C, G, T.")
        sys.exit(1)

    # Perform calculations and search operations
    positions = find_motif(dna, motif)
    gc = gc_content(dna)
    rna = transcribe(dna)

    # Output analysis results to the console
    print("\n--- Results ---")
    print(f"DNA Length: {len(dna)} bp")
    print(f"GC Content: {gc:.2f}%")
    print(f"RNA Transcribe: {rna}")
    if positions:
        print(f"Motif '{motif}' found at positions (1-indexed): {positions}")
    else:
        print(f"Motif '{motif}' not found in the sequence.")


def validate_dna(sequence):
    # Checks if sequence contains only valid DNA bases (A, C, G, T)
    if not sequence:
        return False

    # Check if all unique characters in the sequence are valid DNA bases
    return set(sequence.upper()).issubset({'A', 'C', 'G', 'T'})


def find_motif(dna, motif):
    # Searches for all occurrences of a motif in a DNA sequence.
    # Returns 1-based index positions of matches (including overlapping ones).

    dna = dna.upper()
    motif = motif.upper()

    # Return empty list for invalid input lengths or empty strings
    if not dna or not motif or len(motif) > len(dna):
        return []

    positions = []
    motif_len = len(motif)

    # Slide a window across the DNA sequence to locate exact matches
    for i in range(len(dna) - motif_len + 1):
        if dna[i:i + motif_len] == motif:
            positions.append(i + 1)
    return positions


def gc_content(sequence):
    # Calculates the GC content percentage of a DNA sequence.
    sequence = sequence.upper()
    if not sequence:
        return 0.0

    # Count occurrences of Guanine (G) and Cytosine (C)
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return round(((g_count + c_count) / len(sequence)) * 100, 2)


def transcribe(dna_sequence):
    # Transcribes a DNA sequence into RNA (replaces T with U).
    return dna_sequence.upper().replace('T', 'U')


if __name__ == "__main__":
    main()
