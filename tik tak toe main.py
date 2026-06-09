from tkinter import *
import random

screen = Tk()
screen.title('BASSETs tic tac toe game')

def next_turn(row, column):
   global choice_player
   if buttons[row][column]['text'] == '' and win() == False:
       if choice_player == players[0]:
           buttons[row][column]['text'] = choice_player
           
           if win() == False:
               choice_player = players[1]
               player_turn_label.config(text=(choice_player + ' turn'))
           elif win() == True:
               player_turn_label.config(text=(players[0] + ' wins!'))
           elif win() == 'tie':
               player_turn_label.config(text=('tie')) 
        
       elif choice_player == players[1]:
           buttons[row][column]['text'] = choice_player
           
           if win() == False:
               choice_player = players[0]
               player_turn_label.config(text=(choice_player + ' turn'))
           elif win() == True:
               player_turn_label.config(text=(players[1] + ' wins!'))
           elif win() == 'tie':
               player_turn_label.config(text=('tie')) 
                    
def win():
    for row in range(3):
         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
              buttons[row][0].config(bg='green')
              buttons[row][1].config(bg='green')
              buttons[row][2].config(bg='green')
              return True
            
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
          buttons[0][0].config(bg='green')
          buttons[1][1].config(bg='green')
          buttons[2][2].config(bg='green')
          return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    
    if check_spaces() == False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='red')
        return 'tie'
    else:
        return False

def check_spaces():
   spaces = 9
   for row in range(3):
       for column in range(3):
           if buttons[row][column]['text'] != '':
              spaces -= 1
   if spaces == 0:
        return False
   else:
        return True

def restart():
    global choice_player
    choice_player = random.choice(players)
    player_turn_label.config(text=(choice_player) + ' turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg='#F0F0F0')
            

players = ['x', 'o']
choice_player = random.choice(players)
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

player_turn_label = Label(text=(choice_player + ' Turn'), font=('Cairo', 35))
player_turn_label.pack(side='top')

restart_button = Button(text='restart', font=('Cairo', 35), command=restart)
restart_button.pack(side='top')

buttons_frame = Frame(screen)
buttons_frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(buttons_frame, text='', font=('Cairo', 40), width=4, height=1,
        command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

screen.mainloop()