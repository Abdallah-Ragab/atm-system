import json
import random
from storage import JSONStorage
from models import Account, TransactionType, Transaction
from bank import Bank



def all_note_possibilities(results, note_idx, notes):
    _results = []
    note = notes[note_idx]
    for result in results:
        amount = result["amount"]
        if amount == 0:
            _results.append(result)
            continue
        count = amount // note
        for i in range(count+1):
            _result = result.copy()
            _result["amount"] = amount - i*note
            _result[note] = i
            _results.append(_result)
    if note_idx < len(notes) - 1:
        return all_note_possibilities(_results, note_idx+1, notes)
    else:
        return _results

def brute_force(amount, notes):
    all_possibilities = all_note_possibilities([{"amount": amount}], 0, notes)
    valid_possibilities = [p for p in all_possibilities if p["amount"] == 0]
    least_notes = 100000
    least_notes_possibility = None

    for possibility in valid_possibilities:
        sum_of_notes = 0
        _possibility = {}
        for note in possibility.keys():
            if note in notes:
                _possibility[note] = possibility[note]
                sum_of_notes += possibility[note]
        if sum_of_notes < least_notes:
            least_notes = sum_of_notes
            least_notes_possibility = _possibility
    return least_notes_possibility


def greedy_algorithm(amount, notes):
    result = {}
    for note in sorted(notes, reverse=True):
        count = amount // note
        if count > 0:
            result[note] = count
            amount -= count * note
    if amount == 0:
        return result
    else:
        # Handle the case where it's not possible to give the exact amount with available notes
        return None

amount = random.randint(1, 20)*20
notes = [200, 100, 50, 20]

def dynamic_programming(amount, notes):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for note in notes:
        for i in range(note, amount + 1):
            dp[i] = min(dp[i], dp[i - note] + 1)

    if dp[amount] == float('inf'):
        return None

    result = {}
    remaining_amount = amount
    for note in sorted(notes, reverse=True):
        count = remaining_amount // note
        if count > 0:
            result[note] = count
            remaining_amount -= count * note

    return result

def total(notes):
    total = 0
    if notes is None:
        return total
    for note in notes:
        total += note * notes[note]
    return total

def test_algorithm(algorithm, amount, notes):
    result = algorithm(amount, notes)
    if result is None:
        return False
    return total(result) == amount


brute_force_success = 0
greedy_algorithm_success = 0
dynamic_programming_success = 0

for _ in range(10000):
    amount = random.randint(1, 20)*20
    notes = [200, 100, 50, 20]
    if test_algorithm(brute_force, amount, notes):
        brute_force_success += 1
    if test_algorithm(greedy_algorithm, amount, notes):
        greedy_algorithm_success += 1
    if test_algorithm(dynamic_programming, amount, notes):
        dynamic_programming_success += 1

print("Brute force success rate:", brute_force_success/100, "%")
print("Greedy algorithm success rate:", greedy_algorithm_success/100, "%")
print("Dynamic programming success rate:", dynamic_programming_success/100, "%")