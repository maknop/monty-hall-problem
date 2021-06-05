"""
TODO: Documentation
"""
from assumptions.player_switches_door import PlayerSwitchesDoor
from assumptions.player_doesnt_switch_door import PlayerDoesntSwitchDoor
from assumptions.host_randomly_picks import HostRandomlyPicks
import random


def main():
    instruction()
    userAssumptionChoice = input('Choose which assumption to view\n> ')

"""
Creates initial options for the user to view the game under a different set
of assumptions. 
"""
def instruction():
    print(f'\nMonty Hall Problem!\n'
         + 'Assumptions:\n'
         + '1. Player switches door after Monty chooses an incorrect door\n'
         + '2. Player does not switch doors after Monty chooses an incorrect door\n'
         + '3. Monty chooses door randomly (Could be the winning option\n')
   
if __name__ == '__main__':
    main()
