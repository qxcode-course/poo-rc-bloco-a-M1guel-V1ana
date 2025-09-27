class Calculadora:
    def __init__(self,  batteryMax: int, baterry : int, display ):
        self.display: float = 0.0
        self.batteryMax: int = 0

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.batteryMax}"
    

    def charge(self, increment: int) -> None:
        self.batteryMax += increment 

        if self.batteryMax >5:
            self.batteryMax = 5 
        


def main():

    calculadora: Calculadora = Calculadora("", "")
    while True:

        line: str = input()
        print("$" +  line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax: int = args[1]
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "charge":
            calculadora.charge(int(args[1]))

main()
