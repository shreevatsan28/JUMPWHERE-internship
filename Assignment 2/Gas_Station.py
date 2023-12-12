def can_complete_circuit(gas, cost, start):
    n = len(gas)
    remaining = 0

    for i in range(start, start + n):
        remaining += gas[i % n] - cost[i % n]

        if remaining < 0:
            return False

    return True

gas = [1, 5, 4, 2, 1, 2, 1, 4, 3, 3]
cost = [5, 8, 1, 6, 2, 3, 5, 2, 1, 2]
start = 0

if can_complete_circuit(gas, cost, start):
    print("You can complete the circuit.")
else:
    print("You cannot complete the circuit.")
