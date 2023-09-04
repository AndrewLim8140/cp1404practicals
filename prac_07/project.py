class Project:
    def __init__(self, project_name='', start_date='', priority=0, esitmated_cost=0, completion_percentage=0):
        self.name = project_name
        self.start_date = start_date.split('/')
        self.day = self.start_date[0]
        self.month = self.start_date[1]
        self.year = self.start_date[2]
        self.priority = priority
        self.cost = esitmated_cost
        self.percent = completion_percentage

    def __str__(self):
        return f'{self.name},{self.start_date},{self.priority},{self.cost},{self.percent}'

    def __lt__(self, other):
        if self.year > other.year:
            return False
        else:
            if self.month > other.month:
                return False
            else:
                if self.day > other.day:
                    return False
                else:
                    return True

    def is_completed(self):
        if self.percent == 100:
            return True
        else:
            return False
