class piglet:
    name = ""
    def speak(self):
        print("Oink, i'm {} and i'm a piglet".format(self.name))

hamlet = piglet()
hamlet.name = "Hamlet"
hamlet.speak()

hammy = piglet()
hammy.name = "Hammy"
hammy.speak()
