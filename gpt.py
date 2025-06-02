from tkinter import ttk
from tkinter import *
import google.generativeai as genai
import wikipedia
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
OPEN_AI = os.getenv('OPEN_AI')
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
OPEN_AI = os.getenv('OPEN_AI')

# from openai import OpenAI

# client = OpenAI(api_key=OPEN_AI)

# def GPTclone(prompt):
# response = client.chat.completions.create(
# model = 'gpt-4o-mini',
# messages=[
# {"role" : "system" , "content" : "You are a helpfull assistant."},
# {"role" : "user" , "content": prompt},
 
# ],
# max_tokens=50,
# )
# result = response.choices[0].message.content
# # print(result)
# output.delete(2.0 , END)
# output.insert(1.0 , result)
 
def gemini():
 genai.configure(api_key=GEMINI_API_KEY)
 model = genai.GenerativeModel(model_name='gemini-1.5-flash')
 response = model.generate_content(query.get())
 data = response.text
 output.delete(2.0 , END)
 output.insert(1.0 , data)
 

def searchonWiki():
    data = query.get()
    try:
        data = wikipedia.summary(query.get() , sentences=2)
        output.delete(2.0)
        output.insert(1.0,data)
    except:
        print("error")
 

root = Tk()

root.title("Wikipedia")

label = Label(text="Search on Wikipedia")
label.pack()


query = ttk.Entry(root)
query.pack()

output = Text(root ,height=10 , width=50 ,wrap= WORD)
output.pack()


button = ttk.Button(text='Search' , command=searchonWiki)
button.pack()
button = ttk.Button(text='AI' , command=gemini)
button.pack()

button = ttk.Button(text='Quit' , command=root.destroy)
button.pack()

root.mainloop()