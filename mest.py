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
        School.__init__(self, name, nationality)
        self.funfact = funfact
        self.funfact = input("What's your funfact?\n")

    def GetSchool(self):
        return self.Name() + " -> " + self.Nationality() + " -> " + self.funfact


class Fellows(School):

    def __init__(self, name, nationality, happiness, eat, teach):
        School.__init__(self, name, nationality)
        self.happiness = happiness
        self.eat = eat
        self.teach = teach

    def HasEaten(self):
    	self.eat = input("Has fellow eaten?")
    	if self.eat == "Yes":
    		# self.happiness = True
    		print("Fellow is happy")
    	elif self.eat == "No":
    		# self.happiness = False
    		("Fellow is not happy")
    	else:
    		print("Type Yes/No")


    	# if self.happiness == True:
    	# 	print("Fellow is happy")
    	# else:
    	# 	("Fellow is not happy")

    def GetFellows(self):
        return self.Name() + " -> " + self.Nationality() + " -> " + self.happiness + " -> " + self.eat + " -> " + self.teach

Downstairs_EIT = Eit("Eyram", "Ghana", "Andrew == Tech")
All_Fellows = Fellows("Francis", "Ghana", "1000", "Banku", "True")

# Downstairs_EIT.SayFunfact()

print(Downstairs_EIT.GetSchool())
print(All_Fellows.HasEaten())
