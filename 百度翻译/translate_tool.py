import baidu_fanyi
import tkinter as tk


root=tk.Tk()
root.title('翻译小工具')
root.geometry('550x600+300+150')
L1=tk.Label(root,text='百度翻译',bg='blue',fg='white',font=('微软雅黑',20))
L1.grid(row=0,columnspan=2)
E1=tk.Entry(root,bg='green',fg='white')
E2=tk.Entry(root,bg='green',fg='white')
E1.grid(row=1,column=0,padx=50)
E2.grid(row=1,column=1,sticky=tk.NE,padx=50)

lb1=tk.Listbox(root,height=15,width=20)
lb2=tk.Listbox(root,height=15,width=20)

languages=baidu_fanyi.language_list()
for one in languages:
    lb1.insert(tk.END,one)
    lb2.insert(tk.END, one)

lb1.grid(row=2,column=0,pady=0,sticky=tk.N)
lb2.grid(row=2,column=1,pady=0,sticky=tk.N)

def func1(event):
    val1=lb1.get(lb1.curselection()[0])
    E1.delete(0,tk.END)
    E1.insert(tk.END,val1)

def func2(event):
    val2=lb2.get(lb2.curselection()[0])
    E2.delete(0,tk.END)
    E2.insert(tk.END,val2)

def fanyi():
    word = E3.get()
    fro = E1.get()
    to = E2.get()
    try:
        result=baidu_fanyi.main(word,fro,to)
    except Exception as e:
        result='翻译出现错误，错误信息为：'+str(e)
    T1.delete(1.0, tk.END)
    T1.insert(1.0, result)


lb1.bind('<Double-Button-1>',func1)
lb2.bind('<Double-Button-1>',func2)

E3=tk.Entry(root,width=30,font=('微软雅黑',12),fg='red')
E3.grid(row=3,pady=50,sticky=tk.E)
B1=tk.Button(root,text='翻译',bg='blue',fg='white',width=10,command=fanyi)
B1.grid(row=3,column=1,padx=1,sticky=tk.W)
tk.Label(root,text='翻译结果：',font=('微软雅黑',15)).grid(row=4,sticky=tk.W)
T1=tk.Text(root,font=('微软雅黑',15),width=40,fg='green')
T1.grid(row=5,columnspan=2)

root.mainloop()
