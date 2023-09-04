class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return(f'{self.name} ({self.year}) : ${self.cost}')

    def get_age(self,current_year=0):
        self.age = current_year - self.year
        return self.age

    def is_vintage(self):
        if self.age >= 50:
            return True
        else:
            return False

    def __lt__(self,other):
        if self.age < other.age:
            return True
        else:
            return False