from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

def btn_click():
    mark = 0
    warn = False
    if v1.get()==1 and v2.get()==1 and v3.get()==0 and v4.get()==0:
        mark += 2
    elif v1.get()==1 and v2.get()==0 and v3.get()==0 and v4.get()==0:
        mark += 0
    elif v1.get()==0 and v2.get()==1 and v3.get()==0 and v4.get()==0:
        mark += 0
    elif v1.get()==0 and v2.get()==0 and v3.get()==0 and v4.get()==0:
        warn = True
    if not ent2.get():
        warn = True    
    elif ent2.get() in ["Київ", "київ"]:
        mark += 2
    if not ent2.get():
        warn = True
    elif scl.get() == 4:
        mark += 2
    if not ent1.get():
        warn = True
    elif ent1.get() in ["Чорне море", "чорне море", "чорне", "Чорне" ]:
        mark += 2
    if not cbx.get():
        warn = True
    elif cbx.get() == "км":
        mark += 2
    if not lbx.curselection():
        warn = True
    elif lbx.curselection()[0] == 3:
        mark += 2
    showinfo(title="Результат", message="Ваша оцінка: "+str(mark))

def on_configure(event):
    canvas.config(scrollregion=canvas.bbox("all"))

root = Tk()
root.title("Тест з географії")
root.geometry("400x600")
font_title = ("Arial", 12, "bold")
font_q = ("Arial", 10, "bold")
font_ans = ("Arial", 10)

canvas = Canvas(root, yscrollcommand=True, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

tk = Frame(canvas)
canvas.create_window((0,0), window=tk, anchor="nw")

scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)
tk.bind("<Configure>", on_configure)

lbl1_1 = Label(tk, text="Питання №1", font=font_title)
lbl1_2 = Label(tk, text="Які існують остріви у світі?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Гренландія", variable=v1, font=font_ans, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Нова Гвінея", variable=v2, font=font_ans, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Крим", variable=v3, font=font_ans, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Африка", variable=v4, font=font_ans, onvalue=1, offvalue=0)

lbl2_1 = Label(tk, text="Питання №2", font=font_title)
lbl2_2 = Label(tk, text="Яке найбільше місто України?", font=font_q)
ent2 = Entry(tk, font=font_ans)

lbl3_1 = Label(tk, text="Питання №3", font=font_title)
lbl3_2 = Label(tk, text="Скільки океанів в світі?", font=font_q)
scl = Scale(tk, orient=HORIZONTAL, from_ =0, to=16, length=250, tickinterval=2, resolution=1, font=font_ans)

lbl4_1 = Label(tk, text="Питання №4", font=font_title)
lbl4_2 = Label(tk, text="Найбільше море України?", font=font_q)
ent1 = Entry(tk, font=font_ans)

lbl5_1 = Label(tk, text="Питання №5", font=font_title)
lbl5_2 = Label(tk, text="Як скорочено записують кілометри?", font=font_q)
data = ('м', 'км', 'мм', 'дм')
cbx = ttk.Combobox(tk, font=font_ans, values=data)

lbl6_1 = Label(tk, text="Питання №6", font=font_title)
lbl6_2 = Label(tk, text="Як скорочено записують дициметри?", font=font_q)
lbx = Listbox(tk, font=font_ans, width=5, height=4)
for el in data:
    lbx.insert(END, el)

btn = Button(tk, text="Відповісти", command=btn_click, font=font_q)
v6 = StringVar()
lbl5 =Label(tk, text='', textvariable=v6, font=font_title)

lbl1_1.pack(pady=10)
lbl1_2.pack(anchor=W, padx=10)
chb1.pack(anchor=W, padx=10)
chb2.pack(anchor=W, padx=10)
chb3.pack(anchor=W, padx=10)
chb4.pack(anchor=W, padx=10)
lbl2_1.pack(pady=10)
lbl2_2.pack(anchor=W, padx=10)
ent2.pack(anchor=W, padx=10)
lbl3_1.pack(pady=10)
lbl3_2.pack(anchor=W, padx=10)
scl.pack(anchor=W, padx=10)
lbl4_1.pack(pady=10)
lbl4_2.pack(anchor=W, padx=10)
ent1.pack(anchor=W, padx=10)
lbl5_1.pack(pady=10)
lbl5_2.pack(anchor=W, padx=10)
cbx.pack(anchor=W, padx=10)
lbl6_1.pack(pady=10)
lbl6_2.pack(anchor=W, padx=10)
lbx.pack(anchor=W, padx=10)
btn.pack()
lbl5.pack()

tk.mainloop()
