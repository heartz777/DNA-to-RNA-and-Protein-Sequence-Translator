genetic_code = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def dna_rna(dna_seq):
 return dna_seq.upper().replace('T', 'U')

def rna_protein(rna_seq):
 pro_seq = ''
 for i in range(0, len(rna_seq)-2, 3):
  codon = rna_seq[i:i+3]
  amino_acid = genetic_code.get(codon, '?')  # '?' for unknown codons
  if amino_acid == '*':  # Stop codon
   break
  pro_seq += amino_acid
 return pro_seq

def main():
    dna_seq = input("Enter a DNA sequence: ").strip()
    valid_bases = {'A', 'T', 'C', 'G'}
    if not set(dna_seq.upper()).issubset(valid_bases):
     print("Warning: Sequence contains invalid characters.")
    rna_seq = dna_rna(dna_seq)
    pro_seq = rna_protein(rna_seq)
    print("RNA sequence: ", rna_seq)
    print("Protein sequence: ", pro_seq)
   

if __name__ == "__main__":
 main()
    
