class Pets():
	__init__(self):
	self.pet_store = list()

	def store_pet(self, pet):
		self.pet_store.append(pet)
	def walking(self):
		for pet in self.pet_store:
			print("{} is walking".format(pet.name))

class Dog():
	def __init__(self):
		self.dog_name = str()
		self.dog_age = int()
		self.animal_type = str()
		self.is_hungry = True

	def check_hunger(self):
		if self.is_hungry == True:
			print("{} is hungry".format(self.dog_name))
		else:
			print("{} is not hungry".format(self.dog_name))

	def eat(self):
		self.is_hungry = False

if __name__ == "__main__":
	tom = Dog()
	tom.dog_name = "Tom"
	tom.dog_age = 6
	tom.animal_type = "mammal"
	fletcher = Dog()
	fletcher.dog_name = "Fletcher"
	fletcher.dog_age = 7
	fletcher.animal_type = "mammal"



