from random import choice

class Forca_jogo():
    def __init__(self):
        self.x = choice(["Martelo","Abelha","Aviação"])
        self.palavra_secreta = "".join(["_." for i in self.x])
        self.b = self.palavra_secreta.split('.')
        self.b.pop(-1)
    
    def Verifica(self, jogada):
        if jogada in self.x:            
            for indice, letra in enumerate(list(self.x)):
                if jogada.lower() == letra.lower():
                    if letra.isupper():
                        self.b[indice] = jogada.upper()
                    else:
                        self.b[indice] = jogada
            return "".join([i+"." for i in self.b])
        else:
            print("\n Errou!")
            return "".join([i+"." for i in self.b])

def main():
    forca = Forca_jogo()
    while True:  
        secret = forca.Verifica(input("Digite uma letra: "))
        if secret.replace(".","") == forca.x:
            print(f"\n Você ganhou!")
            print(secret)
            break
        print(f"\n {secret}")
main()
