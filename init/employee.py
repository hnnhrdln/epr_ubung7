
class Employee:
    """A sample Employee class"""

    def __init__(self, ID, first, last, role):
        self.ID = ID
        self.first = first
        self.last = last
        self.role = role

    def email(self):
        return '{}.{}@email.com'.format(self.firt, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee(('{}', '{}', '{}', '{}')".format(self.ID, self.first, self.last, self.role)
