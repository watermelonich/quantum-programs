import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Initialize a quantum and classical register with 2 qubits
alice_qubit = 0
bob_qubit = 1
qc = QuantumCircuit(2, 2)

# Alice generates random bits to encode her qubits
alice_bits = np.random.randint(2, size=2)
alice_bases = np.random.randint(2, size=2)  # 0 for |0>/<1>, 1 for |+>/<->

# Function to prepare qubits by Alice
def alice_prepare():
    for i in range(2):
        if alice_bases[i] == 0:  # Prepare in Z-basis
            if alice_bits[i] == 1:
                qc.x(alice_qubit)
        else:  # Prepare in X-basis
            if alice_bits[i] == 0:
                qc.h(alice_qubit)

# Alice prepares her qubits
alice_prepare()

# Simulate the quantum channel (ideally)
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
alice_statevector = result.get_statevector()

# Bob randomly chooses measurement bases
bob_bases = np.random.randint(2, size=2)

# Function to perform measurements by Bob
def bob_measure():
    for i in range(2):
        if bob_bases[i] == 0:  # Measure in Z-basis
            qc.measure(i, i)
        else:  # Measure in X-basis
            qc.h(i)
            qc.measure(i, i)
            qc.h(i)

# Bob performs measurements
bob_measure()

# Simulate measurement outcomes
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1).result()
bob_results = list(result.get_counts().keys())[0]

# Extract Bob's results
bob_bits = [int(bit) for bit in bob_results]
bob_bases_str = ''.join(['Z' if base == 0 else 'X' for base in bob_bases])

print("Alice's bits:", alice_bits)
print("Alice's bases:", alice_bases)
print("Bob's bases:", bob_bases_str)
print("Bob's measured bits:", bob_bits)

# Compare bases and extract the sifted key
sifted_key = [alice_bits[i] for i in range(2) if alice_bases[i] == bob_bases[i]]

print("Sifted key:", sifted_key)
