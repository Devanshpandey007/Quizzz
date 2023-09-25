from tkinter import *
from quizz_api import *
import html
obj = api_req()
print(obj.data)
counter =0
x = 0
score = 0
# BLUE = '#4477CE'
light_blue ='#8CABFF'
# RED = '#C70039'
# GREEN = '#5B9A8B'
LIGHT_GREEN = '#C8E4B2'
LIGHT_RED = '#EF6262'
window = Tk()
window.title("Quizzzzzssss")
window.geometry("400x400")
label =Label(text="Quizzzzzzsss", font=('Arial',11))
label.place(x=50,y=12)
score_text_label = Label(text='Score: ', font=('Arial',11))
score_text_label.place(x=300,y=12)
score_txt =Label(text=score,font=('Arial',11))
score_txt.place(x=350,y=12)
canva = Canvas(window,height=250,width=320)
canva.place(x=40,y=45)
canva.config(bg=light_blue)
answer = obj.data['results'][x]['question']
new_text=canva.create_text(158,110,text=answer,width= 300,font=('Arial',13,'italic'))
photo_true= PhotoImage(file="new_correct_img (1).png")
photo_false = PhotoImage(file="new_wrong_img (1).png")
initial_value = 'True'
def comparison():
    if initial_value==obj.data['results'][x]['correct_answer']:
        canva.config(bg= LIGHT_GREEN)
        global score,counter
        if counter<1:
            score+=5
        score_txt.config(text=score)
        counter=1

    else:
        canva.config(bg=LIGHT_RED)

def correct():
    global initial_value
    initial_value = 'True'
    comparison()
    Wrong_button.config(state=DISABLED)
def not_correct():
    global initial_value
    initial_value = 'False'
    comparison()
    Correct_Button.config(state=DISABLED)
def next():
    global x,obj
    x+=1
    if x>20:
        Correct_Button.config(state=DISABLED)
        Wrong_button.config(state=DISABLED)
        canva.config(bg=light_blue)
        canva.itemconfig(new_text, text = "Well that's it for today, thanks for playing.")
    canva.config(bg=light_blue)
    answer1 =html.unescape(obj.data['results'][x]['question'])
    canva.itemconfig(new_text,text = answer1)
    global counter
    counter = 0
    Correct_Button.config(state=NORMAL)
    Wrong_button.config(state=NORMAL)
Correct_Button = Button(window,image=photo_true,command=correct)
Wrong_button = Button(window,image=photo_false,command=not_correct)
next_button = Button(window,text='⏭',height=3,width=4,command=next)
Correct_Button.place(x=90,y=330)
Wrong_button.place(x=230,y=330)
next_button.place(x=355,y=330)


window.mainloop()
