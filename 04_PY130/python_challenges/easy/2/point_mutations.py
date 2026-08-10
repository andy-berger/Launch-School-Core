class DNA:
    def __init__(self, strand):
        self.strand = strand
    
    def hamming_distance(self, other_strand):
        differences = 0
        for idx in range(min(len(self.strand), len(other_strand))):
            if self.strand[idx] != other_strand[idx]:
                differences += 1
        
        return differences