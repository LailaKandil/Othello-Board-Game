import tkinter as tk
from Game import Game
from Player import Player
from Board import Board
from GUI import OthelloGUI

if __name__ == "__main__":

    root = tk.Tk()
    board = Board()
    colours = ['B', 'W']
    Players = {}
    print("Welcome to the game!\n")
    for i in range(2):
        print("Player " + str(i + 1) + " please enter your name:")
        name = str(input())
        player = Player(colours[i], name)
        Players[colours[i]] = player
        print(f"Player {str(i + 1)}'s name: {player.name}\nPlayer {str(i + 1)}'s color: {player.color}")

    game = Game(board, Players['B'], Players['W'])
    gui = OthelloGUI(root, game)
    root.mainloop()
