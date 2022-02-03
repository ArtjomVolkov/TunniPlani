from tkinter import *
from tkinter.messagebox import *
import time
import os
def failist_sõnastikusse():
	tund_kirjeldus={}
	file=open("Tunnid_kirjeldused.txt","r")
	for line in file:
		tund,kirjeldus=line.strip().split(":")
		tund_kirjeldus[tund.strip()]=kirjeldus.strip()
	file.close()
	print(tund_kirjeldus)
	return tund_kirjeldus

tund_kirjeldus=failist_sõnastikusse()
def kirjeldus_aknasse(t:str,tit:str):
	if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
		alam_aken=Toplevel()
		lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
		alam_aken.geometry("400x400")
		c=Canvas(alam_aken,height=500,width=500)
		file=PhotoImage(file=t)
		c.create_image(10,10,image=file,anchor=NW)
		c.pack()
		alam_aken.mainloop()
	else:
		showinfo("Vastus","Kui ei taha,siis ei taha!")

j=0
def veel():
	global j
	if j==0:
		aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-350))
		btn_veel.config(text="+")
		j=1
	else:
		aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+350))
		btn_veel.config(text="-")
		j=0
aken=Tk()
aken.geometry("1100x460")
aken.title("Tunniplan")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(2,11,2):
	Ep=Label(aken,text=p[j],font="Arial 20",relief="groove").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
	j+=1
keel=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
k=0
for i in range(1,12,1):
	Ek=Label(aken,text=keel[k],font="Arial 6",relief="flat").grid(row=1,column=i,rowspan=2,sticky=N)
	k+=1
Rp=Label(aken,text="TARpv21",font="Arial 16",relief="flat").grid(row=0,column=0,sticky=N+S+W+E)
Ep=Label(aken,text="",relief="flat").grid(row=1,column=0,rowspan=1,sticky=N+S+W+E)
for i in range(11):
	tn="t"+str(i)
	tn=Label(aken,text=i,font="Arial 20",relief="groove").grid(row=0,column=i+1,sticky=N+S+W+E)

btn_veel=Button(aken,text="+", font="Calibri 26",bg="green",command=veel)
btn_veel.place(x=1060,y=400)
#Понедельник
t1=Button(aken,text="Multimeedia",command=lambda:kirjeldus_aknasse("mult.gif","Multimeedia"),font="Arial 15",relief="groove",bg="#3399FF").grid(row=2,column=2,columnspan=2,sticky=N+S+W+E)
t1_=Button(aken,text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("11.gif","Programmeerimise alused"),font="Arial 15",relief="groove",bg="#33FFFF").grid(row=3,column=2,columnspan=3,sticky=N+S+W+E)
t2=Button(aken,text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("11.gif","Programmeerimise alused"),font="Arial 15",relief="groove",bg="#33FFFF").grid(row=2,column=5,columnspan=3,sticky=N+S+W+E)
t2_=Button(aken,text="Multimeedia",command=lambda:kirjeldus_aknasse("mult.gif","Multimeedia"),font="Arial 15",relief="groove",bg="#3399FF").grid(row=3,column=5,columnspan=2,sticky=N+S+W+E)
t3=Button(aken,text="Rühmaju\nhataja\ntund",font="Arial 15",relief="groove",bg="#33FFFF").grid(row=2,column=8,rowspan=2,sticky=N+S+W+E)
o=Label(aken,text="",width=7,height=1,font="Arial 15",relief="flat").grid(row=2,column=1,sticky=N+S+W+E)
o1=Label(aken,text="",width=7,height=1,font="Arial 15",relief="flat").grid(row=2,column=11,sticky=N+S+W+E)
#Вторник
t4=Button(aken,text="Inglise keel",font="Arial 15",relief="groove",bg="#FFFFCC").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
t4_=Button(aken,text="Inglise keel",font="Arial 15",relief="groove",bg="#FF99FF").grid(row=5,column=2,columnspan=2,sticky=N+S+W+E)
t5=Button(aken,text="Operatsiooni\nsüsteemide \nalused",font="Arial 15",relief="groove",bg="#FF33FF").grid(row=4,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
t6=Button(aken,text="Kehaline\nkasvatus",font="Arial 15",relief="groove",bg="#FF99CC").grid(row=4,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
t7=Button(aken,text="Eesti keel",font="Arial 15",relief="groove",bg="#D75898").grid(row=4,column=9,sticky=N+S+W+E)
t7_=Button(aken,text="Eesti keel",font="Arial 15",relief="groove",bg="#A0A0A0").grid(row=5,column=9,sticky=N+S+W+E)
t8=Button(aken,text="Inimese\nõpetus",font="Arial 15",relief="groove",bg="#FFFFCC").grid(row=4,column=10,rowspan=2,sticky=N+S+W+E)
#Среда
t9=Button(aken,text="Multimeedia",font="Arial 15",relief="groove",bg="#3399FF").grid(row=7,column=2,columnspan=3,sticky=N+S+W+E)
t9_=Button(aken,text="Programmeerimise alused",font="Arial 15",relief="groove",bg="#33FFFF").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
t10=Button(aken,text="Multimeedia",font="Arial 15",relief="groove",bg="#3399FF").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
t11=Button(aken,text="Programmeerimise alused",font="Arial 15",relief="groove",bg="#33FFFF").grid(row=7,column=6,columnspan=3,sticky=N+S+W+E)
t12=Button(aken,text="Kunstiained",font="Arial 15",relief="groove",bg="#990099").grid(row=6,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)
#Четверг
t13=Button(aken,text="Andmebaasisüstee\mide alused",font="Arial 15",relief="groove",bg="#E22E2E").grid(row=8,column=2,columnspan=5,rowspan=2,sticky=N+S+W+E)
t14=Button(aken,text="Inimese\nõpetus",font="Arial 15",relief="groove",bg="#FFFFCC").grid(row=8,column=7,rowspan=2,sticky=N+S+W+E)
t15=Button(aken,text="Eesti keel",font="Arial 15",relief="groove",bg="#D75898").grid(row=8,column=8,sticky=N+S+W+E)
t15_=Button(aken,text="Eesti keel",font="Arial 15",relief="groove",bg="#A0A0A0").grid(row=9,column=8,sticky=N+S+W+E)
#Пятница
t16=Button(aken,text="Keel ja kirjandus",font="Arial 15",relief="groove",bg="#FFFF33").grid(row=10,column=3,rowspan=2,columnspan=2,sticky=N+S+W+E)
t17=Button(aken,text="Matemaatika",font="Arial 15",relief="groove",bg="#E1ACAC").grid(row=10,column=6,rowspan=2,columnspan=2,sticky=N+S+W+E)
t18=Button(aken,text="Suhtlemine ja\nklienditeenindus",font="Arial 15",relief="groove",bg="#B266FF").grid(row=10,column=8,rowspan=2,columnspan=2,sticky=N+S+W+E)
t19=Button(aken,text="Inimese\nõpetus",font="Arial 15",relief="groove",bg="#FFFFCC").grid(row=10,column=10,rowspan=2,sticky=N+S+W+E)
i1=PhotoImage(file="vladimir-putin-wink.gif")
r1=Label(aken,image=i1)
r1.place(x=160,y=480)
frameCnt = 44
frames = [PhotoImage(file='mult.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    aken.after(100, update, ind)
label = Label(aken)
label.place(x=500,y=500)
aken.after(0, update, 0)
aken.mainloop()