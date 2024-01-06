#Project gym 
#The aim of this project is to get the user to enter information about their goals in the gym
#and it will provide them with  a scheudle based on the amount of time they have  in their week
#

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

root.title("Gym workout program")


#Ask the user for some basic information about them , height weight and age

#there wil be a button which the user clicks to go to a new screen which they display all their information

#Function to open to a new screen which  gets the useer to input all their information 

def get_user_info():
    
    info_screen = tk.Toplevel(root)
    info_screen.title("User Information")
    info_screen.geometry("800x600")

    #collects user input
    def submit():
        
        
        user_weight = weight_input.get("1.0", "end-1c").strip()
        user_height = height_input.get("1.0", "end-1c").strip()
        user_age = age_input.get("1.0", "end-1c").strip()
        
        # if isinstance(int(user_weight),int) or isinstance(int(user_height),int) or isinstance(int(user_age),int) and int(user_age) <0:
        #     sumbit_label.config(text="information is valid")

        # else:
        #     sumbit_label.config(text="information is invalid")
        try:
            if isinstance(int(user_weight),int) and isinstance(int(user_height),int)  and int(user_age) >0:
                sumbit_label.config(text="information valid")
        except:
            sumbit_label.config(text="infomration is invalid")
    #name
    name_label=tk.Label(info_screen,text="enter your name ")
    name_label.pack()
    name_input = tk.Text(info_screen,width=30 ,height=1)
    name_input.pack()
    #age
    age_label = tk.Label(info_screen, text="Enter your age")
    age_label.pack(pady=10)
    age_input = tk.Text(info_screen,width =10,height=1)
    age_input.pack(pady=10)
    #weight button
    weight_label = tk.Label(info_screen, text="Enter your weight(kg)")
    weight_label.pack(pady=10)
    weight_input = tk.Text(info_screen,width =10,height=1)
    weight_input.pack(pady=10)

    #height button
    height_label = tk.Label(info_screen,text="Enter your height(cm)")
    height_label.pack(pady=10)
    height_input = tk.Text(info_screen,width =10,height=1)
    height_input.pack(pady=10)

    

    #submit button

    submit_button = tk.Button(info_screen, text="Submit", command=submit)
    submit_button.pack(pady=10)
    sumbit_label = tk.Label(info_screen,text='')
    sumbit_label.pack(pady=10)
   
    #go back button
    button_back = tk.Button(info_screen, text="Go Back", command=lambda: close_window(info_screen))
    button_back.pack(pady=10)
    
        
   
    
    # stops the information screen being displayed multiple times
    info_button.config(state=tk.DISABLED)


# this fucntion will close the window
    
def close_window(screen):
    screen.destroy()
    info_button.config(state=tk.NORMAL)

#submit fucttion


#information button
#to make sure the user cant spam open a new screen

info_button = tk.Button(root, text="Information", command=get_user_info)
info_button.pack()
    

#submit button




root.mainloop()

#if you think of a better way to write the code , dont feel afraid to change it 




#want to add all the information to a text file so when the user enters their name it remember it 