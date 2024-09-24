from tkinter import *
from tkinter import ttk
import requests
import deepl

auth_key = "e1e937f5-c260-4b02-b983-0fd0f6b82fd1:fx"  

root = Tk()
root.geometry('1100x420')  
root.resizable(0, 0)  
root['bg'] = 'black'  
root.title('Basic Translator')  
 
Label(root, text="Translator App", font="Arial 20 bold").pack()
 
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)
 
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)
 
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)
 
Output_text = Text(root, font='arial 10', height=4, wrap=WORD, padx=5, pady=5, width=40)
Output_text.place(x=600, y=140)
 
def fetch_languages():
    complete_url = "https://api-free.deepl.com/v2/languages?type=target"

    response = requests.get(complete_url, headers={"Authorization": f"DeepL-Auth-Key {auth_key}"})
    languages_map = {}
    for language in response.json():
        languages_map[language["name"]] = language["language"]
    return languages_map

languages = fetch_languages()
 
dest_lang = ttk.Combobox(root, values=list(languages.keys()),  width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('Choose Language')  
 
def Translate():
    try:
        language_code = languages.get(dest_lang.get())

        translator = deepl.Translator(auth_key)

        translation = translator.translate_text(Input_text.get(), target_lang=language_code)
      
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation.text)
    except Exception as e:
        print(f"Translation error: {e}")
 
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=180)
 
root.mainloop()