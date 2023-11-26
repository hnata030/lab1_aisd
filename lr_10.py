"""
Хабарова Наталья ИСТбд-21
Крестики-нолики
"""

import tkinter as tk
from tkinter import messagebox
import random

#Создаем пустое игровое поле
board = [' ' for _ in range(9)]
player = 'X'
computer = 'О'

#Все выигрышные комбинации
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # Горизонтальные
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # Вертикальные
    [0, 4, 8], [2, 4, 6]             # Диагональные
]

#Проверка всех возможных комбинаций
def winner(board, player):
    return any(all(board[i] == player for i in combination) for combination in winning_combinations)

#Проверка заполнения поля
def board_full(board):
    return ' ' not in board

#Обработка ходов пользователя и компьютера
def make_move(move):
    if board[move] != ' ':
        return
    board[move] = player
    buttons[move].config(text=player)
    if winner(board, player):
        highlight_winning_combination(player, 'chartreuse1')
        messagebox.showinfo('Победа!', 'Вы победили!')
        reset_game()
    elif board_full(board):
        highlight_draw()
        messagebox.showwarning('Ничья!', 'Вы сыграли вничью!')
        reset_game()
    else:
        computer_move = get_computer_move()
        if computer_move is not None:
            board[computer_move] = computer
            buttons[computer_move].config(text=computer)
            if winner(board, computer):
                highlight_winning_combination(computer, 'firebrick2')
                messagebox.showerror('Поражение!', 'Компьютер победил!')
                reset_game()

#Ход компьютера
def get_computer_move():
    possible_moves = [i for i, x in enumerate(board) if x == ' ']
    for move in possible_moves:
        board_copy = board[:]
        board_copy[move] = computer
        if winner(board_copy, computer):
            return move
    for move in possible_moves:
        board_copy = board[:]
        board_copy[move] = player
        if winner(board_copy, player):
            return move
    corners = [0, 2, 6, 8] #углы
    available_corners = [corner for corner in corners if corner in possible_moves]
    if available_corners:
        return random.choice(available_corners)
    if 4 in possible_moves:
        return 4
    edges = [1, 3, 5, 7] #края
    available_edges = [edge for edge in edges if edge in possible_moves]
    if available_edges:
        return random.choice(available_edges)
    return None

#Сброс игры после окончания
def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ', bg='CadetBlue1')

#Вывод цвета на выигрышной комбинации
def highlight_winning_combination(player, color):
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            for index in combination:
                buttons[index].config(bg=color)
            break

#Ничья
def highlight_draw():
    for button in buttons:
        button.config(bg='gold1')

root = tk.Tk()
root.title('Крестики-нолики')
root.resizable(False, False)
buttons = []
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

#Кнопки игрового поля
for i in range(9):
    button = tk.Button(root, text=' ', bg='CadetBlue1', font=('Courier New', 14), width=8, height=4, command=lambda move=i: make_move(move))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)
    
#Кнопка новой игры
new_button = tk.Button(root, text='Начать новую игру', command=reset_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

root.mainloop()
