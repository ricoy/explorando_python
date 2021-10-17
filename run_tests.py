'''
Para executar os testes executar este arquivo da seguinte forma:
python -m unittest run_tests.py
'''
from unittest import TestSuite, TextTestRunner, makeSuite
import pokemon_game.tests.batalha_pokemon_test as test

def suite():
    suite = TestSuite()
    suite.addTest(makeSuite(test.TestPokemon))
    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(suite())