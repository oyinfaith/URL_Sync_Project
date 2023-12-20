from tkinter import *
import pyshorteners

root = Tk()
root.title("Motunrayo's URL Shortener")
root.geometry("450x300")
root.resizable(0,0)

def shorten_url():
    long_url = url_entry.get()
    shortened_url = pyshorteners.Shortener().tinyurl.short(long_url)
    result_entry.delete(0, END) 
    result_entry.insert(END, shortened_url)

Label(root, text="URL Shortener", font=("Algerian 25"), fg='purple').pack()

frame1 = Frame(root)
Label(frame1, text="Enter the URL here: ", font=("timeroman 12 bold"), fg='purple').pack(side=LEFT)
url_entry = Entry(frame1, width="38", borderwidth=8, font=("timeroman 10 bold"))
url_entry.pack()
frame1.pack(pady=10)

Button(root, text="Generate Link", fg='purple', borderwidth=3, font=('timeroman 8 bold'), command=shorten_url).pack(pady=20)

frame2 = Frame(root)
Label(frame2, text="Copy URL: ", fg="purple", font=('timeroman 8 bold')).pack(side=LEFT)
result_entry = Entry(frame2, width="25", fg='black', borderwidth=5, font=('timeroman 8 bold'))
result_entry.pack()
frame2.pack(pady=40)

root.mainloop()
