import tkinter

def combine():
    firstname = str(firstNameEntry.get())
    secondname = str(secondNameEntry.get())
    result = firstname + secondname + "@gmail.com"
    suggestedLabel.config(text="Suggested: " + str(result))

def clears():
    fisrtname = firstNameEntry.delete(0)
    secondname = secondNameEntry.delete(0)
    
    
def exit():
    window.destroy()

window = tkinter.Tk()
window.title("Automatic Username")
window.minsize(width=700, height=300)

labelFrame = tkinter.LabelFrame(text="Username Suggestion")
labelFrame.pack(fill="both", expand="yes")

firstNameLabel = tkinter.Label(labelFrame,text="First Name: ")
firstNameLabel.pack()

firstNameEntry = tkinter.Entry(labelFrame, bd=2, width=30)
firstNameEntry.pack()

secondNameLabel = tkinter.Label(labelFrame, text="Second Name: ")
secondNameLabel.pack()

secondNameEntry = tkinter.Entry(labelFrame,bd=2,width=30)
secondNameEntry.pack()

suggestedLabel = tkinter.Label(labelFrame, text="Suggested: ")
suggestedLabel.pack()


combineButton = tkinter.Button(labelFrame, text="Combine",command=combine)
combineButton.pack()

clearButton = tkinter.Button(labelFrame, text="Clear",command=clears)
clearButton.pack()

exitButton = tkinter.Button(text="Exit", command="exit")
exitButton.pack()
window.mainloop()