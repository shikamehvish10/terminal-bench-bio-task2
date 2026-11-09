# Bioinformatics GC Content Calculator

## Overview
This repository contains a professional Python-based task solution designed to process DNA sequences, compute their Guanine-Cytosine (GC) content percentage, and export structured quantitative reports.

## Project Structure
- `solution.py`: Main executable script containing the core sequence parsing and GC percentage calculation logic.
- `gc_report.csv`: Generated output report containing sequence identifiers, lengths, and computed GC metrics.

## Technical Implementation
- **Language:** Python 3.x
- **Libraries Used:** Built-in `csv` module for structured data logging.
- **Workflow:** 
  1. Reads a target DNA sequence string.
  2. Computes total sequence length.
  3. Counts occurrences of 'G' and 'C' nucleotides to derive the percentage.
  4. Exports the aggregated results into a standardized CSV format.

## Usage
Run the script directly from your terminal:
\`\`\`bash
python solution.py
\`\`\`
