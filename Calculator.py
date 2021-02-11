from tkinter import *

window=Tk()
window.title('Simple Calculator')
window.geometry('250x170')
window.resizable(width=False,height=False)

#**************FRAME****************
frame_1=Frame(window,height=100,width=300)
frame_1.configure(bg='lightblue')
frame_1.pack(side=TOP)

frame_2=Frame(window,height=100,width=300)
frame_2.configure(bg='lightblue')
frame_2.pack(side=TOP)

frame_3=Frame(window,height=100,width=300)
frame_3.configure(bg='lightblue')
frame_3.pack(side=TOP)

frame_4=Frame(window,height=100,width=300)
frame_4.configure(bg='lightblue')
frame_4.pack(side=TOP)

frame_5=Frame(window,height=100,width=300)
frame_5.configure(bg='lightblue')
frame_5.pack(side=TOP)
#**************FUNCTION****************
def plus():
    pass

#**************BUTTON****************
btn_7=Button(frame_1,text='7',width=5,highlightbackground='lightblue',textvariable='7')
btn_7.grid(sticky='w',padx=2,pady=5,row=0,column=0)
btn_8=Button(frame_1,text='8',width=5,highlightbackground='lightblue')
btn_8.grid(sticky='w',padx=2,pady=5,row=0,column=1)
btn_9=Button(frame_1,text='9',width=5,highlightbackground='lightblue')
btn_9.grid(sticky='w',padx=2,pady=5,row=0,column=2)
btn_div=Button(frame_1,text='/',width=5,highlightbackground='lightblue')
btn_div.grid(sticky='w',padx=2,pady=5,row=0,column=3)
btn_mod=Button(frame_1,text='%',width=5,highlightbackground='lightblue')
btn_mod.grid(sticky='w',padx=2,pady=5,row=0,column=4)

btn_4=Button(frame_2,text='4',width=5,highlightbackground='lightblue')
btn_4.grid(sticky='w',padx=2,pady=5,row=0,column=0)
btn_5=Button(frame_2,text='5',width=5,highlightbackground='lightblue')
btn_5.grid(sticky='w',padx=2,pady=5,row=0,column=1)
btn_6=Button(frame_2,text='6',width=5,highlightbackground='lightblue')
btn_6.grid(sticky='w',padx=2,pady=5,row=0,column=2)
btn_multi=Button(frame_2,text='*',width=5,highlightbackground='lightblue')
btn_multi.grid(sticky='w',padx=2,pady=5,row=0,column=3)
btn_re=Button(frame_2,text='1/x',width=5,highlightbackground='lightblue')
btn_re.grid(sticky='w',padx=2,pady=5,row=0,column=4)

btn_1=Button(frame_3,text='1',width=5,highlightbackground='lightblue')
btn_1.grid(sticky='w',padx=2,pady=5,row=0,column=0)
btn_2=Button(frame_3,text='2',width=5,highlightbackground='lightblue')
btn_2.grid(sticky='w',padx=2,pady=5,row=0,column=1)
btn_3=Button(frame_3,text='3',width=5,highlightbackground='lightblue')
btn_3.grid(sticky='w',padx=2,pady=5,row=0,column=2)
btn_minus=Button(frame_3,text='-',width=5,highlightbackground='lightblue')
btn_minus.grid(sticky='w',padx=2,pady=5,row=0,column=3)
btn_plus=Button(frame_3,text='+',width=5,highlightbackground='lightblue',command=lambda:plus())
btn_plus.grid(sticky='w',padx=2,row=0,column=4)

btn_0=Button(frame_4,text='0',width=5,highlightbackground='lightblue')
btn_0.grid(sticky='w',padx=2,pady=5,row=0,column=0)
btn_dot=Button(frame_4,text='.',width=5,highlightbackground='lightblue')
btn_dot.grid(sticky='w',padx=2,pady=5,row=0,column=1)
btn_result=Button(frame_4,text='=',width=19,highlightbackground='lightblue')
btn_result.grid(sticky='w',padx=2,pady=5,row=0,column=2)

btn_out=Entry(frame_5,text=' ',width=40,highlightbackground='lightblue')
btn_out.grid(sticky='w',padx=2,pady=5,row=0,column=2)


window.mainloop()
