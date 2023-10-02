from collections import Counter
from tkinter import *
import tkinter as tk

#Global Variable that stores the current state of the script
newScript = "" 
caesarKeyLength = 0

#Submit Script to be edited function (Asigns the input script to variable newScript)
def ScriptSubmit():
    global newScript
    newScript = scriptInputText.get(1.0, tk.END+"-1c")
    outputLabel.config(text=newScript)
    

#Replace Letter/Word Function
def ReplacePopup():
    def ReplaceWord():
        #Replaces old word with new and stores the result under the global variable newScript
        global newScript
        oldWord = oldWordBox.get(1.0, tk.END+"-1c")
        newWord = newWordBox.get(1.0, tk.END+"-1c")
        newScript = newScript.replace(oldWord, newWord)
        
        #Edits output in root program to display the new script
        outputScript = newScript
        outputLabel.config(text=outputScript)
        popup.destroy()
    
    #Creates popup window with the tools to replace letters / words
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


#Common Word Finder
def CommonWordPopup():
    def CommonWord():
        global newScript
        
        wordList = (newScript.upper()).split()
        wordCount = Counter(wordList)
        amountOfMostCommon = int(searcherBox.get(1.0, tk.END+"-1c"))
        listOfValues = wordCount.most_common(amountOfMostCommon)
        commonWordOutput = "The most common words are " + str(listOfValues)
        outputLabel.config(text=commonWordOutput)
        popup.destroy()
        
    #Creates popup window with the tools to find most common word
    popup = tk.Tk()
    popup.title("Find Config")
    popup.geometry("260x200")
    
    searcherTitle = tk.Label(popup, text = "Amount of most common words:", font = ("Comic Sans MS", 10, "bold"))
    searcherTitle.place(x=5, y=0)
    searcherBox = tk.Text(popup, width=20, height=1)
    searcherBox.place(x=5, y=25)
    searcherSubmitButton = tk.Button(popup, text = "Submit", font = ("Comic Sans MS", 10), command=CommonWord)
    searcherSubmitButton.place(x=5, y=120)
    popup.mainloop()


#Manual Caesar Cipher Solver
def SingularCaesarCipherPopUp():
    def SingularCaesarCipher():
        global newScript
        newScript = newScript.lower()
        outputScriptForward = ""
        outputScriptBackward = ""
        keyLength = int(keyLengthBox.get(1.0, tk.END+"-1c"))
                        
        #magic 
        for count in range(0, len(newScript)):
            if newScript[count].isalpha():
                stayInAlphabet = ord(newScript[count]) + keyLength
            else:
                outputScriptForward += newScript[count]
                continue
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            if stayInAlphabet < ord('a'):
                stayInAlphabet += 26   
            finalLetter = chr(stayInAlphabet)
            outputScriptForward += finalLetter
            
        for count in range(0, len(newScript)):
            if newScript[count].isalpha():
                stayInAlphabet = ord(newScript[count]) - keyLength
                print(stayInAlphabet)
            else:
                outputScriptBackward += newScript[count]
                continue
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            if stayInAlphabet < ord('a'):
                stayInAlphabet += 26
            finalLetter = chr(stayInAlphabet)
            outputScriptBackward += finalLetter
            
        #Edits output in root program to display the new script
        output = "key: +"+str(keyLength)+"\n"+outputScriptForward+"\n or \n"+"key: -"+str(keyLength)+"\n"+outputScriptBackward
        outputLabel.config(text=output)
        
        singularCaesarCipherPopup.destroy()
        
    singularCaesarCipherPopup = tk.Tk()
    singularCaesarCipherPopup.title("Caesar Shift")
    singularCaesarCipherPopup.geometry("260x200")
        
    searcherTitle = tk.Label(singularCaesarCipherPopup, text = "Shift Amount: ", font = ("Comic Sans MS", 10, "bold"))
    searcherTitle.place(x=5, y=0)
    
    keyLengthBox = tk.Text(singularCaesarCipherPopup, width=20, height=1)
    keyLengthBox.place(x=5, y=25)
    
    keyLengthSubmitButton = tk.Button(singularCaesarCipherPopup, text = "Submit", font = ("Comic Sans MS", 10), command=SingularCaesarCipher)
    keyLengthSubmitButton.place(x=5, y=120)
        
    singularCaesarCipherPopup.mainloop()
    SingularCaesarCipher()
        
#Brute Force Ceaser Cipher Solver
def AutoCaesarCipherPopUp():
    def AutoCaesarCipherSolver(): 
        global newScript
        newScript = newScript.lower()
        outputScriptForward = ""
        global caesarKeyLength 
        caesarKeyLength += 1
        
        for count in range(0, len(newScript)):
            if newScript[count].isalpha():
                stayInAlphabet = ord(newScript[count]) + caesarKeyLength
            else:
                outputScriptForward += newScript[count]
                continue
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            if stayInAlphabet < ord('a'):
                stayInAlphabet += 26   
            finalLetter = chr(stayInAlphabet)
            outputScriptForward += finalLetter
        
        outputLabel.config(text=outputScriptForward)
        
    AutoCaesarCipherSolver()
    
#Simple Keyword Substitution Cipher With Ordered Alphabet
def KnownKeywordSubstitutionPopup():
    def KnownKeywordSubstitutionSolver():
        global newScript
        newScript = newScript.lower()
        outputScript = ""
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        keyAplhabet = ["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        keyWord = keyBox.get(1.0, tk.END+"-1c")
        keyWord = keyWord.lower()
        if len(keyWord) > 26:
            outputLabel.config(text="invalidKeyLength")
        for count in range(0, len(keyWord)):
            keyAplhabet[count] = keyWord[count]
            
        while("" in keyAplhabet):
            keyAplhabet.remove("")
            
        for count in range(0, len(alphabet)):
            if alphabet[count] in keyAplhabet:
                continue
            else:
                keyAplhabet.append(alphabet[count])
                
        for count in range(0, len(newScript)):
            if newScript[count].isalpha():
                listPos = keyAplhabet.index(newScript[count])
                outputScript += alphabet[listPos]
            else:
                outputScript += newScript[count]
                continue
        
        outputLabel.config(text=outputScript)    
        KnownKeywordSubstitutionPopup.destroy()
        
        
    KnownKeywordSubstitutionPopup = tk.Tk()
    KnownKeywordSubstitutionPopup.title("Caesar Shift")
    KnownKeywordSubstitutionPopup.geometry("260x200")
        
    searcherTitle = tk.Label(KnownKeywordSubstitutionPopup, text = "Key: ", font = ("Comic Sans MS", 10, "bold"))
    searcherTitle.place(x=5, y=0)
    
    keyBox = tk.Text(KnownKeywordSubstitutionPopup, width=20, height=3)
    keyBox.place(x=5, y=25)
    
    keySubmitButton = tk.Button(KnownKeywordSubstitutionPopup, text = "Submit", font = ("Comic Sans MS", 10), command=KnownKeywordSubstitutionSolver)
    keySubmitButton.place(x=5, y=120)
        
    KnownKeywordSubstitutionPopup.mainloop()


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

#Text Replace Button
textReplaceButton = tk.Button(root, text = "Replace Text", font = ("Comic Sans MS", 10), command=ReplacePopup)
textReplaceButton.place(x=5, y=310)

#Most Common Word Button
mostCommonWord = tk.Button(root, text = "Common Word", font = ("Comic Sans MS", 10), command=CommonWordPopup)
mostCommonWord.place(x=5, y=350)

#Singular Caesar Cipher Button
SingleCaesarCipherWord = tk.Button(root, text = "Singular Caesar Cipher", font = ("Comic Sans MS", 10), command=SingularCaesarCipherPopUp)
SingleCaesarCipherWord.place(x=5, y=390)

#Auto Caesar Cipher Button
AutoCaesarCipherWord = tk.Button(root, text = "Auto Caesar Cipher + 1", font = ("Comic Sans MS", 10), command=AutoCaesarCipherPopUp)
AutoCaesarCipherWord.place(x=5, y=430)

#Known Keyword Substitution Cipher Normal Order Button
KnownKeywordSubstitutionCipherWord = tk.Button(root, text = "Known Keyword Substitution Cipher Normal Alphabet Order", font = ("Comic Sans MS", 10), command=KnownKeywordSubstitutionPopup)
KnownKeywordSubstitutionCipherWord.place(x=5, y=470)

outputLabel = tk.Label(root, text ="Output:", font = ("Comic Sans MS", 10, "bold"))
outputLabel.place(x=5, y=550)

outputLabel = tk.Label(root, text = "", font = ("Comic Sans MS", 10, "bold"), wraplength = 900, justify = "left")
outputLabel["state"] = "readonly"
outputLabel.place(x=5, y=580)

root.mainloop()






