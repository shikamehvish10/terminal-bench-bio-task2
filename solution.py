import csv

def calc_gc():
    dna_sequence = "AGCTCGATCGATCG"
    length = len(dna_sequence)
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    gc_percentage = (gc_count / length) * 100
    results = [["seq_1", length, round(gc_percentage, 2)]]
    
    with open("gc_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sequence_id", "length", "gc_percentage"])
        writer.writerows(results)

if __name__ == "__main__":
    calc_gc()
