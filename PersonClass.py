class Person():
    def __init__(self, the_name):
        self.name = the_name
    def talk(self):
        print(f'My name is {self.name}')


p1 = Person('Jatin')
p1.talk()