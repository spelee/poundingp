# XXX should settings be in a class?


class Settings():

    def __init__(self):
        self.db_home = "."
        self.db_people_csv = "people.csv"
        self.db_people_path = self.db_home + "/" + self.db_people_csv
