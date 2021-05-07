import pygame    
from random import randint

def computer():
    computer = randint(0,2)
    # computer = {
    #     if computer == 0:
    #         computer = "đấm"
    #     if computer == 1:
    #         computer = "lá"
    #     else:
    #         computer = "kéo"
    # }
    print(computer)

def player():
    player = int(input("Nhập: "))

def ss():
    if computer.computer() == player.player():
        print("Hi")
    


computer()
player()
ss()
