class School:

    def __init__(self, name, nationality):

        self.name = name
        self.nationality = nationality

    def Name(self):
        return self.name

    def Nationality(self):
        return self.nationality


class Eit(School):

    def __init__(self, name, nationality, funfact):
        super().__init__(name, nationality)
        self.funfact = funfact

    def GetEIT(self):
        self.funfact = input("What's your funfact?\n")
        return self.Name() + " -> " + self.Nationality() + " -> " + self.funfact


class Fellows(School):

    def __init__(self, name, nationality, happiness, eat, teach):
        super().__init__(name, nationality)
        self.happiness = happiness
        self.eat = eat
        self.teach = teach

    def HasEaten(self):
    	self.eat = input("Has fellow eaten? \n")
    	if self.eat == "Yes":
    		self.happiness = True
    	elif self.eat == "No":
    		self.happiness = False

    	return self.happiness

    def GetFellows(self):
        return self.Name() + " -> " + self.Nationality() + " -> " + self.happiness + " -> " + self.eat + " -> " + self.teach


class Person():
    def __init__(self,name,nationality)

AllFellows = Fellows("Andrew","USA","False","No","Yes")

print(AllFellows.GetFellows())

