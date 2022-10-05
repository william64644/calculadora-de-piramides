from tkinter import *

from back_end import Data_Model, Model

dt = Data_Model()
model = Model(dt)

window = Tk()
window.title("Calculadora de pirâmides")
window.geometry('300x330')
window.configure(background = "grey")


	# Plaing Text Labels #
aresta_base = Label(window ,text = "Aresta da base").grid(row = 0,column = 0)
aresta_lateral = Label(window ,text = "Aresta da lateral").grid(row = 1,column = 0)
apotema_base = Label(window ,text = "Apotema da base").grid(row = 2,column = 0)
apotema_lateral = Label(window ,text = "Apotema da lateral").grid(row = 3,column = 0)
altura = Label(window ,text = "Altura").grid(row = 4,column = 0)
area_base = Label(window ,text = "Area da base").grid(row = 5,column = 0)
area_face_lateral = Label(window ,text = "Area da face lateral").grid(row = 6,column = 0)
area_lateral = Label(window ,text = "Area da lateral").grid(row = 7,column = 0)
area_total = Label(window ,text = "Area total").grid(row = 8,column = 0)
volume = Label(window ,text = "Volume").grid(row = 9,column = 0)
quantidade_laterais = Label(window ,text = "Quantidade laterais").grid(row = 10,column = 0)


	# Plaing Text Inputs #
entry_aresta_base = Entry(window)
entry_aresta_base.grid(row = 0,column = 1)

entry_aresta_lateral = Entry(window)
entry_aresta_lateral.grid(row = 1,column = 1)

entry_apotema_base = Entry(window)
entry_apotema_base.grid(row = 2,column = 1)

entry_apotema_lateral = Entry(window)
entry_apotema_lateral.grid(row = 3,column = 1)

entry_altura = Entry(window)
entry_altura.grid(row = 4,column = 1)

entry_area_base = Entry(window)
entry_area_base.grid(row = 5,column = 1)

entry_area_face_lateral = Entry(window)
entry_area_face_lateral.grid(row = 6,column = 1)

entry_area_lateral = Entry(window)
entry_area_lateral.grid(row = 7,column = 1)

entry_area_total = Entry(window)
entry_area_total.grid(row = 8,column = 1)

entry_volume = Entry(window)
entry_volume.grid(row = 9,column = 1)

entry_quantidade_laterais = Entry(window)
entry_quantidade_laterais.grid(row = 10,column = 1)


def calculate():
	#get data from entries
	try:
		dt.aresta_base = float(entry_aresta_base.get())
	except:
		pass
	try:
		dt.aresta_lateral = float(entry_aresta_lateral.get())
	except:
		pass
	try:
		dt.apotema_base = float(entry_aresta_base.get())
	except:
		pass
	try:
		dt.apotema_lateral = float(entry_apotema_lateral.get())
	except:
		pass
	try:
		dt.altura = float(entry_altura.get())
	except:
		pass
	try:
		dt.area_base = float(entry_area_base.get())
	except:
		pass
	try:
		dt.area_face_lateral = float(entry_area_face_lateral.get())
	except:
		pass
	try:
		dt.area_lateral = float(entry_area_lateral.get())
	except:
		pass
	try:
		dt.area_total = float(entry_area_total.get())
	except:
		pass
	try:
		dt.volume = float(entry_volume.get())
	except:
		pass
	try:
		dt.quantidade_laterais = float(entry_quantidade_laterais.get())
	except:
		pass


	model.run()


   #show data
	entry_aresta_base.delete(0, END)
	entry_aresta_lateral.delete(0, END)
	entry_apotema_base.delete(0, END)
	entry_apotema_lateral.delete(0, END)
	entry_altura.delete(0, END)
	entry_area_base.delete(0, END)
	entry_area_face_lateral.delete(0, END)
	entry_area_lateral.delete(0, END)
	entry_area_total.delete(0, END)
	entry_volume.delete(0, END)
	entry_quantidade_laterais.delete(0, END)

	entry_aresta_base.insert(string=str(dt.aresta_base), index=0)
	entry_aresta_lateral.insert(string=str(dt.aresta_lateral), index=0)
	entry_apotema_base.insert(string=str(dt.apotema_base), index=0)
	entry_apotema_lateral.insert(string=str(dt.apotema_lateral), index=0)
	entry_altura.insert(string=str(dt.altura), index=0)
	entry_area_base.insert(string=str(dt.area_base), index=0)
	entry_area_face_lateral.insert(string=str(dt.area_face_lateral), index=0)
	entry_area_lateral.insert(string=str(dt.area_lateral), index=0)
	entry_area_total.insert(string=str(dt.area_total), index=0)
	entry_volume.insert(string=str(dt.volume), index=0)
	entry_quantidade_laterais.insert(string=str(dt.quantidade_laterais), index=0)

def clear():

	dt.aresta_base = None
	dt.aresta_lateral = None
	dt.apotema_base = None
	dt.apotema_lateral = None
	dt.altura = None
	dt.area_base = None
	dt.area_face_lateral = None
	dt.area_lateral = None
	dt.area_total = None
	dt.volume = None
	dt.quantidade_laterais = None

	entry_aresta_base.delete(0, END)
	entry_aresta_lateral.delete(0, END)
	entry_apotema_base.delete(0, END)
	entry_apotema_lateral.delete(0, END)
	entry_altura.delete(0, END)
	entry_area_base.delete(0, END)
	entry_area_face_lateral.delete(0, END)
	entry_area_lateral.delete(0, END)
	entry_area_total.delete(0, END)
	entry_volume.delete(0, END)
	entry_quantidade_laterais.delete(0, END)


calculate_btn = Button(window ,text="Calcular", command=calculate).grid(row = 11, column = 1)

clear_btn = Button(window ,text="Limpar", command=clear).grid(row = 11, column=0)






for rowi in range(11):
	window.grid_rowconfigure(rowi, minsize=25)

window.grid_rowconfigure(11, minsize=50)

window.grid_columnconfigure(0, minsize=140)


window.mainloop()


#asd

