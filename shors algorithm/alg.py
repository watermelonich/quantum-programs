from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# Define the number to be factored (you'll need to replace this with your target number)
N = 15

# Quantum circuit for the quantum period finding
def qpe_amod15(a):
    n_count = 8  # Number of counting qubits
    qc = QuantumCircuit(4+n_count, n_count)
    for q in range(n_count):  # Initialize counting qubits in state |+>
        qc.h(q)     
    qc.x(3+n_count)  # And auxiliary register in state |1>
    for q in range(n_count):  # Do controlled-U operations
        qc.append(c_amod15(a, 2**q), 
                 [q] + [i+n_count for i in range(4)])
    qc.append(qft_dagger(n_count), range(n_count))  # Do inverse-QFT
    qc.measure(range(n_count), range(n_count))
    # Simulating the circuit to get the final measurements
    aer_sim = Aer.get_backend('aer_simulator')
    # Setting memory=True below allows us to see a list of each sequential reading
    # for each experiment.
    # Setting shots=1 gives us the most likely result
    # (with the highest probability)
    result = execute(qc, aer_sim, memory=True, shots=1).result()
    readings = result.get_memory()
    print("Register Reading: " + readings[0])
    print("Corresponding Binary: " + "".join([chr(int(readings[0][i:i+4],2)+ord('0')) for i in range(0, n_count*4, 4)]))
    return int(readings[0],2)

# Implementing the Quantum Phase Estimation (QPE) subroutine
# as a gate
def qpe_amod15_gate():
    U = np.array([[1, 0, 0, 0],
                  [1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0]])
    return qpe_amod15_gate, U

# Simulating Shor's Algorithm
np.random.seed(1)     # This is to make sure we get reproduceable results
a = np.random.randint(2,15)
print("Chose a=", a)
factor_found = False
attempt = 0
while not factor_found:
    attempt += 1
    print(f"Attempt {attempt}")
    measured = qpe_amod15(a)
    print(measured)
    if measured != 0:
        # Classical post-processing to find factors
        gcd_attempt = np.gcd(int(np.power(a, measured/2)) - 1, N)
        if gcd_attempt > 1 and gcd_attempt < N:
            print(f"Non-trivial factor found: {gcd_attempt}")
            factor_found = True