import pytest
from project import find_motif, gc_content, transcribe, validate_dna


def test_validate_dna():
    # Test validation function with valid, invalid, lowercase, and empty inputs.
    assert validate_dna("ATGCGATC") == True
    assert validate_dna("atgcgatc") == True
    assert validate_dna("ATGCX") == False  # Contains invalid character 'X'
    assert validate_dna("123") == False  # Contains numbers
    assert validate_dna("") == False  # Empty string case


def test_find_motif():
    # Test motif search including overlapping matches, missing motifs, and edge cases.
    # Test sequence with multiple overlapping occurrences of 'ATAT'
    assert find_motif("GATATATGCATATACTT", "ATAT") == [2, 4, 10]

    # Test motif that does not exist in the DNA
    assert find_motif("ATGCGATCG", "AAAA") == []

    # Test case insensitivity handling (ΔΙΟΡΘΩΜΕΝΟ: [4, 8])
    assert find_motif("atgcgatcg", "cg") == [4, 8]

    # Test edge cases
    assert find_motif("", "AT") == []
    assert find_motif("ATGC", "ATGCAAAA") == []


def test_gc_content():
    # Test GC-content calculation accuracy for various sequences.
    assert gc_content("CCACCACC") == 75.0
    assert gc_content("ATAT") == 0.0
    assert gc_content("GCAT") == 50.0
    assert gc_content("") == 0.0  # Empty sequence case


def test_transcribe():
    # Test DNA to RNA transcription conversion.
    assert transcribe("GATTACA") == "GAUUACA"
    assert transcribe("gattaca") == "GAUUACA"  # Lowercase conversion
    assert transcribe("CGCG") == "CGCG"  # Sequence without Thymine
