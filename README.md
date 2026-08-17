# DNA Motif Searcher and Sequence Analyzer
#### Video Demo: https://youtu.be/gUcDAtrKnnE?si=S5ZkMdv7eu6iK2L1
#### Description:

The **DNA Motif Searcher and Sequence Analyzer** is a Python-based command-line tool designed to simplify fundamental bioinformatics tasks. In biological research and computational biology, analyzing DNA sequences is a crucial step toward understanding genetic structures, identifying functional sequence patterns, and simulating molecular biology processes such as gene transcription. This project provides a reliable and thoroughly tested set of functions to validate raw DNA inputs, locate specific target motifs (including overlapping matches), calculate GC-content ratios, and convert DNA sequences into RNA.

---

## Motivation and Project Overview

The goal of this application is to automate standard pre-processing and exploratory analysis tasks:
1. Ensuring input integrity through rigorous sequence validation.
2. Finding nucleotide patterns (motifs) that might correspond to restriction enzyme recognition sites, transcription factor binding sites, or genetic markers.
3. Calculating the GC-content ratio, which directly influences the thermal stability of DNA molecules and melting temperatures ($T_m$) in PCR experiments.
4. Simulating transcription, the biological process where DNA serves as a template to build messenger RNA (mRNA).

---

## Core Features and Implementation Details

The core functionality of the project is implemented in `project.py` using standard, modular Python practices. Below is a detailed breakdown of each custom function:

### 1. `validate_dna(sequence)`
- **Purpose**: Validates whether a given string is a legitimate DNA sequence.
- **Behavior**: Checks every character in the string against the allowed nucleotide set (`A`, `C`, `G`, `T`). It automatically normalizes input strings to uppercase, allowing users to enter sequences in lowercase or mixed case without encountering false validation failures.
- **Return Value**: Returns `True` if the sequence consists solely of valid DNA bases; otherwise, returns `False`. Empty strings or inputs containing spaces, digits, or invalid characters (e.g., `U`, `N`, `Z`) are flagged as invalid.

### 2. `find_motif(sequence, motif)`
- **Purpose**: Locates all starting indices of a target nucleotide pattern (motif) within a parent DNA sequence.
- **Biological Context**: Native string methods like Python's `.find()` or standard regex searches often skip overlapping occurrences (e.g., searching for `ATA` in `ATATA` might return only the first index). In genomics, overlapping sites are biologically significant and must all be detected.
- **Implementation**: Uses a sliding window algorithm to iterate through the parent sequence step-by-step. It supports **overlapping motif matches** and implements **1-based indexing**, aligning with standard biological reference notation (such as FASTA and GenBank formats) rather than standard 0-based programming indices.
- **Return Value**: Returns a list of integer positions (1-indexed) where the motif starts. Returns an empty list `[]` if the sequence is invalid or the motif is not found.

### 3. `gc_content(sequence)`
- **Purpose**: Calculates the proportion of Guanine (`G`) and Cytosine (`C`) bases in a DNA sequence as a percentage.
- **Significance**: `G-C` base pairs form three hydrogen bonds, whereas `A-T` base pairs form only two. Higher GC-content indicates stronger DNA duplex stability.
- **Implementation**: Validates the input sequence first. Counts the occurrences of `G` and `C` (case-insensitively) and divides the total by the length of the sequence, returning a floating-point percentage rounded to two decimal places (e.g., `50.0`).
- **Return Value**: Returns a float representing the percentage (e.g., `42.86`). Returns `0.0` for invalid or empty sequence inputs.

### 4. `transcribe(sequence)`
- **Purpose**: Simulates the primary step of central dogma in molecular biology — DNA to RNA transcription.
- **Implementation**: Replaces every occurrence of Thymine (`T`) with Uracil (`U`), while converting the rest of the string to uppercase.
- **Return Value**: Returns the transcribed RNA string (e.g., `ATGC` becomes `AUGC`). If the input sequence contains invalid bases, the function raises a `ValueError` or returns an error indication to prevent downstream errors in genetic data processing.

---

## Project Structure and File Descriptions

- **`project.py`**:
  The primary entry point of the program. It contains the implementation of the four standalone functions described above, alongside a `main()` function that manages the interactive command-line interface (CLI) for user interaction.
- **`test_project.py`**:
  Contains automated unit test suites using the `pytest` framework. Each standalone function from `project.py` is tested against multiple scenarios, including standard inputs, edge cases (such as empty strings, single-character sequences, and overlapping motifs), case-insensitivity, and invalid input handlings.
- **`README.md`**:
  Detailed documentation outlining the project's background, design decisions, structure, and execution instructions.

---

## Design Decisions

1. **Standalone Functions for Testability**:
   In accordance with CS50 guidelines, all main logic functions are designed as pure, standalone functions independent of input/output (`input()` / `print()`) operations. This separation enables seamless automated testing via `pytest`.

2. **1-Based Indexing for Biological Standards**:
   While Python natively uses 0-based indexing, biological sequence notation overwhelmingly uses 1-based indexing (where the first nucleotide in a chromosome or gene is position 1). To make the tool intuitive for scientists and educators, `find_motif` outputs 1-based positions.

3. **Case-Insensitive Input Processing**:
   User inputs can frequently be pasted from varied sources with lowercase letters. Converting inputs to uppercase across all functions improves user experience and prevents silent errors.

---

## How to Run the Project

### Prerequisites
Ensure Python 3.10+ and `pytest` are installed:
```bash
pip install pytest
