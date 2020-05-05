from tkinter import *
import csv

root = Tk()
root.title("Text to Check")

#Menu bar (just gonna have saving and loading for now)

menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_command(label="Save", command=lambda:saver())
menubar.add_command(label="Load", command=lambda:loader())
root.config(menu=menubar)


#First Column: Task Entry

lbl = Label(root, text="Put Tasks Here", font=("Arial", 18), fg="white", bg="green", width=15)
lbl.grid(column=0, row=0)

todo = Text(root, width=20, height=20, font=("Arial", 12))
todo.grid(column=0, row=1)
 
ent_but = Button(root, text="Save to Tasklist", command=lambda:getter())
ent_but.grid(column=0, row=2)

#Second Column: Checklist

slbl = Label(root, text="To Do List", font=("Arial", 18), fg="white", bg="red", width=15)
slbl.grid(column=1, row=0)

scheck = Frame(root)
scheck.grid(column=1, row=1)

sent = Button(root, text="Clear Completed Tasks", command=lambda:deleter())
sent.grid(column=1, row=2)

#gets the user input after they click the button to add to the checklist

class Logging:
	log_count = 0

variable_list = []	
checklist_name = []

def getter():
	input = todo.get("1.0", 'end-1c')
	var = IntVar()
	cb = Checkbutton(scheck, text=input, font=("Arial", 12), offvalue=0, onvalue=1, variable=var)
	cb.grid(row=Logging.log_count)
	checklist_name.append(input)
	variable_list.append(var)
	Logging.log_count += 1

#deletes all completed tasks

def deleter():
	global variable_list, checklist_name
	
	vl2 = [variable_list[i] for i in range(len(variable_list)) if variable_list[i].get() == 0]
	cl2 = [checklist_name[i] for i in range(len(variable_list)) if variable_list[i].get() == 0]
	
	variable_list = vl2
	checklist_name = cl2

	for child in scheck.winfo_children():
		child.destroy()
	
	for i in range(len(variable_list)):
		var = variable_list[i]
		cb = Checkbutton(scheck, text=checklist_name[i], font=("Arial", "12"), offvalue=0, onvalue=1, variable=var)
		cb.grid(row=i)
		
	Logging.log_count = len(variable_list)
		

#Saves the tasklist file

def saver():
	global variable_list, checklist_name
	file = open(r"C:\Users\User\Documents\PythonWork\savedlist.txt", "w")
	for i in range(len(variable_list)):
		if i != range(len(variable_list)):
			file.write(str(variable_list[i].get()) + "," + str(checklist_name[i]) + "\n")
		else:
			file.write(str(variable_list[i].get()) + "," + str(checklist_name[i]))
	file.close()
	return
	
#Loads the tasklist file

def loader():
	global variable_list, checklist_name
	
	vl = []
	cl = []
	
	file = open(r"C:\Users\User\Documents\PythonWork\savedlist.txt", "r")
	readCSV = csv.reader(file, delimiter=",")
	for row in readCSV:
		vl.append(int(row[0]))
		cl.append(row[1])
	file.close()
	
	for child in scheck.winfo_children():
		child.destroy()
	
	new_vl = []
	
	for i in range(len(vl)):
		var = IntVar()
		if vl[i] == 0:
			cb = Checkbutton(scheck, text=cl[i], font=("Arial", "12"), offvalue=0, onvalue=1, variable=var)
			cb.grid(row=i)
			cb.deselect()
			new_vl.append(var)
		elif vl[i] == 1:
			cb = Checkbutton(scheck, text=cl[i], font=("Arial", "12"), offvalue=0, onvalue=1, variable=var)
			cb.grid(row=i)
			cb.select()
			new_vl.append(var)
	
	variable_list = new_vl
	checklist_name = cl
	Logging.log_count = len(vl)

root.mainloop()