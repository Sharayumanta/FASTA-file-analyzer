# FASTA File Analyzer V1.0
# Reads a FASTA file, validates DNA sequences,
# and calculates basic sequence statistics.

VALID_BASES = {"A", "T", "C", "G"}


def is_valid_sequence(sequence):
    """Check if a DNA sequence contains only valid bases."""
    for base in sequence:
        if base not in VALID_BASES:
            return False
    return True


def gc_content(sequence):
    """Calculate GC content percentage."""
    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100


def analyze_sequence(name, sequence):
    """Display statistics for a DNA sequence."""

    print("=" * 40)
    print(f"Sequence Name : {name}")
    print(f"Length        : {len(sequence)}")
    print()

    print(f"A Count       : {sequence.count('A')}")
    print(f"T Count       : {sequence.count('T')}")
    print(f"C Count       : {sequence.count('C')}")
    print(f"G Count       : {sequence.count('G')}")
    print()

    print(f"GC Content    : {gc_content(sequence):.2f}%")
    print("=" * 40)
    print()


def read_fasta(filename):
    """Read sequences from a FASTA file."""

    sequences = []

    with open(filename, "r") as file:
        name = ""
        sequence = ""

        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if name != "":
                    sequences.append((name, sequence))

                name = line[1:]
                sequence = ""

            else:
                sequence += line.upper()

        if name != "":
            sequences.append((name, sequence))

    return sequences


def main():
    filename = input("Enter FASTA file name: ")

    try:
        sequences = read_fasta(filename)

        if len(sequences) == 0:
            print("No sequences found.")
            return

        for name, sequence in sequences:

            if not is_valid_sequence(sequence):
                print(f"Invalid sequence detected in '{name}'.")
                continue

            analyze_sequence(name, sequence)

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()