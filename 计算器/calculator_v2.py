import calculate
import tkinter as tk

root=tk.Tk()
root.title('计算器')
root.geometry('203x250+300+300')
T1=tk.Text(root,bg='#FCFCFC',width=22,height=3,font=('微软雅黑',12))
T1.grid(row=0,columnspan=4)

#第一行
def func_C():
    data=T1.get(1.0,tk.END)[:-2]
    T1.delete(1.0, tk.END)
    T1.insert(1.0,data)

def func_CA():
    T1.delete(1.0,tk.END)
def func_DIV():
    T1.insert(tk.END,'/')
def func_M():
    T1.insert(tk.END,'*')
tk.Button(root,text='←',command=func_C,width=4,height=1,bg='#FFFFE0').grid(row=1,column=0,padx=1,pady=1)
tk.Button(root,text='CA',command=func_CA,width=4,height=1,bg='#FFFACD').grid(row=1,column=1,padx=1,pady=1)
tk.Button(root,text='/',command=func_DIV,width=4,height=1,bg='#FFF0F5').grid(row=1,column=2,padx=1,pady=1)
tk.Button(root,text='*',command=func_M,width=4,height=1,bg='#FFEBCD').grid(row=1,column=3,padx=1,pady=1)

#第二行
def func_7():
    T1.insert(tk.END,'7')
def func_8():
    T1.insert(tk.END,'8')
def func_9():
    T1.insert(tk.END,'9')
def func_SUB():
    T1.insert(tk.END,'-')
tk.Button(root,text='7',command=func_7,width=4,height=1,bg='#FFFFE0').grid(row=2,column=0,padx=1,pady=1)
tk.Button(root,text='8',command=func_8,width=4,height=1,bg='#FFFACD').grid(row=2,column=1,padx=1,pady=1)
tk.Button(root,text='9',command=func_9,width=4,height=1,bg='#FFF0F5').grid(row=2,column=2,padx=1,pady=1)
tk.Button(root,text='-',command=func_SUB,width=4,height=1,bg='#FFEBCD').grid(row=2,column=3,padx=1,pady=1)

#第三行
def func_4():
    T1.insert(tk.END,'4')
def func_5():
    T1.insert(tk.END,'5')
def func_6():
    T1.insert(tk.END,'6')
def func_ADD():
    T1.insert(tk.END,'+')
tk.Button(root,text='4',command=func_4,width=4,height=1,bg='#FFFFE0').grid(row=3,column=0,padx=1,pady=1)
tk.Button(root,text='5',command=func_5,width=4,height=1,bg='#FFFACD').grid(row=3,column=1,padx=1,pady=1)
tk.Button(root,text='6',command=func_6,width=4,height=1,bg='#FFF0F5').grid(row=3,column=2,padx=1,pady=1)
tk.Button(root,text='+',command=func_ADD,width=4,height=1,bg='#FFEBCD').grid(row=3,column=3,padx=1,pady=1)


#第四行
def func_1():
    T1.insert(tk.END,'1')
def func_2():
    T1.insert(tk.END,'2')
def func_3():
    T1.insert(tk.END,'3')
def func_EQL():
    data=T1.get(1.0,tk.END)
    res=calculate.main(data)
    T1.delete(1.0,tk.END)
    T1.insert(1.0,res)

tk.Button(root,text='1',command=func_1,width=4,height=1,bg='#FFFFE0').grid(row=4,column=0,padx=1,pady=1)
tk.Button(root,text='2',command=func_2,width=4,height=1,bg='#FFFACD').grid(row=4,column=1,padx=1,pady=1)
tk.Button(root,text='3',command=func_3,width=4,height=1,bg='#FFF0F5').grid(row=4,column=2,padx=1,pady=1)
tk.Button(root,text='=',command=func_EQL,width=4,height=1,bg='#FF34B3').grid(row=4,column=3,padx=1,pady=1)

#第五行
def func_0():
    T1.insert(tk.END,'0')
def func_LK():
    T1.insert(tk.END,'(')
def func_POT():
    T1.insert(tk.END,'.')
def func_RK():
    T1.insert(tk.END,')')
tk.Button(root,text='0',command=func_0,width=4,height=1,bg='#FFFFE0').grid(row=5,column=0,padx=1,pady=1)
tk.Button(root,text='(',command=func_LK,width=4,height=1,bg='#EE7AE9').grid(row=5,column=1,padx=1,pady=1)
tk.Button(root,text='.',command=func_POT,width=4,height=1,bg='#00F5FF').grid(row=5,column=2,padx=1,pady=1)
tk.Button(root,text=')',command=func_RK,width=4,height=1,bg='#EE7AE9').grid(row=5,column=3,padx=1,pady=1)
root.mainloop()
