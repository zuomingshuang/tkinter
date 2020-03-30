import tkinter as tk
import pymysql
import pandas as pd
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,askdirectory
import sqlalchemy
import pandas as pd

class Mysql_handle():
    def connect_db(self):
        try:
            conn=pymysql.connect(E11.get(),E12.get(),E13.get(),E14.get())
            self.conn=conn
            self.cursor=conn.cursor()
            self.engine=sqlalchemy.create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
                E12.get(),E13.get(),E11.get(),'3306',E14.get()
            ))
            L15.configure(text='已连接到数据库：%s'%E14.get(),fg='blue')
            self.show_tables()
        except Exception as e:
            messagebox.showerror('数据库连接','连接时错现错误：%s'%e)

    def close_db(self):
        try:
            self.conn.close()
            Lb.delete(0,tk.END)
            L15.configure(text='数据库未连接!',fg='red')
        except Exception as e:
            messagebox.showerror('断开数据库','断开数据库时出现错误：%s'%e)

    def show_tables(self):
        self.cursor.execute('show tables')
        for table in self.cursor.fetchall():
            Lb.insert(tk.END,table[0])

    def desc_table(self):
        cur_table = Lb.get(Lb.curselection()[0])
        self.cursor.execute('desc %s'%cur_table)
        T1.delete(1.0, tk.END)
        for one in self.cursor.fetchall():
            T1.insert(tk.END,str(one)+'\n')

    def table_data(self):
        cur_table = Lb.get(Lb.curselection()[0])
        self.cursor.execute('select * from %s'%cur_table)
        T1.delete(1.0,tk.END)
        for one in self.cursor.fetchall():
            T1.insert(tk.END,str(one)+'\n')

    def load(self,file_name):
        try:
            cur_table = Lb.get(Lb.curselection()[0])
            # self.cursor.execute('select * from %s into outfile "%s"'%(cur_table,file_name))
            dt=pd.read_sql('select * from %s'%cur_table,con=self.conn)
            if myformat.get()=='.csv':
                dt.to_csv(file_name,index=False,encoding='utf8')
                messagebox.showinfo('导出成功', '文件已成功导出')
            elif myformat.get() =='.xlsx':
                dt.to_excel(file_name, index=False,encoding='utf8')
                messagebox.showinfo('导出成功','文件已成功导出')
        except Exception as e:
            messagebox.showerror('导出错误','错误：%s'%e)

    def loadin_data(self):
        try:
            file=E32.get()
            table_name=file.split(r'/')[-1].split(r'.')[0]
            dt=pd.read_excel(file)
            dt.to_sql(name=table_name,con=self.engine,index=False,if_exists='append')
            messagebox.showinfo('导入成功','文件已成功导入')
        except Exception as e:
            messagebox.showerror('错误','导入时发生错误:%s\n请修改文件名后重新导入试试'%e)


###############################################################################
Mh=Mysql_handle()
root=tk.Tk()
root.title('Mysql')
#F1  数据库连接和断开
F1=tk.Frame(root)
F1.grid(row=0,column=0)
L10=tk.Label(F1,text='数据库连接',font=('微软雅黑',15))
L10.grid(row=0,column=0,columnspan=2)
#主机
L11=tk.Label(F1,text='主机：',font=('微软雅黑',12))
E11=tk.Entry(F1,font=('微软雅黑',12))
L11.grid(row=1,column=0,sticky=tk.E,pady=5)
E11.grid(row=1,column=1)
#用户名
L12=tk.Label(F1,text='用户名：',font=('微软雅黑',12))
E12=tk.Entry(F1,font=('微软雅黑',12))
L12.grid(row=2,column=0,sticky=tk.E,pady=5)
E12.grid(row=2,column=1)
#密码
L13=tk.Label(F1,text='密码：',font=('微软雅黑',12))
E13=tk.Entry(F1,show='*',font=('微软雅黑',12))
L13.grid(row=3,column=0,sticky=tk.E,pady=5)
E13.grid(row=3,column=1)
#数据库
L14=tk.Label(F1,text='数据库：',font=('微软雅黑',12))
E14=tk.Entry(F1,font=('微软雅黑',12))
L14.grid(row=4,column=0,sticky=tk.E,pady=5)
E14.grid(row=4,column=1)

#连接数据库
tk.Button(F1,text='连接',fg='red',width=6,command=Mh.connect_db).grid(row=5,column=0,pady=20)
#断开数据库
tk.Button(F1,text='断开',fg='blue',width=6,command=Mh.close_db).grid(row=5,column=1,pady=20,sticky=tk.W)
L15=tk.Label(F1,text='数据库未连接!',fg='red')
L15.grid(row=6,columnspan=2,sticky=tk.W)

########################表操作###############################
F2=tk.Frame(root)
F2.grid(row=0,column=1,padx=10)
#tables列表
L21=tk.Label(F2,text='tables',font=('微软雅黑',15))
L21.grid(row=0,column=0,sticky=tk.N)
Lb=tk.Listbox(F2,height=22)
Lb.grid(row=1,column=0,sticky=tk.W)
tk.Button(F2,text='查看表结构',command=Mh.desc_table,width=8,bg='green',fg='white',font=('微软雅黑',12)).grid(row=2,column=0)
tk.Button(F2,text='查看数据',command=Mh.table_data,width=8,bg='blue',fg='white',font=('微软雅黑',12)).grid(row=3,column=0)

###################查看表结构或数据###############################
L22=tk.Label(F2,text='查询结果',font=('微软雅黑',15))
L22.grid(row=0,column=1,sticky=tk.N)
T1=tk.Text(F2,height=30,width=50)
T1.grid(row=1,column=1)

################导出和导入#####################################
#导出数据
F3=tk.Frame(root)
F3.grid(row=0,column=2)
L31=tk.Label(F3,text='导出格式:',font=('微软雅黑',15))
L31.grid(row=0,column=0)
myformat=tk.StringVar()
R31=tk.Radiobutton(F3,variable=myformat,value='.csv',text='.csv',font=('微软雅黑',12))
R31.grid(row=1,column=0)
R32=tk.Radiobutton(F3,variable=myformat,value='.xlsx',text='.xlsx',font=('微软雅黑',12))
R32.grid(row=1,column=1,sticky=tk.W)
L32=tk.Label(F3,text='选择路径',font=('微软雅黑',12))
L32.grid(row=2,column=0,sticky=tk.E)
def load_data():
    try:
        cur_table = Lb.get(Lb.curselection()[0])
    except:
        pass
    dir=askdirectory()
    try:
        if dir:
            file_name = dir + '/' + cur_table + myformat.get()
            Mh.load(file_name)
    except:
        messagebox.showerror('错误','请选择一个数据表')

E31=tk.Entry(F3,font=('微软雅黑',12))
E31.grid(row=2,column=1)
B31=tk.Button(F3,text='导出',width=6,bg='blue',fg='white',font=('微软雅黑',12),command=load_data)
B31.grid(row=2,column=2)

#导入Excel数据
L33=tk.Label(F3,text='导入Excel文件：',font=('微软雅黑',14))
L33.grid(row=3,column=0,pady=20)
L34=tk.Label(F3,text='选择文件',font=('微软雅黑',12))
L34.grid(row=4,column=0,sticky=tk.E)
E32=tk.Entry(F3,font=('微软雅黑',12))
E32.grid(row=4,column=1)
def get_file(event):
    file=askopenfilename()
    E32.delete(0,tk.END)
    E32.insert(tk.END,file)
E32.bind('<Double-Button-1>',get_file)
B32=tk.Button(F3,text='导入',width=6,bg='red',fg='white',command=Mh.loadin_data,font=('微软雅黑',12))
B32.grid(row=4,column=2)

root.mainloop()

