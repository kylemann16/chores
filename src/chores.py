import csv
from enum import Enum
from typing import List

csv_path = 'chores_list.csv'

#frequency expressed in weeks
class Frequency(Enum):
    weekly = 1
    biweekly = 2
    semimonthly = 2
    monthly = 4
    bimonthly = 8
    semiannually = 24
    annually = 48
    yearly = 48

class Cleaner():
    def __init__(self, name, phone_number):
        self.name: str = name
        self.phone_number: int = phone_number
        self.chores: List[str] = []

    def get_chores(self):
        return [ c.name for c in self.chores ]

    def add_chore(self, chore_name):
        self.chores.append(chore_name)

class Chore():
    def __init__(self, name, frequency, offset, assignment):
        self.name: str = name
        self.frequency: Frequency = frequency
        self.offset: int = offset
        self.assignment: Cleaner = assignment

    def get_assignment(self):
        if self.assignment not in ['Any', 'All']:
            return self.assignment


class ChoreList():
    def __init__(self):
        self.chore_list: List[Chore] = [ ]
        self.cleaners: List[Cleaner] = [ ]

    def add_cleaner(self, c: Cleaner):
        self.cleaners.append(c)

    def add_chore(self, c: Chore):
        if not self.cleaners:
            raise("No cleaners availabled")
        cleaner = self.cleaners[0]
        for temp_cleaner in self.cleaners:
            temp_cleaner: Cleaner
            if len(temp_cleaner.chores) < len(cleaner.chores):
                cleaner = temp_cleaner
        cleaner.add_chore(c)


def get_chores():
    with open(csv_path,newline='\n') as chores_file:
        sniff = csv.Sniffer().sniff(chores_file.read(), delimiters=',')
        chores_file.seek(0)
        reader = csv.reader(chores_file, dialect=sniff)

        chore_list = ChoreList()
        chore_list.add_cleaner(Cleaner('Elena', 5635997621))
        chore_list.add_cleaner(Cleaner('Kyle', 9896003828))

        for row in reader:
            if row[0] == 'name':
                continue
            name, frequency, offset, assignment = row
            print(', '.join([name,frequency,offset,assignment]))

            chore = Chore(name, frequency, offset, assignment)
            chore_list.add_chore(chore)

        import pdb; pdb.set_trace()
        print([i.get_chores() for i in chore_list.cleaners])

get_chores()