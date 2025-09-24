class Animal:
    def __init__(self, specie:str,  sound:str): #construtor 
        self.specie: str = ""
        self.age : int = 0 
        self.sound: str = ""

    
    def __str__(self) -> str: #toString
        return f"{self.specie} : {self.age} : {self.sound}"
    
    def ismakeSound(self) -> str:
        if self.age== 0:  # early return
            return "--"
        if self.age== 1:
            return f"{self.sound}"
        if self.age == 2:
            return f"{self.sound}"
        if self.age == 3:
            return f"{self.sound}"
        if self.age == 4:
            return "RIP"
    def ageBy (self, increment : int):
        if self.age >= 4:
            print(f"warning: {self.specie} morreu.")
        self.age += increment
        if self.age > 4:
            self.age = 4 


            