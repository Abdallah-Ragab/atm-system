import random


class SAFE:
    DEFAULT_NOTES = {20: 1_00, 50: 1_00, 100: 1_00, 200: 1_00}
    NOTES = DEFAULT_NOTES.copy()

    @staticmethod
    def total():
        total = 0
        for note in SAFE.NOTES:
            total += note * SAFE.NOTES[note]
        return total

    @staticmethod
    def withdraw_note(note, amount):
        if note in SAFE.NOTES:
            if SAFE.NOTES[note] >= amount:
                SAFE.NOTES[note] -= amount
                return True
        return False

    @staticmethod
    def deposit_note(note, amount):
        if note in SAFE.NOTES:
            SAFE.NOTES[note] += amount
            return True
        return False

    @staticmethod
    def withdraw(amount):
        withdrawal_notes = {}

        # Sort the notes in descending order of importance
        sorted_notes = sorted({note: SAFE.NOTES[note] for note in SAFE.NOTES if SAFE.NOTES[note] > 0}.keys(), reverse=True)

        # Initialize a table to store the minimum number of notes for each sub-amount
        dp_table = {0: 0}

        for sub_amount in range(1, amount + 1):
            dp_table[sub_amount] = float('inf')

            for note in sorted_notes:
                if sub_amount >= note and dp_table[sub_amount - note] + 1 < dp_table[sub_amount]:
                    dp_table[sub_amount] = dp_table[sub_amount - note] + 1

        if dp_table[amount] == float('inf'):
            # Cannot meet the requested amount with available notes
            return False

        remaining_amount = amount
        for note in sorted_notes:
            while remaining_amount >= note and dp_table[remaining_amount - note] + 1 == dp_table[remaining_amount]:
                withdrawal_notes[note] = withdrawal_notes.get(note, 0) + 1
                remaining_amount -= note

        if remaining_amount != 0:
            # Cannot meet the requested amount with available notes
            return False
        # Update the notes in SAFE.NOTES
        for note, count in withdrawal_notes.items():
            SAFE.withdraw_note(note, count)

        return withdrawal_notes

    def note_combinations(results, note_idx):
        _results = []
        note = list(SAFE.NOTES.keys())[note_idx]

        for result in results:
            amount = result["amount"]
            if amount == 0:
                _results.append(result)
                continue
            count_limit = min(amount // note, SAFE.NOTES[note])
            for i in range(count_limit + 1):
                _result = result.copy()
                _result["amount"] = amount - i * note
                _result[note] = i
                _results.append(_result)

        if note_idx < len(SAFE.NOTES) - 1:
            return SAFE.note_combinations(_results, note_idx + 1)
        else:
            return _results

    @staticmethod
    def withdraw_(amount):
        all_combinations = SAFE.note_combinations([{"amount": amount}], 0)
        valid_combinations = [p for p in all_combinations if p["amount"] == 0]
        least_notes = float('inf')
        least_notes_combination = None

        for combination in valid_combinations:
            sum_of_notes = 0
            _combination = {}
            for note in combination.keys():
                if note in SAFE.NOTES:
                    _combination[note] = combination[note]
                    sum_of_notes += combination[note]
            if sum_of_notes < least_notes:
                least_notes = sum_of_notes
                least_notes_combination = _combination

        if least_notes_combination:
            for note, count in least_notes_combination.items():
                SAFE.withdraw_note(note, count)
            return least_notes_combination

        else: return False









withdrawal_values = [random.randint(1, 100)*20 for _ in range(100)]
def test_withdrawal():
    print("Testing brute force...")
    count = 0
    print("Initial total:", SAFE.total())
    print("Initial notes:", SAFE.NOTES)
    for amount in withdrawal_values:
        print(f"Withdrawing {amount}... ", end=" ")
        result = SAFE.withdraw(amount)
        if result is not False:
            print(result, "Success")
            count += 1
        else:
            print("Failed")
            break
    print("last amount:", amount)
    print(f"Succeeded {count} times")
    print(f"Remaining Notes: {SAFE.NOTES}")
    print(f"Remaining Total: {SAFE.total()}")

def test_withdrawal_():
    print("Testing dynamic programming...")
    count = 0
    print("Initial total:", SAFE.total())
    print("Initial notes:", SAFE.NOTES)
    for amount in withdrawal_values:
        print(f"Withdrawing {amount}... ", end=" ")
        result = SAFE.withdraw_(amount)
        if result is not False:
            print(result, "Success")
            count += 1
        else:
            print("Failed")
            break
    print("last amount:", amount)
    print(f"Succeeded {count} times")
    print(f"Remaining Notes: {SAFE.NOTES}")
    print(f"Remaining Total: {SAFE.total()}")


# test_withdrawal()
# SAFE.NOTES = SAFE.DEFAULT_NOTES.copy()
# test_withdrawal_()


def test_two_algorithms():
    brute_force_success = 0
    dynamic_programming_success = 0
    brute_force_notes = SAFE.NOTES.copy()
    dynamic_programming_notes = SAFE.NOTES.copy()

    brute_force_finish = False
    dynamic_programming_finish = False

    for _ in range(10000):
        amount = random.randint(1, 100) * 20
        print(amount, end=" ")
        if not brute_force_finish:
            SAFE.NOTES = brute_force_notes.copy()
            brute_force_result = SAFE.withdraw(amount)
            brute_force_notes = SAFE.NOTES.copy()
            print(brute_force_result, brute_force_notes, end="\n")

        if not dynamic_programming_finish:
            SAFE.NOTES = dynamic_programming_notes.copy()
            dynamic_programming_result = SAFE.withdraw_(amount)
            dynamic_programming_notes = SAFE.NOTES.copy()
            print("\t" ,dynamic_programming_result, dynamic_programming_notes, end="\n")

        if brute_force_result is not False:
            brute_force_success += 1
        else:
            brute_force_finish = True
        if dynamic_programming_result is not False:
            dynamic_programming_success += 1
        else:
            dynamic_programming_finish = True
        if brute_force_finish and dynamic_programming_finish:
            break


    print(f"Brute Force Success: {brute_force_success}")
    print(f"Dynamic Programming Success: {dynamic_programming_success}")

# test_two_algorithms()