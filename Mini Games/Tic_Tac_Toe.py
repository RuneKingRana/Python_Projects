import tkinter as tk
import random
import time
from tkinter import ttk

def start_game(mode):
    global game_mode, current_chr
    game_mode = mode
    current_chr = 'X'
    menu_frame.pack_forget()
    game_frame.pack()
    reset_game()

def quit_game():
    root.quit()

def reset_game():
    global current_chr
    current_chr = 'X'
    for button in buttons:
        button.config(text="", state=tk.NORMAL, bg="#f0f0f0")
    status_label.config(text="X's turn", fg="#0000ff",bg="#f9f64b")
    play_again_button.pack_forget()
    quit_button.pack_forget()

def animate_button(button, player):
    button.config(bg="#0070ff" if player == 'X' else "#ff007f")
    root.update()
    time.sleep(0.2)
    button.config(bg="#f0f0f0")

def check_win():
    for combo in win_combinations:
        values = [buttons[i]['text'] for i in combo]
        if values[0] == values[1] == values[2] and values[0] in ('X', 'O'):
            status_label.config(text=f"{values[0]} wins!", fg="#ff033e")
            for i in combo:
                buttons[i].config(state=tk.DISABLED, bg="#ff6700")
            play_again_button.pack()
            quit_button.pack()
            return True
    if all(button['text'] in ('X', 'O') for button in buttons):
        status_label.config(text="Draw!", fg="#ff033e")
        play_again_button.pack()
        quit_button.pack()
        return True
    return False

def button_click(i):
    global current_chr
    if buttons[i]['text'] == "":
        animate_button(buttons[i], current_chr)
        buttons[i].config(text=current_chr, fg="black")
        if check_win():
            return
        current_chr = 'O' if current_chr == 'X' else 'X'
        status_label.config(text=f"{current_chr}'s turn", fg="#0000ff",bg="#f9f64b")
        if game_mode == "computer" and current_chr == 'O':
            root.after(500, computer_move)

def computer_move():
    empty_buttons = [i for i in range(9) if buttons[i]['text'] == ""]
    for combo in win_combinations:
        values = [buttons[i]['text'] for i in combo]
        if values.count('O') == 2 and values.count('') == 1:
            button_click(combo[values.index('')])
            return
    for combo in win_combinations:
        values = [buttons[i]['text'] for i in combo]
        if values.count('X') == 2 and values.count('') == 1:
            button_click(combo[values.index('')])
            return
    if 4 in empty_buttons:
        button_click(4)
        return
    for move in [0, 2, 6, 8]:
        if move in empty_buttons:
            button_click(move)
            return
    button_click(random.choice(empty_buttons))

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)
root.configure(bg="#d3d3d3")

menu_frame = tk.Frame(root, bg="#d3d3d3")
tk.Label(menu_frame, text="Tic Tac Toe", font=('Ariel', 20), bg="#fefe12").pack()
tk.Button(menu_frame, text="Play Offline", font=('Ariel', 15), bg="#ff00ff", command=lambda: start_game("offline")).pack()
tk.Button(menu_frame, text="Play with Computer", font=('Ariel', 15), bg="#00ffff", command=lambda: start_game("computer")).pack()
menu_frame.pack()

game_frame = tk.Frame(root, bg="#fefe12")
status_label = tk.Label(game_frame, text="X's turn", font=('Ariel', 15), bg="#d3d3d3", fg="blue")
status_label.pack()

button_frame = tk.Frame(game_frame, bg="#ff9f00")
button_frame.pack()

buttons = [tk.Button(button_frame, text="", font=('Ariel', 20), width=5, height=2, bg="#ff9f00", command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

play_again_button = tk.Button(game_frame, text="Play Again", font=('Ariel', 15), bg="#f400a1", command=reset_game)
quit_button = tk.Button(game_frame, text="Quit", font=('Ariel', 15), bg="#00bfff", command=quit_game)

win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

game_frame.pack_forget()
root.mainloop()