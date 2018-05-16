import person


class TestPerson():
    """XXX Bad example of testing... but just for now...."""

    def setUp(self):
        self.person_1 = person.Person("John", "Doe")
        self.person_2 = person.Person("John", "Doe")
        self.person_3 = person.Person("Jane", "Doe")

    def test_person_equals(self):
        print("true", self.person_1 == self.person_2)
        print("true", self.person_2 == self.person_1)
        print("false", self.person_1 == self.person_3)
        print("false", self.person_3 == self.person_1)

        print("true", self.person_1 != self.person_3)
        print("true", self.person_3 != self.person_1)
        print("false", self.person_1 != self.person_2)
        print("false", self.person_2 != self.person_1)

        print("true", self.person_1 == self.person_1)
        print("false", self.person_1 != self.person_1)


def main():
    test = TestPerson()
    test.setUp()
    test.test_person_equals()


if __name__ == "__main__":
    # TODO: Should the argparse import be here?
    #    import argparse

    main()
