import random


def note_combinations(results, note_idx, notes):
    _results = []
    note = list(notes.keys())[note_idx]

    for result in results:
        amount = result["amount"]
        if amount == 0:
            _results.append(result)
            continue
        count_limit = min(amount // note, notes[note])
        for i in range(count_limit + 1):
            _result = result.copy()
            _result["amount"] = amount - i * note
            _result[note] = i
            _results.append(_result)

    if note_idx < len(notes) - 1:
        return note_combinations(_results, note_idx + 1, notes)
    else:
        return _results


def brute_force(amount, notes):
    all_combinations = note_combinations([{"amount": amount}], 0, notes)
    valid_combinations = [p for p in all_combinations if p["amount"] == 0]
    least_notes = float('inf')
    least_notes_combination = None

    for combination in valid_combinations:
        sum_of_notes = 0
        _combination = {}
        for note in combination.keys():
            if note in notes:
                _combination[note] = combination[note]
                sum_of_notes += combination[note]
        if sum_of_notes < least_notes:
            least_notes = sum_of_notes
            least_notes_combination = _combination
    return least_notes_combination


def total(notes):
    total = 0
    if notes is None:
        return total
    for note in notes:
        total += note * notes[note]
    return total

notes = {20: 100, 50: 20, 100: 10, 200: 5}
safe_total = total(notes)

counter = 0
for _ in range(10000):
    amount = random.randint(1, 100) * 20
    result = brute_force(amount, notes)
    total_dispensed = total(result)
    if total_dispensed != amount:
        print(f"Success: {counter} times, Remaining: {safe_total}")
        break
    safe_total -= total_dispensed
    counter += 1