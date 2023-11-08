import numpy as np

from qcpy import quantumcircuit


def inc(x):
    qc = quantumcircuit(qubits=x, little_endian=True, prep="z")
    return qc.flatten()


def test_01a():
    assert (inc(1) == np.array([1 + 0j, 0 + 0j], "F")).all(), "test_01a Failed on QuantumCircuit"


def test_01b():
    assert (inc(2) == np.array([1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j], "F")).all(), "test_01b Failed on QuantumCircuit"


def test_01c():
    assert (
        inc(3) == np.array([1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    ).all(), "test_01c Failed on QuantumCircuit"


def test_01d():
    assert (
        inc(4)
        == np.array(
            [
                1 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
                0 + 0j,
            ],
            "F",
        )
    ).all(), "test_01d Failed on QuantumCircuit"
