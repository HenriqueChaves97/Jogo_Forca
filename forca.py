from random import choice

class Forca_jogo():
    def __init__(self):
        self.x = choice(["Martelo","Abelha","Aviação"])
        self.palavra_secreta = "".join(["_." for i in self.x]).lower()
        self.b = self.palavra_secreta.split('.')
        self.b.pop(-1)
    
    def Verifica(self, jogada):
        if jogada in self.x:
            for indice, letra in enumerate(list(self.x)):
                if jogada == letra:
                    self.b[indice] = jogada
            # print(self.x,''.join(self.b))
            print(self.b)
            if self.x ==''.join(self.b):
                print('parabén vc acertou!',self.x)
                return 0
        else:
            print('não contem a letra: ',jogada)
        return "".join([i+"." for i in self.b])

def main():
    forca = Forca_jogo()
    while forca.Verifica(input("Digite uma letra: ").lower().strip()): pass
main()
