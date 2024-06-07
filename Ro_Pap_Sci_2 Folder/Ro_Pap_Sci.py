import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import threading
import time
import os

class Ro_Pap_Sci:

    #this is the constructor of the window
    def __init__(self, main):
        self.main = main
        self.main.title("Rock Paper Scissors")
        self.main.geometry("700x700") #This will be the size of the main window
        self.img_path1 = 'Images/Rock.jpg'
        self.img_path2 = 'Images/Scissors.jpg'
        self.img_path3 = 'Images/paper.jpg'
        roaming_appdata_path = os.getenv('APPDATA')
        self.save_Path = os.path.join(roaming_appdata_path, 'Rock Paper Scissors High Score.txt')
        with open(self.save_Path, 'a') as f:
            f.write('.')
        self.main_menu()

    #main menu function
    def main_menu(self):
 
        for widget in self.main.winfo_children():  # This for loop is used for creating multiple windows inside of a parent window without disrupting the widgets of
            widget.destroy()                                                                #parent and nor child window. It uses the winfo_children() method in tkinter library

        tk.Label(self.main, text="Welcome to Rock Paper Scissors", font=("Helvetica ", 20)).pack(pady=10) 
        img1 = Image.open(self.img_path1)
        photo1 = ImageTk.PhotoImage(img1)
        label1 = tk.Label(root, text="Rock", image=photo1)
        label1.image = photo1  
        label1.place(x=10, y=150) 
        text_label = tk.Label(root, text="Rock", font=("Arial", 12))
        text_label.place(x=130, y=380)

        def Scissors_Image():
            img2 = Image.open(self.img_path2)
            photo2 = ImageTk.PhotoImage(img2)
            label2 = tk.Label(root, text="Rock", image=photo2)
            label2.image = photo2 
            label2.place(x=400, y=150) 
            text_label = tk.Label(root, text="Scissors", font=("Arial", 12))
            text_label.place(x=475, y=380)

        def Paper_Image():
            img3 = Image.open(self.img_path3)
            photo3 = ImageTk.PhotoImage(img3)
            label3 = tk.Label(root, text="Rock", image=photo3)
            label3.image = photo3  
            label3.place(x=400, y=150) 
            text_label = tk.Label(root, text="Paper", font=("Arial", 12))
            text_label.place(x=490, y=480)

        def High_Score():
            os.startfile(self.save_Path)
            
        Images = [Scissors_Image, Paper_Image]

        selected_images = random.choice(Images)

        selected_images()
     
        tk.Button(self.main, text="Play New Game", command= self.Choose_element,height = 3, width = 18).place(x=280 ,y=500)
        tk.Button(self.main, text="High Score", command= High_Score,height= 3, width= 18).place(x=280, y=550)
        tk.Button(self.main, text="Close", command=self.main.quit, height=3, width=18).place(x=280, y=600)
    

    def Rock_Img(self):
        img1 = Image.open(self.img_path1)
        photo1 = ImageTk.PhotoImage(img1)
        label1 = tk.Label(root, text="Rock", image=photo1)
        label1.image = photo1  # Keep a reference to avoid garbage collection
        label1.place(x=10, y=150) 
        text_label = tk.Label(root, text="Rock", font=("Arial", 12))
        text_label.place(x=130, y=380)

    def Scissors_Img(self):
        img2 = Image.open(self.img_path2)
        photo2 = ImageTk.PhotoImage(img2)
        label2 = tk.Label(root, text="Scissor", image=photo2)
        label2.image = photo2  # Keep a reference to avoid garbage collection
        label2.place(x=10, y=150) 
        text_label = tk.Label(root, text="Scissors", font=("Arial", 12))
        text_label.place(x=130, y=380)

    def Paper_Img(self):
        img3 = Image.open(self.img_path3)
        img3 = img3.resize((300, 300))
        photo3 = ImageTk.PhotoImage(img3)
        label3 = tk.Label(root, text="Paper", image=photo3)
        label3.image = photo3  # Keep a reference to avoid garbage collection
        label3.place(x=30, y=150) 
        text_label = tk.Label(root, text="Paper", font=("Arial", 12))
        text_label.place(x=130, y=480)


    def Rock_Img2(self):
        img1 = Image.open(self.img_path1)
        photo1 = ImageTk.PhotoImage(img1)
        label1 = tk.Label(root, text="Rock", image=photo1)
        label1.image = photo1  # Keep a reference to avoid garbage collection
        label1.place(x=400, y=150) 
        text_label = tk.Label(root, text="Rock", font=("Arial", 12))
        text_label.place(x=475, y=380)


    def Scissors_Img2(self):
        img2 = Image.open(self.img_path2)
        photo2 = ImageTk.PhotoImage(img2)
        label2 = tk.Label(root, text="Rock", image=photo2)
        label2.image = photo2 
        label2.place(x=400, y=150) 
        text_label = tk.Label(root, text="Scissors", font=("Arial", 12))
        text_label.place(x=475, y=380)

    def Paper_Img2(self):
        img3 = Image.open(self.img_path3)
        img3 = img3.resize((300, 300))
        photo3 = ImageTk.PhotoImage(img3)
        label3 = tk.Label(root, text="Rock", image=photo3)
        label3.image = photo3  
        label3.place(x=400, y=150) 
        text_label = tk.Label(root, text="Paper", font=("Arial", 12))
        text_label.place(x=490, y=480)


    def Choose_element(self):
        for widget in self.main.winfo_children():
            widget.destroy()

        global current_index

        label = tk.Label(root, text="Rock Paper Scissors...", font=("Helvetica ", 20))
        label.pack(pady=20)

        Images = [self.img_path1, self.img_path2, self.img_path3] 
        current_index= 0

        label2 = tk.Label(root, text="Select", font=("Aril Black", 14))
        label2.pack(pady= 45)

        def display_img(index):
            global photo, current_index
            current_index = index
            image_path = Images[index]
            image = Image.open(image_path)
            image = image.resize((300, 300))
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo

        #Loading the initial Image
        global image_label
        image_label = tk.Label(root)
        image_label.pack(pady=20)
        display_img(current_index)

        def next_image():
            global current_index
            current_index = (current_index + 1) % len(Images)
            display_img(current_index)
            return current_index

        nx_button = tk.Button(root, text="Next",command= next_image,height= 1, width= 10)
        nx_button.place(x=550 , y=350)
        tk.Button(self.main, text="CHOOSE n START",command= lambda: self.Play_Game(current_index), height= 2, width= 15).place(x= 300, y= 550)
        tk.Button(self.main, text="Back to Main Menu", command= self.main_menu,height= 2, width= 15).place(x= 300, y= 600)


    def save_match(self, Result):
        with open(self.save_Path,'a') as f:
            f.write(".\n")
        def count_lines(filename):
            with open(filename, 'r') as file:
                return sum(1 for _ in file)
        lines = count_lines(self.save_Path)
        Player_score = 0
        Computer_score = 0
        Draws = 0
        if Result == 1:
            with open(self.save_Path, 'a') as f:
                f.write(f"Match {lines+1} : Draw {Draws+1}")
        elif Result == 11:
            with open(self.save_Path, 'a') as f:
                f.write(f"Match {lines+1} : Player Won +{Player_score+1}")
        elif Result == 12:
            with open(self.save_Path, 'a') as f:
                f.write(f"Match {lines+1} : Computer Won +{Computer_score+1}")

        else:
            try:
                with open(self.save_Path, 'a') as f:
                    f.write(f"Match {lines} : Result corrupted Draw",Draws+1)
            except FileExistsError as e:
                print(e)



    def Play_Game(self, index):
        for widget in self.main.winfo_children():
            widget.destroy()

        label = tk.Label(root, text="Start", font=("Algerian ", 30))
        label.pack(pady=20)
        opponent = [self.Rock_Img2, self.Scissors_Img2, self.Paper_Img2]
        opponents = [self.img_path1, self.img_path2, self.img_path3]


        if index == 0:
            self.Rock_Img()
        elif index == 1:
            self.Scissors_Img()
        elif index == 2:
            self.Paper_Img() 

        computer_select = random.choice(opponent)
        opp_index = opponent.index(computer_select)

        def result(index, opp_index):
            D = 1
            Y = 11
            C = 12
            if index == 0 and opp_index == 0:
                label = tk.Label(root, text="Draw", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return D
            elif index == 1 and opp_index == 1:
                label = tk.Label(root, text="Draw", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return D
            elif index == 2 and opp_index == 2:
                label = tk.Label(root, text="Draw", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return D

            elif index == 0 and opp_index == 1:
                label = tk.Label(root, text="You Win!!!", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return Y
            elif index == 0 and opp_index == 2:
                label = tk.Label(root, text="You Lose!!!", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return C

            elif index == 1 and opp_index == 2:
                label = tk.Label(root, text="You Win!!!", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return Y
            elif index == 1 and opp_index == 0:
                label = tk.Label(root, text="You Lose!!!", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return C

            elif index == 2 and opp_index == 0:
                label = tk.Label(root, text="You Win!!!", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return Y
            elif index == 2 and opp_index == 1:
                label = tk.Label(root, text="You Lose!!!", font=("Algerian ", 30))
                label.place(x = 280, y=520)
                return C

            else:
                label = tk.Label(root, text="An error occurred", font=("Algerian ", 30))
                label.pack(pady=350)


        def start_slideshow(images, display_time, duration):
            current_index = 0
            running = True
            
            def show_next_image():
                nonlocal current_index, running
                
                if not running:
                    return
                
                # Load and display the current image
                image_path = images[current_index]
                image = Image.open(image_path)
                image = image.resize((250, 250))
                photo = ImageTk.PhotoImage(image)
                image_label.config(image=photo)
                image_label.image = photo  # Keep a reference to avoid garbage collection
                
                # Update the index to show the next image
                current_index = (current_index + 1) % len(images)
                
                # Schedule the next image change
                root.after(display_time, show_next_image)
            
            def stop_slideshow():
                nonlocal running
                running = False
                image_label.config(image='')
                image_label.image = None
                computer_select()
                rs = result(index, opp_index)
                self.save_match(rs)
                tk.Button(self.main, text="Play Again",command= self.Choose_element, height= 2, width= 15).place(x= 280, y= 600)

            
            # Set up the Label to display images
            image_label = tk.Label(root)
            image_label.place(x=400, y=150)
            
            # Start the slideshow
            show_next_image()
            
            # Schedule the slideshow to stop after the specified duration
            root.after(duration, stop_slideshow)
            

        start_slideshow(opponents, 80, 5000)


root = tk.Tk()
App = Ro_Pap_Sci(root)
root.mainloop()