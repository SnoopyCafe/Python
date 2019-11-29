class PartyAnimal:
   letter_counts = 0

   def party(self) :
     self.x = self.x + 1
     print "So far",self.x

an = PartyAnimal()

an.party()
an.party()
an.party()

