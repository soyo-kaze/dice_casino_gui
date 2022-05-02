from Tkinter import *
from random import randint
import tkMessageBox

class Casino(object):
    def __init__(self):
        self.window_start = Tk()
        self.window_start.title("DICE CASINO")
        self.window_start.iconbitmap(r'.\Radiation.ico')
        
        self.frame_upper = Frame(self.window_start, width=100, height=50)
        self.frame_upper_1 = Frame(self.window_start, width=50, height=100)
        self.frame_upper_2 = Frame(self.window_start, width=50, height=100)
        self.frame_upper_3 = Frame(self.window_start, width=100, height=30)

        self.name = Entry(self.window_start)
        self.cost = Entry(self.window_start)

        self.play = Button(self.window_start, text="Play", command=self.game_start_decider, width=10, bg="grey")
        self.exit_btn = Button(self.window_start, text="Exit", command=self.window_start.destroy, width=10, bg="grey")

    def name_onclick(self, x):
        if self.name.get() == "  Name":
            self.name.delete(0, 'end')
            self.name.insert(0, "")
            self.name.config(bg="grey", fg="black")

    def bet_onclick(self, x):
        if self.bet.get() == "  Bet":
            self.bet.delete(0, 'end')
            self.bet.insert(0, "")
            self.bet.config(bg="grey", fg="black")

    def guess1_onclick(self, x):
        if self.guess_1.get() == "  1st Guess":
            self.guess_1.delete(0, 'end')
            self.guess_1.insert(0, "")
            self.guess_1.config(bg="grey", fg="black")

    def guess2_onclick(self, x):
        if self.guess_2.get() == "  2nd Guess":
            self.guess_2.delete(0, 'end')
            self.guess_2.insert(0, "")
            self.guess_2.config(bg="grey", fg="black")

    def name_watermark(self, y):
        if self.name.get() == "" or self.name.get() == " ":
            self.name.delete(0, "end")
            self.name.insert(0, "  Name")
            self.name.config(bg="white", fg="grey")

    def bet_watermark(self, y):
        if self.bet.get() == "" or self.bet.get() == " ":
            self.bet.delete(0, "end")
            self.bet.insert(0, "  Bet")
            self.bet.config(bg="white", fg="grey")

    def guess1_watermark(self, y):
        if self.guess_1.get() == "" or self.guess_1.get() == " ":
            self.guess_1.delete(0, "end")
            self.guess_1.insert(0, "  1st Guess")
            self.guess_1.config(bg="white", fg="grey")

    def guess2_watermark(self, y):
        if self.guess_2.get() == "" or self.guess_2.get() == " ":
            self.guess_2.delete(0, "end")
            self.guess_2.insert(0, "  2nd Guess")
            self.guess_2.config(bg="white", fg="grey")

    def cost_onclick(self, b):
        if self.cost.get() == "  $$$":
            self.cost.delete(0, 'end')
            self.cost.insert(0, "")
            self.cost.config(bg="grey", fg="green")

    def cost_watermark(self, a):
        if self.cost.get() == "" or self.cost.get() == " ":
            self.cost.delete(0, "end")
            self.cost.insert(0, "  $$$")
            self.cost.config(bg="white", fg="lightgreen")
        
    def game_ongoing_decider(self):
        self.random_no = randint(1,6)
        self.dice.config(text=self.random_no)
        
        if self.bet.get().isalpha() == True or self.guess_1.get().isalpha() == True or self.guess_2.get().isalpha() == True:
            self.bet.delete(0, "end")
            tkMessageBox.showwarning("Error!!", "In our world these values are in digits!!")
            
        elif self.bet.get().isalpha() == False or self.guess_1.get().isalpha() == False or self.guess_2.get().isalpha() == False:
            if self.bet.get().isdigit() != True or self.guess_1.get().isdigit() != True or self.guess_2.get().isdigit() != True:
                self.bet.delete(0, "end")
                tkMessageBox.showwarning("Error!!", "Blanks are not allowed!!")
        self.lastbet = int(self.bet.get())
        
        if int(self.lastbet) == int(self.bet.get()):
            if int(self.lastbet) > int(self.money):
                self.bet.delete(0, "end")
                tkMessageBox.showwarning("Money Alert", "Hey!! keep an eye on ur wallet!!")
                
            elif int(self.lastbet) <= int(self.money)  and int(self.lastbet) > 0 :
                if int(self.guess_1.get()) in range(1,7):
                    if int(self.guess_2.get()) in range(1,7):
                        if int(self.guess_2.get()) == int(self.random_no) or int(self.guess_1.get()) == int(self.random_no):
                            self.money = int(self.money) + (2*int(self.lastbet))
                            tkMessageBox.showinfo("WINNER WINNER CHICKEN DINNER!!", "CONGO!! YOU WON!!")
                            self.money_label.config(text="Money:" + str(self.money) + "$    Last bet:" + str(self.lastbet))
                            self.bet.delete(0, "end")
                            self.guess_1.delete(0, "end")
                            self.guess_2.delete(0, "end")
                            
                        else:
                            self.money = int(self.money) - int(self.lastbet)
                            tkMessageBox.showinfo("LOSER LOSER BULL-DOZER!!", "SORRY!! YOU REALLY HAVE A GREAT BAD-LUCK!!")
                            self.money_label.config(text="Money:" + str(self.money) + "$    Last bet:" + str(self.lastbet))
                            self.bet.delete(0, "end")
                            self.guess_1.delete(0, "end")
                            self.guess_2.delete(0, "end")
                            
                    else:
                        tkMessageBox.showwarning("Guess Alert!!", "dice doesn't have "+ str(self.guess_2.get())+" on it")
                        self.guess_2.delete(0, "end")
                        
                else:
                    tkMessageBox.showwarning("Guess Alert!!", "dice doesn't have "+ str(self.guess_1.get())+" on it")
                    self.guess_1.delete(0, "end")
                    
            elif int(self.lastbet) == 0:
                if int(self.lastbet) == int(self.money):
                    self.bet.delete(0, "end")
                    tkMessageBox.showwarning("Money Alert", "You're broke as AF!!")
                else:
                    self.bet.delete(0, "end")
                    tkMessageBox.showwarning("Money Alert", "Don't try trick us!!")
                
            elif int(self.lastbet) < 0:
                self.bet.delete(0, "end")
                tkMessageBox.showwarning("Money Alert", "We don't trade in negatives!!")
            
    def game_start_decider(self):
        if self.cost.get().isalpha() == True :
            self.cost.delete(0, "end")
            tkMessageBox.showwarning("Error!!", "In our world these values are in digits!!")
        elif self.name.get() == "  Name" or self.cost.get().isdigit() == False:
            self.name.delete(0, "end")
            self.cost.delete(0, "end")
            tkMessageBox.showwarning("Error!!", "Blanks are not allowed!!")
        else:
            self.game_ongoing()

    def game_ongoing(self):
        self.window_game = Tk()
        self.window_game.title("DICE CASINO")
        self.window_game.geometry("400x250")
        self.window_game.iconbitmap(r'.\Radiation.ico')

        
        if self.cost.get().isdigit() == True:
            self.money = int(self.cost.get())
        elif self.cost.get().isalpha() == True:
            self.money = self.cost.get()      
        
        self.frame_up = Frame(self.window_game, width=400, height=50)
        self.frame_up.grid(column=0,columnspan=2, row=2)

        self.name = self.name.get()
        self.money = self.cost.get()

        self.name_label = Label(self.window_game, text=str(self.name)+"  ", relief=SUNKEN, anchor=E)
        self.name_label.grid(column=0,columnspan=2, row=0, sticky=W+E)

        self.money_label = Label(self.window_game, text="Money:" + str(self.money) + "$    Last bet:", relief=SUNKEN, anchor=E)
        self.money_label.grid(column=0,columnspan=2, row=1, sticky=W+E)

        self.label_down=Frame(self.window_game, width=200, height=50)
        self.label_down.grid(column=0, row=3)

        self.label_down_1 = Frame(self.window_game, width=200, height=50)
        self.label_down_1.grid(column=1, row=3)

        self.bet=Entry(self.label_down, width=15)
        self.bet.grid(column=0, row=0, pady=5)
        self.bet.bind('<FocusIn>', self.bet_onclick)
        self.bet.bind('<FocusOut>', self.bet_watermark)
        self.bet.insert(0, "  Bet")
        self.bet.config(fg="grey")

        self.guess_1 = Entry(self.label_down, width=15)
        self.guess_1.grid(column=0, row=1, pady=5)
        self.guess_1.bind('<FocusIn>', self.guess1_onclick)
        self.guess_1.bind('<FocusOut>', self.guess1_watermark)
        self.guess_1.insert(0, "  1st Guess")
        self.guess_1.config(fg="grey")

        self.guess_2 = Entry(self.label_down, width=15)
        self.guess_2.grid(column=0, row=2, pady=5)
        self.guess_2.bind('<FocusIn>', self.guess2_onclick)
        self.guess_2.bind('<FocusOut>', self.guess2_watermark)
        self.guess_2.insert(0, "  2nd Guess")
        self.guess_2.config(fg="grey")

        self.dice = Label(self.label_down_1, text=" ", width=3, relief=SUNKEN, bg="white", fg="darkgreen")
        self.dice.grid(column=0, row=0, pady=5)

        self.let_roll = Button(self.label_down_1, text="lets roll", command=self.game_ongoing_decider, bg="grey")
        self.let_roll.grid(column=0, row=2)

        self.window_start.destroy()
        self.window_game.mainloop()

    def game_start(self):
        self.frame_upper.pack(side=TOP)
        self.frame_upper_1.pack(side=LEFT)
        self.frame_upper_2.pack(side=RIGHT)
        self.frame_upper_3.pack(side=BOTTOM)

        self.name.pack(padx=5, pady=5)
        self.name.insert(0, "  Name")
        self.name.config(fg="grey")

        self.cost.pack(padx=5, pady=5)
        self.cost.insert(0, "  $$$")
        self.cost.config(fg="lightgreen")

        
        
        self.name.bind('<FocusIn>',  self.name_onclick)
        self.name.bind('<FocusOut>', self.name_watermark)

        self.cost.bind('<FocusIn>', self.cost_onclick)
        self.cost.bind('<FocusOut>', self.cost_watermark)

        self.play.pack(padx=5, pady=5)
        self.exit_btn.pack(padx=5, pady=5)

        self.window_start.mainloop()

  
game = Casino()

game.game_start()
