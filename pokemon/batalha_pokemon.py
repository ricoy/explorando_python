from random import randint
from abc import ABC, abstractmethod

'''
Escrevi este programa para explorar alguns recursos da linguagem Python
e ao mesmo tempo se aproximar do mundo dos meus filhos (dai o tema Pokemon rs) 
para ver se eles comecam a se interessar por programacao. 
Fiquem a vontade para divulgar, melhorar e se quiser podem xingar tb rs
so nao se esquecam de dar os creditos ok?.
'''

__author__ = "Rodrigo Ricoy Marques"

'''
Classe responsavel por definir os atributos e metodos padroes de um Pokemon
'''
class Pokemon(ABC):

    ENERGIA_GOLPE_ESPECIAL = 10
    AUMENTO_FORCA_ATAQUE_ESPECIAL = 0.50

    def __init__(self, nome_pokemon, ataque, defesa):
        self.__nome = nome_pokemon
        self.__ataque = ataque
        self.__defesa = defesa
        self.__energia_golpe_especial = 0
    
    @property
    def nome(self):
        return self.__nome

    @property
    def ataque(self):
        return self.__ataque

    @property
    def defesa(self):
        return self.__defesa          
    
    def atualizar_dano(self, forca_ataque):
        if (forca_ataque < self.defesa):
            self.__defesa -= forca_ataque
        else:
            self.__defesa = 0

        return self.__defesa
    
    @abstractmethod
    def golpe_especial(self):
        pass
        
    def acumular_energia_golpe_especial(self):
        self.__energia_golpe_especial += 2
    
    def defender(self):
        return (randint(0, 1) == 1)
    
    def possui_energia_ataque_especial(self):
        return (self.__energia_golpe_especial == self.ENERGIA_GOLPE_ESPECIAL)

    def calcular_dano_ataque(self):
        if (self.possui_energia_ataque_especial()):
            return self.__ataque + int(self.__ataque * self.AUMENTO_FORCA_ATAQUE_ESPECIAL)
        else:
            return self.__ataque                

    def atacar(self, pokemon_adversario):        
        dano = self.calcular_dano_ataque()
        if (not pokemon_adversario.defender()):
            defesa_antes_ataque = pokemon_adversario.__defesa;
            defesa_restante = pokemon_adversario.atualizar_dano(dano)            
            if (self.possui_energia_ataque_especial()):
                print('{}[{}/{}] atacou {}[{}/{}] com golpe especial'.format(self.__nome, str(dano), str(self.__defesa), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(defesa_antes_ataque)))
                self.golpe_especial()
                self.__energia_golpe_especial = 0                
            else:
                print('{}[{}/{}] atacou {}[{}/{}]'.format(self.__nome, str(dano), str(self.__defesa), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(defesa_antes_ataque)))
            
            self.acumular_energia_golpe_especial()            
            ataque_foi_fatal = (defesa_restante <= 0)
        
            if (ataque_foi_fatal):
                print('  * {} perdeu {} pontos de defesa. {}[{}/{}]'.format(pokemon_adversario.__nome, str(dano), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(defesa_restante)))
                print('\nFim de partida\nO Pokemon {} venceu'.format(self.__nome))
                return -1
            else:
                print('  * {} perdeu {} pontos de defesa. {}[{}/{}]'.format(pokemon_adversario.__nome, str(dano), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(defesa_restante)))
                return defesa_restante
        else:
            print('{}[{}/{}] atacou {}[{}/{}]'.format(self.__nome, str(dano), str(self.__defesa), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(pokemon_adversario.defesa)))
            print('  * {} errou o golpe :-('.format(self.__nome))
            return 0
        
'''
Especializacao da classe Pokemon de um Pikachu
'''
class Pikachu(Pokemon):
    def __init__(self, id_jogador):
        nome_pokemon = __class__.__name__ + id_jogador
        super().__init__(nome_pokemon, ataque = 7, defesa = 60)

    def golpe_especial(self):
        super().golpe_especial()
        print('  [!] Choque do trovao dzzzzzzzzzzzzzzz aahhhhhhhhh buuuuuuuuuuu trum cabum')

'''
Especializacao da classe Pokemon de um Charizard
'''
class Charizard(Pokemon):
    def __init__(self, id_jogador):
        nome_pokemon = __class__.__name__ + id_jogador
        super().__init__(nome_pokemon, ataque = 10, defesa = 40)

    def golpe_especial(self):
        super().golpe_especial()
        print('  [!] Garras de dragão fuuuoooooozzzzzzz trazzzzz raaaz raaaz fuol bum')

'''
Especializacao da classe Pokemon de um Bulbasaur
'''        
class Bulbasaur(Pokemon):
    def __init__(self, id_jogador):
        nome_pokemon = __class__.__name__ + id_jogador
        super().__init__(nome_pokemon, ataque = 5, defesa = 80)

    def golpe_especial(self):
        super().golpe_especial()
        print('  [!] Chazam bam bim bom bum trazzzzzz kazum')

'''
Especializacao da classe Pokemon de um Akuma 
tudo bem q o Akuma nao eh um pokemon, mas nao podia deixar de ter ele rs
'''        
class Akuma(Pokemon):
    def __init__(self, id_jogador):
        nome_pokemon = __class__.__name__ + id_jogador
        super().__init__(nome_pokemon, ataque = 8, defesa = 50)

    def golpe_especial(self):
        super().golpe_especial()
        print('  [!] Haaaaaaaadooouuuukeeeennnn!!!! pow pow pow puff big bang')

'''
Especializacao da classe Pokemon de um John Wick 
Esse eh bom de briga rs
'''        
class JohnWick(Pokemon):
    def __init__(self, jogador):
        nome_pokemon = __class__.__name__ + jogador
        super().__init__(nome_pokemon, ataque = 11, defesa = 35)

    def golpe_especial(self):
        super().golpe_especial()
        print('  [!] Ahhhhhh eu to muito maluco e vou te pegar seu filho da p*!!!! pow soc puf taz bang')        

'''
Classe que controla a batalha de pokemons entre dois jogadores
'''        
class Batalha:
    def __init__(self, pokemon_1, pokemon_2):
        print('\nLuta: {}[{}/{}] vs {}[{}/{}]'.format(pokemon_1.nome, pokemon_1.ataque, pokemon_1.defesa, pokemon_2.nome, pokemon_2.ataque, pokemon_2.defesa))
        
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.vencedor = False
        self.__rodada = 1
        
    def lutar(self):
        print('\n[Round {}]'.format(str(self.__rodada)))
        
        pokemons = (self.pokemon_1, self.pokemon_2)
        
        # adicionando mais emocao no jogo colocando o atacante e o defensor variavel em cada rodada
        indice_pokemon_ataque = randint(0, 1)
        indice_pokemon_defesa = 1 - indice_pokemon_ataque

        self.__rodada += 1

        pokemon_ataque = pokemons[indice_pokemon_ataque]
        pokemon_defesa = pokemons[indice_pokemon_defesa]
        
        # se o ataque de um dos jogadores foi fatal fim de jogo, senao continua a briga
        if (pokemon_ataque.atacar(pokemon_defesa) < 0 or pokemon_defesa.atacar(pokemon_ataque) < 0): 
            return False
        else:
            return True

'''
Classe que abstrai a criacao de pokemons
'''
class FabricaPokemon:
    
    @staticmethod
    def criar_pokemon(tipo_pokemon, jogador):
        string_jogador = ' P' + str(jogador)
        if (tipo_pokemon == 1):
            return Pikachu(string_jogador)
        elif (tipo_pokemon == 2):
            return Charizard(string_jogador)
        elif (tipo_pokemon == 3):
            return Bulbasaur(string_jogador)
        elif (tipo_pokemon == 4):
            return JohnWick(string_jogador)
        elif (tipo_pokemon == 0):
            return Akuma(string_jogador)

        raise ValueError('Pokemon inválido')

'''
Classe que controla o game, exibindo as opcoes de pokemons para os usuarios
e da o inicio a batalha. Cada Pokemon tem atributos de ataque, que sera utilizado
para retirar pontos de defesa do adversario e vice-versa. Para dificultar o resultado
o golpe pode ou nao acertar o adversario em cada rodada. Ganha quem acertar mais e conseguir
zerar a defesa do outro primeiro. Animado para uma batalha? Que comecem os jogos :-)
'''
class PokemonGame:
    @staticmethod
    def __obter_pokemon_usuario(jogador):                    
            while(True):
                try:
                    opcao_usuario = int(input("Jogador {}\nEscolha seu Pokemon: \n[0] - Akuma\n[1] - Pikachu\n[2] - Charizard\n[3] - Bulbasaur\n[4] - John Wick\n=> ".format(jogador)))
                    if (opcao_usuario >= 0 and opcao_usuario <= 4):
                        return FabricaPokemon.criar_pokemon(opcao_usuario, jogador)
                except Exception as e:
                    print('Ops algo nao funcionou como devia...')
                    print(e)  
                    print(e.with_traceback())          
                    continue        
    
    @staticmethod
    def iniciar_game():
        pokemon_usuario_1 = PokemonGame.__obter_pokemon_usuario(1)
        pokemon_usuario_2 = PokemonGame.__obter_pokemon_usuario(2)
        batalha = Batalha(pokemon_usuario_1, pokemon_usuario_2)
        while(True):
            if (not batalha.lutar()):
                break
        
if __name__ == '__main__':
  PokemonGame.iniciar_game()  


        
        


