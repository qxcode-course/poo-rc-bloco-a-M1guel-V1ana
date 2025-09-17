class Towel:
    def __init__(self):
        self.color : str = ""
        self.size : str = ""
        self.wetness : int = 0 

minha = Towel()
minha.color = "rosinha "
minha.size = "G"

hellys = Towel()
hellys.color = "vermelha"
hellys.size = "M"

print(f"a cor da sua toalha é {hellys.color}")
