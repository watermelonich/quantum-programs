
from qiskit import *
import matplotlib.pyplot as plt
import numpy as np

oracle = QuantumCircuit(2, name='oracle')
oracle.cz(0,1)
oracle.to_gate()
oracle.draw()

backend = Aer.get_backend('statevector_simulator')
grover_circ = QuantumCircuit(2, 2)
grover_circ.h([0, 1])
grover_circ.append(oracle, [0,1])
grover_circ.draw()

job = execute(grover_circ, backend)
result = job.result()
sv = result.get_statevector()
np.round(sv, 2)