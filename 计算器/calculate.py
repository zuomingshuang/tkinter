import re

#加法计算
def sub_cal(mystr):
    result=0
    mystr=re.findall(r'[\+\-]?\d+\.?\d*',mystr)
    for one in mystr:
        result+=float(one)
    return result

#乘除法都可以计算
def ccf_cal(mystr):
    result=0
    try:
        #如果有*或/，则判断是*还是/然后相应的计算结果
        temp_str=re.search(r'\-?\d+\.?\d*[*/]\-?\d+\.?\d*',mystr).group()
        
        if '*' in temp_str:
            num_list=temp_str.split('*')
            result=float(num_list[0])*float(num_list[1])
        else:
            num_list=temp_str.split('/')
            result=float(num_list[0])/float(num_list[1])
        mystr=mystr.replace(temp_str,str(result))
            
    #如果没有*或/，则调用sub_cal方法
    except:
        result=sub_cal(mystr)
        mystr=str(result)
    return mystr

#模拟eval的功能
def myeval(mystr):
    while True:
        mystr=ccf_cal(mystr)
        if  not re.search(r'[*/]',mystr):
            mystr=ccf_cal(mystr)
            break
    return float(mystr)


#去掉最里层的扣号
def remove_kh(mystr):
    temp_str=re.search(r'\([^()]+\)',mystr).group()
    mystr=mystr.replace(temp_str,str(myeval(temp_str)))
    return mystr
        
def main(mystr):
     while True:
        if re.search(r'\([^()]+\)',mystr):
            mystr=remove_kh(mystr)
            continue
        result=myeval(mystr)
        return result
        break
                      

            
       
       
        










