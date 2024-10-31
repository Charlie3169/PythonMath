import numpy as np
# https://www.cantorsparadise.com/a-magical-theorem-was-undiscovered-for-thousands-of-years-7d1a7cdca766
def generate_sequence(n):
    """Generate the first n natural numbers."""
    return list(range(1, n + 1))

def remove_sequence(seq, remove_seq):
    """Remove elements based on the pattern defined by remove_seq from seq."""
    return [x for i, x in enumerate(seq) if (i + 1) % remove_seq != 0]

def partial_sums(seq):
    """Calculate the partial sums of a sequence."""
    sums = []
    current_sum = 0
    for num in seq:
        current_sum += num
        sums.append(current_sum)
    return sums

def generalized_transformation(start_seq, remove_seqs):
    """Apply the generalized transformation to start_seq using remove_seqs."""
    seq = start_seq
    for remove_seq in remove_seqs:
        seq = remove_sequence(seq, remove_seq)
        seq = partial_sums(seq)
    return seq

def show_examples():
    """Run examples to demonstrate the patterns."""
    examples = {
        "Powers of 2": {
            "start_seq": generate_sequence(20),
            "remove_seqs": [2, 3, 4, 5],
            "description": "Removing every n-th number and taking partial sums to get powers of 2."
        },
        "Triangular Numbers": {
            "start_seq": generate_sequence(30),
            "remove_seqs": [1, 3, 6, 10],
            "description": "Removing triangular numbers and taking partial sums to get factorials."
        },
        "Exponential Relationship": {
            "start_seq": generate_sequence(20),
            "remove_seqs": [2, 4, 6, 8],
            "description": "Removing numbers of the form n, 2n, 3n, etc., to see exponential growth."
        }
    }
    
    for name, example in examples.items():
        print(f"\n{name}:")
        result = generalized_transformation(example["start_seq"], example["remove_seqs"])
        print(f"Description: {example['description']}")
        print(f"Result: {result}\n")

show_examples()
