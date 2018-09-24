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
		if self.is_hungry == True:
			self.is_hungry = False
			return "Dog fed"
		else:
			return "Dog already fed"

if __name__ == "__main__":
	tom = Dog()
	tom.dog_name = "Tom"
	tom.dog_age = 6
	tom.animal_type = "mammal"
	fletcher = Dog()
	fletcher.dog_name = "Fletcher"
	fletcher.dog_age = 7
	fletcher.animal_type = "mammal"
	larry = Dog()
	larry.dog_name = "Larry"
	larry.dog_age = 9
	larry.animal_type = "mammal"
	my_dogs = Pets()
	my_dogs.store_pet(tom)
	my_dogs.store_pet(fletcher)
	my_dogs.store_pet(larry)
	my_dogs.walking()



