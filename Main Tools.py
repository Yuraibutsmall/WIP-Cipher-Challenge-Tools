from tkinter import *
import tkinter as tk
    

def ScriptSubmit():
    script = scriptInputText.get(1.0, tk.END+"-1c")
    outputLabel.config(text=script)
    return script


def ReplacePopup():
    def ReplaceWord():
        oldWord = oldWordBox.get(1.0, tk.END+"-1c")
        newWord = newWordBox.get(1.0, tk.END+"-1c")
        script = ScriptSubmit()
        newScript = script.replace(oldWord, newWord)
        outputLabel.config(text=newScript)
        popup.destroy()
    
    popup = tk.Tk()
    popup.title("Replace Config")
    
    oldWordTitle = tk.Label(popup, text = "Word/Letter to be replaced:", font = ("Comic Sans MS", 10, "bold"))
    oldWordTitle.place(x=5, y=0)
    oldWordBox = tk.Text(popup, width=20, height=1)
    oldWordBox.place(x=5, y=25)
    newWordTitle = tk.Label(popup, text = "New word/letter:", font = ("Comic Sans MS", 10, "bold"))
    newWordTitle.place(x=5, y=50)
    newWordBox = tk.Text(popup, width=20, height=1)
    newWordBox.place(x=5, y=75)
    replacerSubmitButton = tk.Button(popup, text = "Submit", font = ("Comic Sans MS", 10), command=ReplaceWord)
    replacerSubmitButton.place(x=5, y=120)
    popup.mainloop()

#Window Atributes
root = tk.Tk()
root.title("WIP Cryptography Tools")
root.geometry("480x720")

mainTitle = tk.Label(root, text = "Processes avaliable", font = ("Comic Sans MS", 20, "bold underline"))
mainTitle.place(x=5, y=5)

scriptInputLabel = tk.Label(root, text = "Input the script to be edited:", font = ("Comic Sans MS", 10, "bold"))
scriptInputLabel.place(x=5, y=50)

scriptInputText = tk.Text(root, width=58, height=10)
scriptInputText.place(x=5, y=80)

scriptSubmitButton = tk.Button(root, text = "Submit script", font = ("Comic Sans MS", 10), command=ScriptSubmit)
scriptSubmitButton.place(x=5, y=250)

functionSelectorTitle = tk.Label(root, text = "Chose a function to carry out on the script:", font = ("Comic Sans MS", 10, "bold"))
functionSelectorTitle.place(x=5, y=285)

textReplaceButton = tk.Button(root, text = "Replace Text", font = ("Comic Sans MS", 10), command=ReplacePopup)
textReplaceButton.place(x=5, y=310)

outputLabel = tk.Label(root, text ="Output:", font = ("Comic Sans MS", 10, "bold"))
outputLabel.place(x=5, y=550)

outputLabel = tk.Label(root, text = "", font = ("Comic Sans MS", 10, "bold"), wraplength = 450, justify = "left")
outputLabel.place(x=5, y=580)


root.mainloop()













