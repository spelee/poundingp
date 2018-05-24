"""
Notes of interaction with contact
"""


class Note():

    def __init__(self, note, datetime=None):
        self.datetime = datetime
        self.note = note

    def __str__(self):
        # dont assume note is str, cast; just first 7 chars
        return str(self.note)[:7] + (
            "..." if len(str(self.note)) > 7 else "")  # just first 7 chars


"""
XXX
Tests to create:
Note
1) note creation with just text... right one created?
    verify note & str representation
2) note creation with text and datetime... right one created?
    verify note & date & str representation
3) note creation non-text object
    verify note & str representation
4) empty note creation

Notes
1) notes creation... empty
    verify notes empty and string representation
2) notes creation... one
    verify notes & str representation
3) notes creation... 4 notes
    verify notes & str representation
4) empty notes + append
    verify notes and str representation

"""


class Notes():

    def __init__(self, *notes):
        self.notes = [Note(n) for n in notes]

    def append(self, note):
        self.notes.append(note)

    def __str__(self):
        if len(self.notes) < 1:
            return "[]"
        return ("[[" + str(self.notes[0]) +
                "],...[" + str(self.notes[-1]) + "]]")
