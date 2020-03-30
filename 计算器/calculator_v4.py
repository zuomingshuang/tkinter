import calculate
import tkinter as tk

root=tk.Tk()
root.title('计算器')
root.geometry('210x250+300+300')
T1=tk.Text(root,bg='#00F5FF',width=23,height=2,font=('微软雅黑',12))
T1.grid(row=0,columnspan=4)
T2=tk.Text(root,bg='#00F5FF',width=23,height=1,font=('微软雅黑',12),fg='red')
T2.grid(row=1,columnspan=4)

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
tk.Button(root,text='←',command=func_C,width=4,height=1,bg='#00EE00').grid(row=2,column=0,padx=1,pady=1)
tk.Button(root,text='CA',command=func_CA,width=4,height=1,bg='#00EE00').grid(row=2,column=1,padx=1,pady=1)
tk.Button(root,text='/',command=func_DIV,width=4,height=1,bg='#00EE00').grid(row=2,column=2,padx=1,pady=1)
tk.Button(root,text='*',command=func_M,width=4,height=1,bg='#00EE00').grid(row=2,column=3,padx=1,pady=1)

#第二行
def func_7():
    T1.insert(tk.END,'7')
def func_8():
    T1.insert(tk.END,'8')
def func_9():
    T1.insert(tk.END,'9')
def func_SUB():
    T1.insert(tk.END,'-')
tk.Button(root,text='柒',command=func_7,width=4,height=1,bg='#00EE00').grid(row=3,column=0,padx=1,pady=1)
tk.Button(root,text='捌',command=func_8,width=4,height=1,bg='#00EE00').grid(row=3,column=1,padx=1,pady=1)
tk.Button(root,text='玖',command=func_9,width=4,height=1,bg='#00EE00').grid(row=3,column=2,padx=1,pady=1)
tk.Button(root,text='减',command=func_SUB,width=4,height=1,bg='#00EE00').grid(row=3,column=3,padx=1,pady=1)

#第三行
def func_4():
    T1.insert(tk.END,'4')
def func_5():
    T1.insert(tk.END,'5')
def func_6():
    T1.insert(tk.END,'6')
def func_ADD():
    T1.insert(tk.END,'+')
tk.Button(root,text='肆',command=func_4,width=4,height=1,bg='#00EE00').grid(row=4,column=0,padx=1,pady=1)
tk.Button(root,text='伍',command=func_5,width=4,height=1,bg='#00EE00').grid(row=4,column=1,padx=1,pady=1)
tk.Button(root,text='陆',command=func_6,width=4,height=1,bg='#00EE00').grid(row=4,column=2,padx=1,pady=1)
tk.Button(root,text='加',command=func_ADD,width=4,height=1,bg='#00EE00').grid(row=4,column=3,padx=1,pady=1)


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
    T2.delete(1.0,tk.END)
    T2.insert(1.0,res)

tk.Button(root,text='壹',command=func_1,width=4,height=1,bg='#00EE00').grid(row=5,column=0,padx=1,pady=1)
tk.Button(root,text='贰',command=func_2,width=4,height=1,bg='#00EE00').grid(row=5,column=1,padx=1,pady=1)
tk.Button(root,text='叁',command=func_3,width=4,height=1,bg='#00EE00').grid(row=5,column=2,padx=1,pady=1)
tk.Button(root,text='等于',command=func_EQL,width=4,height=1,bg='#006400',fg='white').grid(row=5,column=3,padx=1,pady=1)

#第五行
def func_0():
    T1.insert(tk.END,'0')
def func_LK():
    T1.insert(tk.END,'(')
def func_POT():
    T1.insert(tk.END,'.')
def func_RK():
    T1.insert(tk.END,')')
tk.Button(root,text='零',command=func_0,width=4,height=1,bg='#00EE00').grid(row=6,column=0,padx=1,pady=1)
tk.Button(root,text='(',command=func_LK,width=4,height=1,bg='#00FF7F').grid(row=6,column=1,padx=1,pady=1)
tk.Button(root,text='点',command=func_POT,width=4,height=1,bg='#00EE00').grid(row=6,column=2,padx=1,pady=1)
tk.Button(root,text=')',command=func_RK,width=4,height=1,bg='#00FF7F').grid(row=6,column=3,padx=1,pady=1)
root.mainloop()
