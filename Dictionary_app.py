#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install PyMultiDictionary


# In[ ]:


from tkinter import *
import tkinter as tk
from PyMultiDictionary import MultiDictionary

# Create Objects
dictionary = MultiDictionary()

# Instantiate the Tk class
root = tk.Tk()

# Set geometry
root.geometry("400x408")

def dict():
    # Use a try-except block to handle missing values
    try:
        word_text = word.get()
        # Get meaning, synonyms, and antonyms
        meaning_text = dictionary.meaning('en', word_text)
        synonym_text = dictionary.synonym('en', word_text)
        antonym_text = dictionary.antonym('en', word_text)

        # Update UI components
        meaning.config(text=meaning_text)
        synonym.config(text=synonym_text)
        antonym.config(text=antonym_text)
    except Exception as e:
        meaning.config(text="Word not found.")
        synonym.config(text="")
        antonym.config(text="")

# Add Labels, Button and Frames
Label(root, text="Dictionary", font=("Helvetica 20 bold"), fg="Green").pack(pady=10)

# Frame 1
frame = Frame(root)
Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack()
frame.pack(pady=10)

# Frame for Meaning
frame1 = Frame(root)
Label(frame1, text="Meaning:-", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

# Frame for Synonyms
frame2 = Frame(root)
Label(frame2, text="Synonym:-", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)

# Frame for Antonyms
frame3 = Frame(root)
Label(frame3, text="Antonym:-", font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

# Submit Button
Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()

# Execute Tkinter
root.mainloop()


# In[ ]:




