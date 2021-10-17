from unittest import TestCase
from unittest.mock import MagicMock

from ..pokemon.batalha_pokemon import Akuma, Bulbasaur, Pikachu, Pokemon

class TestPokemon(TestCase):
    
    def test_verifica_dano_pos_ataque_pokemon(self):
        pikachu = Pikachu('P1')
        akuma = Akuma('P2')
        akuma.defender = MagicMock(return_value = 0)
        dano = pikachu.atacar(akuma)
        defesa_pos_ataque = akuma.defesa
        self.assertEqual(defesa_pos_ataque, dano)
    
    def test_verifica_dano_pos_defesa_ataque_pokemon(self):
        pikachu = Pikachu('P1')
        akuma = Akuma('P2')
        akuma.defender = MagicMock(return_value = 1)
        dano = pikachu.atacar(akuma)
        self.assertEqual(0, dano)
    
    def test_dano_ataque_especial(self):
        pikachu = Pikachu('P1')
        bulbasaur = Bulbasaur('P2')
        bulbasaur.defender = MagicMock(return_value = 0)
       
        dano_golpe_especial = pikachu.ataque + int(pikachu.ataque * Pokemon.AUMENTO_FORCA_ATAQUE_ESPECIAL)
        pikachu.atacar(bulbasaur)
        pikachu.atacar(bulbasaur)
        pikachu.atacar(bulbasaur)
        pikachu.atacar(bulbasaur)
        defesa_antes_golpe_especial = bulbasaur.defesa
        pikachu.atacar(bulbasaur)
        defesa_pos_golpe_especial = bulbasaur.defesa

        self.assertEqual(defesa_pos_golpe_especial,  defesa_antes_golpe_especial - dano_golpe_especial)
    
    def test_verifica_pokemon_morreu_pos_ataque_fatal(self):
        pikachu = Pikachu('P1')
        akuma = Akuma('P2')
        akuma.atualizar_dano = MagicMock(return_value = 0)
        dano = pikachu.atacar(akuma)
        self.assertEqual(-1, dano)

if __name__ == '__main__':
    TestPokemon()