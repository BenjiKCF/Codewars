def decompose_single_strand(single_strand):
    return 'Frame 1: '+ ' '.join(split(single_strand, 3)) + "\n" +'Frame 2: ' + single_strand[0] + ' ' +' '.join(split(single_strand[1:], 3))+ "\n"'Frame 3: ' + single_strand[0:2] + ' ' +' '.join(split(single_strand[2:], 3))
def split(s, n):
  new_list = []
  for i in range(0, len(s), n):
    new_list.append(s[i:i+n])
  return new_list

print decompose_single_strand("AGGTGACACCGCAAGCCTTATATTAGC")
#  "Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC\nFrame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC\nFrame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C")

def decompose_single_strand(dna):
    return '\n'.join('Frame {}: {}'.format(k+1, frame(dna, k)) for k in range(3))

def frame(s, k):
    return ' '.join(([s[:k]] if k else []) + [s[i:i+3] for i in range(k, len(s), 3)])
