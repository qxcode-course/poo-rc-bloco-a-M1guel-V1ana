class Carro:
    def __init__(self, passa: int =0, gas:int = 0, km:int = 0):
        self.passa: int = 0
        self.gas :int = 0
        self.km :int = 0

    def __str__(self) -> str:
        return f"pass: {self.passa}, gas: {self.gas}, km: {self.km}"

        
    def maxPassa(self):
        self.passa += 1
        if self.passa >2:
            self.passa = 2
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.passa >0:
            self.passa -= 1
        else:    
             print("fail: nao ha ninguem no carro")    
    
    def gasMax(self, incremnt : int ):
        self.gas += incremnt
        if self.gas > 100:
            self.gas = 100
     


    def drive(self, distance : int ):
        if self.passa == 0:
            print("fail: nao ha ninguem no carro ")
        elif self.gasMax == 0:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0 
        else:
            self.km += distance
            self.gas -= distance 



def main():
    carro: Carro = Carro("", "", 0)
    
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        
        
        if args[0]=="end":
            break
        elif args[0]=="enter":
            carro.maxPassa()
        elif args[0]=="show":
            print(carro)
        elif args[0]=="leave":
            carro.leave()
        elif args[0]=="fuel":
            increment = int(args[1])
            carro.gasMax(ncrement)
        elif args[0]=="drive":
            increment= int(args[1])
            carro.drive(increment)
                


 
 
 
 
main()           