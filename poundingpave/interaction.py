"""
Notes of interaction with contact
"""


class Interaction():

    def __init__(self, type, datetime=None):
        self.datetime = datetime
        self.type = type
        self.next = None  # what is the next step

    def __str__(self):
        return self.datetime + ":" + self.type


"""
XXX
Tests to create:
Interaction
1) interaction creation with just type... right one created?
    verify type & str representation
2) interaction creation with type and datetime... right one created?
    verify type & date & str representation
3) note creation non-text object
    verify note & str representation
4) empty note creation

Interactions
1) empty creation... empty
    verify interactions empty list and string representation
2) creation... one
    verify length of one of interaction obj & str representation
3) create creation... 4 notes
    verify length of 4 & str representation
4) empty notes + append
    verify interaction was added and str representation

"""


class Interactions():

    def __init__(self, *notes):
        self.notes = [Note(n) for n in notes]

    def append(self, note):
        self.notes.append(note)

    def __str__(self):
        if len(self.notes) < 1:
            return "[]"
        return ("[[" + str(self.notes[0]) +
                "],...[" + str(self.notes[-1]) + "]]")
