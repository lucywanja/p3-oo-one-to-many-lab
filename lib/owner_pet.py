class Pet:
    
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird' , 'reptile', 'exotic'] #list of valid pet types

    all = [] # list to store all instances of pet

    def __init__(self, name, pet_type, owner =None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self) #adds the current Pet instance self of the pet.all list


# the pet_type property has a setter that checks if the provided pet_type is in the PET_TYPES list,If not it raises an exception
    @property
    def pet_type(self):
        return self._pet_type #return a private attribute 

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type.')  
        self._pet_type = pet_type   


    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner): #Validates that the owner is an instance of Owner
            raise Exception("Object is not of type Owner")
        self._owner = owner #If type check passes it sets the private attribute _owner of the pet instance to the current Owner instance           
    

class Owner:  

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]  

    def add_pet(self, pet):#Add_pet method ensures the pet arguement is an instance of Pet before assigning the owner the pet
        if not isinstance(pet, Pet): #To ensure the pet parameter is an instance of the Pet class otherwise raise exception
            raise Exception("Input object is not of type Pet")
        pet.owner = self  


    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)           