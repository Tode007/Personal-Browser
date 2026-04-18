import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

root = tk.Tk()
root.title("Personal Assistant")

#adding a background color

root.configure(bg ='green')

#define the function to automate youtube search
def search_youtube():
    query = entry.get()
    url = f'https://www.youtube.com/results?search_query={query}'
    webbrowser.open(url)

#define the function to automate google search
def search_google():
    query = entry.get()
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)
    

#define the function to automate instagram search
def search_instagram():
    Username = entry.get().replace('@', '')
    url = f'www.instagram.com/{Username}'
    webbrowser.open(url)

#create input field, labels and buttons
Label (root,bg='orange',fg='White',font=('Times new roman',16), text='Enter Your Command: ').pack(pady=10)
entry = Entry(root, width=50)
entry.pack(pady=10)
Button(root, text='Search on youtube',bg='red',fg='white' ,command=search_youtube).pack(pady=5)
Button(root, text='Search on Google',bg='yellow',fg='blue', command=search_google).pack(pady=5)
Button(root, text='Search on Instagram',bg='pink',fg='black', command=search_instagram).pack(pady=5)    

root.mainloop()    
