from tkinter import *
window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

#Label
greeting = Label(text = "Hello User", fg = 'pink')
#Button
button = Button(text = "Click me", bg="white", fg = "black")
#Entry
entry = Entry(fg='yellow', bg ='blue', width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()
window.mainloop()