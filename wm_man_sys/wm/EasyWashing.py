import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm

from MANSYS import db
from MANSYS.models import User, Server1, Server2, Server3, Server4

class EasyWashing:
	def __init__(self,master):
		self.master =  master
		self.master.title("Easy Washing")
		self.master_width=1100
		self.master_height=700
		self.master.geometry("{}x{}".format(self.master_width,self.master_height))
		self.master.minsize(self.master_width,self.master_height)
		self.create_mainframe()

	def create_mainframe(self):
		self.frameRowNumb=50
		self.frameColNumb=40
		self.frame=Frame(self.master,bg="white")
		self.frame.grid(row=0,column=10,rowspan=self.frameRowNumb,
						columnspan=self.frameColNumb,
						sticky=N+S+E+W)
		for rows in range(self.frameRowNumb):                                                     
			Grid.rowconfigure(self.frame,rows,weight=1,uniform="foo")                            
			for cols in range(self.frameColNumb):                                                   
				Grid.columnconfigure(self.frame,cols,weight=1,uniform="foo")

		self.rvar = IntVar()
		self.rvar.set = 1
		self.r1  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=1, text='09:00')
		self.r2  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=2, text='09:40')
		self.r3  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=3, text='10:20')
		self.r4  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=4, text='11:00')
		self.r5  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=5, text='11:40')
		self.r6  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=6, text='12:20')
		self.r7  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=7, text='13:00')
		self.r8  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=8, text='13:40')
		self.r9  = Radiobutton(self.frame, bg="white", variable=self.rvar, value=9, text='14:20')
		self.r10 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=10, text='15:00')
		self.r11 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=11, text='15:40')
		self.r12 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=12, text='16:20')
		self.r13 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=13, text='17:00')
		self.r14 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=14, text='17:40')
		self.r15 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=15, text='18:20')
		self.r16 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=16, text='19:00')
		self.r17 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=17, text='19:40')
		self.r18 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=18, text='20:20')
		self.r19 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=19, text='21:00')
		self.r20 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=20, text='21:40')
		self.r21 = Radiobutton(self.frame, bg="white", variable=self.rvar, value=21, text='22:20')
		
		rbtn = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7,
				self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14,
				self.r15, self.r16, self.r17, self.r18, self.r19, self.r20, self.r21]

		idx = 0
		top_padding = 6
		rows = 2
		cols = 2
		for row in range(0,3*rows,rows):
			for col in range(0,7*cols,cols):
				rbtn[idx].bg = "white"
				self.config(rbtn[idx])
				rbtn[idx].grid(row=row+top_padding,column=col,rowspan=rows,columnspan=cols)
				idx+=1

		self.svar = IntVar()
		self.s1 = Radiobutton(self.frame, bg="white", variable=self.svar, value=1, text='Server 1')
		self.s2 = Radiobutton(self.frame, bg="white", variable=self.svar, value=2, text='Server 2')
		self.s3 = Radiobutton(self.frame, bg="white", variable=self.svar, value=3, text='Server 3')
		self.s4 = Radiobutton(self.frame, bg="white", variable=self.svar, value=4, text='Server 4')

		self.s1.grid(row=20, column=2)
		self.s2.grid(row=20, column=4)
		self.s3.grid(row=20, column=6)
		self.s4.grid(row=20, column=8)
		self.config(self.s1)
		self.config(self.s2)
		self.config(self.s3)
		self.config(self.s4)

		self.select_btn = ttk.Button(self.frame, text='select', command=self.select)
		self.select_btn.grid(row=22,column=6)
		self.config(self.select_btn)

	def select(self):
		s = int(self.svar.get())
		t = int(self.rvar.get())

		servers = {
			1:Server1.query.filter_by(id=1).first(),
			2:Server2.query.filter_by(id=1).first(),
			3:Server3.query.filter_by(id=1).first(),
			4:Server4.query.filter_by(id=1).first()
		}

		user = User.query.filter_by(username='Marc').first()
		if user is not None:
			if t==1:
				m = servers[s].t1
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t1 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==2:
				m = servers[s].t2
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t2 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==3:
				m = servers[s].t3
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t3 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==4:
				m = servers[s].t4
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t4 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==5:
				m = servers[s].t5
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t5 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==6:
				m = servers[s].t6
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t6 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==7:
				m = servers[s].t7
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t7 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==8:
				m = servers[s].t8
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t8 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==9:
				m = servers[s].t9
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t9 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==10:
				m = servers[s].t10
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t10 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==11:
				m = servers[s].t11
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t11 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==12:
				m = servers[s].t12
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t12 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==13:
				m = servers[s].t13
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t13 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==14:
				m = servers[s].t14
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t14 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==15:
				m = servers[s].t15
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t15 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==16:
				m = servers[s].t16
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t16 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==17:
				m = servers[s].t17
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t17 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==18:
				m = servers[s].t18
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t18 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==19:
				m = servers[s].t19
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t19 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==20:
				m = servers[s].t20
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t20 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
			elif t==21:
				m = servers[s].t21
				if m == True:
					user.time_slot += f'({s},{t})'
					servers[s].t21 = False
					db.session.commit()
					tkm.showinfo('Successfully registered',
						f'You successfully registered!\n{user.time_slot}')
				else:
					tkm.showinfo('Time Slot Taken','This time slot is already taken')
		else:
			tkm.showerror('Unknown user','Please login to select a time slot')

	def config(self,widget):
		Grid.rowconfigure(widget,0,weight=1)
		Grid.columnconfigure(widget,0,weight=1)

def main():
	root = Tk()
	run  = EasyWashing(root) 
	root.mainloop( )        

if __name__=="__main__":
	main()