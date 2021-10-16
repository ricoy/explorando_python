import random
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
        self.__defesa -= forca_ataque
        return self.__defesa
    
    @abstractmethod
    def golpe_especial(self):
        pass
        
    def encher_energia_golpe_especial(self):
        self.__energia_golpe_especial += 2
    
    def defender(self):
        return (random.randint(0, 1) == 1)
    
    def atacar(self, pokemon_adversario):
        adversario_defendeu = pokemon_adversario.defender()
        dano = self.__ataque
        
        self.encher_energia_golpe_especial()
        
        if (not adversario_defendeu):
            possui_golpe_especial = (self.__energia_golpe_especial == 10)
            
            if (possui_golpe_especial):
                dano += self.__energia_golpe_especial
                self.__energia_golpe_especial = 0
                self.golpe_especial()
            else:
                print('{}[{}/{}] atacou {}[{}/{}]'.format(self.__nome, str(dano), str(self.__defesa), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(pokemon_adversario.defesa)))
                
            defesa_restante = pokemon_adversario.atualizar_dano(dano)
            
            ataque_foi_fatal = (defesa_restante <= 0)
        
            if (ataque_foi_fatal):
                print('\nFim de partida\nO Pokemon {} venceu'.format(self.__nome))
                return True
            else:
                print('  * {} perdeu {} pontos de defesa. {}[{}/{}]'.format(pokemon_adversario.__nome, str(dano), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(defesa_restante)))
                return False
        else:
            print('{}[{}/{}] atacou {}[{}/{}]'.format(self.__nome, str(dano), str(self.__defesa), pokemon_adversario.__nome, str(pokemon_adversario.ataque), str(pokemon_adversario.defesa)))
            
            print('  * {} errou o golpe :-('.format(self.__nome))
            dano = 0
            return False
        
'''
Especializacao da classe Pokemon de um Pikachu
'''
class Pikachu(Pokemon):
    def golpe_especial(self):
        super().golpe_especial()
        print('Choque do trovao dzzzzzzzzzzzzzzz aahhhhhhhhh buuuuuuuuuuu trum cabum')

'''
Especializacao da classe Pokemon de um Charizard
'''
class Charizard(Pokemon):
    def golpe_especial(self):
        super().golpe_especial()
        print('Garras de dragão fuuuoooooozzzzzzz trazzzzz raaaz raaaz fuol bum')

'''
Especializacao da classe Pokemon de um Bulbasaur
'''        
class Bulbasaur(Pokemon):
    def golpe_especial(self):
        super().golpe_especial()
        print('Chazam bam bim bom bum trazzzzzz kazum')

'''
Especializacao da classe Pokemon de um Akuma 
tudo bem q o Akuma nao eh um pokemon, mas nao podia deixar de ter ele rs
'''        
class Akuma(Pokemon):
    def golpe_especial(self):
        super().golpe_especial()
        print('Haaaaaaaadooouuuukeeeennnn!!!! pow pow pow puff big bang')

'''
Classe que controla a batalha de pokemons entre dois jogadores
'''        
class Batalha:
    def __init__(self, pokemon_1, pokemon_2):
        print('\nLuta: {}[{}/{}] vs {}[{}/{}]'.format(pokemon_1.nome, pokemon_1.ataque, pokemon_1.defesa, pokemon_2.nome, pokemon_2.ataque, pokemon_2.defesa))
        
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.vencedor = False
        self.rodada = 1
        
    def lutar(self):
        print('\n[Round {}]'.format(str(self.rodada)))
        
        self.rodada += 1
        
        pokemon_ataque = self.pokemon_1
        pokemon_defesa = self.pokemon_2
        
        # se o ataque de um dos jogadores nao foi fatal a luta continua, senao ha um vencedor
        if (pokemon_ataque.atacar(pokemon_defesa) or pokemon_defesa.atacar(pokemon_ataque)): 
            return True
        
        return False

'''
Classe que abstrai a criacao de pokemons
'''
class FabricaPokemon:
    
    @staticmethod
    def criar_pokemon(tipo_pokemon, jogador):
        string_jogador = ' P' + str(jogador)
        if (tipo_pokemon == 1):
            return Pikachu('Pikachu' + string_jogador, 7, 60)
        elif (tipo_pokemon == 2):
            return Charizard('Charizard' + string_jogador, 10, 40)
        elif (tipo_pokemon == 3):
            return Bulbasaur('Bulbasaur' + string_jogador, 5, 80)
        elif (tipo_pokemon == 0):
            return Akuma('Akuma' + string_jogador, 8, 50)

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
    def obter_pokemon_usuario(jogador):                    
            while(True):
                try:
                    opcao_usuario = int(input("Jogador {}\nEscolha seu Pokemon: \n[1] - Pikachu\n[2] - Charizard\n[3] - Bulbasaur\n[0] - Akuma\n=> ".format(jogador)))
                    if (opcao_usuario in [0, 1, 2, 3]):
                        return FabricaPokemon.criar_pokemon(opcao_usuario, jogador)
                except Exception as e:
                    print('Ops algo nao funcionou como devia...')
                    print(e)  
                    print(e.with_traceback())          
                    continue        
    
    @staticmethod
    def iniciar_game():
        pokemon_usuario_1 = __class__.obter_pokemon_usuario(1)
        pokemon_usuario_2 = __class__.obter_pokemon_usuario(2)
        batalha = Batalha(pokemon_usuario_1, pokemon_usuario_2)
        while(True):
            if (batalha.lutar()):
                break
        
if __name__ == '__main__':
  PokemonGame.iniciar_game()  


        
        


