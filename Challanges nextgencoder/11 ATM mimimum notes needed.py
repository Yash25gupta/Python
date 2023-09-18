# An algorithim for ATM software which will accept a withdraw amount
# and gives "error" as output if the ammount is invalid else give no of minimum notes needed.
# Notes: 50, 100, 200, 500, 2000
#     TEST CASES:
#   INPUT   OUTPUT
#   2531    error
#   3500    4
#   1250    3
#   1305    error


def withdrawAmount(amount):
    if amount % 50 != 0: return "Error"
    notes = {2000: 0, 500: 0, 200: 0, 100: 0, 50: 0}
    totalNotes = 0
    for curr in notes.keys():
        currNoteCount = amount // curr
        amount -= currNoteCount * curr
        notes[curr] = currNoteCount
        totalNotes += currNoteCount
    return totalNotes, notes


amount = int(input("Enter Amount to withdraw: "))
print(withdrawAmount(amount))
