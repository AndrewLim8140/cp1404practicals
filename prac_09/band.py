from prac_09.musician import Musician

class Band(Musician):
    def __init__(self,name):
        super().__init__(name)
        self.members =[]

    def __str__(self):
        counter = 0
        li = []
        while counter < len(self.members) :
            test= f'{self.members[counter]}'
            li.append(test)
            counter += 1

        return f'{self.name} {str(li)}'

    def add(self, member):
        self.members.append(member)
        len(self.members)
        
    def play(self):
        counter = 0
        li = []
        while counter < len(self.members):
            test = f'{self.members[counter]}'
            li.append(test)
            counter += 1
            return super().play()
