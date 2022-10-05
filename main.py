from math import sqrt


def are_known(*args):
	for num in args:
		if num == None:
			return False
	return True


class Data_Model():
	def __init__(self):
		self.aresta_base = None
		self.aresta_lateral = None
		self.apotema_base = None
		self.apotema_lateral = None
		self.altura = None
		self.area_base = None
		self.area_face_lateral = None
		self.area_lateral = None
		self.area_total = None
		self.volume = None
		self.quantidade_laterais = None
		
		self.calculated_something = False
		
	def show(self):
		print(f'Aresta base = {self.aresta_base}')
		print(f'Aresta lateral = {self.aresta_lateral}')
		print(f'Apotema base = {self.apotema_base}')
		print(f'Apotema lateral = {self.apotema_lateral}')
		print(f'Altura = {self.altura}')
		print(f'Area base = {self.area_base}')
		print(f'Area face lateral = {self.area_face_lateral}')
		print(f'Area lateral = {self.area_lateral}')
		print(f'Area total = {self.area_total}')
		print(f'Volume = {self.volume}')
		print(f'Quantidade laterais = {self.quantidade_laterais}')


class Model():
	def __init__(self, data_model):
		self.dt = data_model
		self.show = data_model.show


	def solve_aresta_base(self):
		if dt.aresta_base == None:
			if are_known(dt.area_base, dt.apotema_base, dt.quantidade_laterais):
				dt.aresta_base = (2 * dt.area_base) / (dt.apotema_base * dt.quantidade_laterais)
				dt.calculated_something = True
				return

	def solve_aresta_lateral(self):
		if dt.aresta_lateral == None:
			if are_known(dt.apotema_lateral, dt.apotema_base):
				dt.aresta_lateral = sqrt(dt.apotema_lateral ** 2 + (dt.apotema_base / 2) ** 2)
				dt.calculated_something = True
				return

	def solve_apotema_base(self):
		if dt.apotema_base == None:
			if are_known(dt.area_base, dt.aresta_base, dt.quantidade_laterais):
				dt.apotema_base = (2*dt.area_base) / (dt.aresta_base * dt.quantidade_laterais)
				dt.calculated_something = True
				return
		
	def solve_apotema_lateral(self):
		if dt.apotema_lateral == None:
			if are_known(dt.apotema_base, dt.altura):
				dt.apotema_lateral = sqrt(dt.apotema_base ** 2 + dt.altura ** 2)
				dt.calculated_something = True
				return
			
	def solve_altura(self):
		if dt.altura == None:
			if are_known(dt.apotema_lateral, dt.apotema_base):
				dt.altura = sqrt(dt.apotema_lateral ** 2 - dt.apotema_base ** 2)
				dt.calculated_something = True
				return
		
	def solve_area_base(self):
		if dt.area_base == None:
			if are_known(dt.aresta_base, dt.apotema_base, dt.quantidade_laterais):
				dt.area_base = dt.aresta_base * dt.apotema_base / 2 * dt.quantidade_laterais
				dt.calculated_something = True
				return
			
	def solve_area_face_lateral(self):
		if dt.area_face_lateral == None:
			if are_known(dt.apotema_lateral, dt.apotema_base):
				dt.area_face_lateral = dt.apotema_lateral * dt.apotema_base / 2
				dt.calculated_something = True
				return
			
	def solve_area_lateral(self):
		if dt.area_lateral == None:
			if are_known(dt.aresta_base, dt.apotema_lateral, dt.quantidade_laterais):
				dt.area_lateral = dt.aresta_base * dt.apotema_lateral / 2 * dt.quantidade_laterais
				dt.calculated_something = True
				return
		
	def solve_area_total(self):
		if dt.area_total == None:
			if are_known(dt.area_lateral, dt.area_base):
				dt.area_total = dt.area_lateral + dt.area_base
				dt.calculated_something = True
				return
		
	def solve_volume(self):
		if dt.volume == None:
			if are_known(dt.area_base, dt.altura):
				dt.volume = dt.area_base * dt.altura / 3
				dt.calculated_something = True
				return
			
	def solve_quantidade_laterais(self):
		if dt.quantidade_laterais == None:
			if are_known(dt.area_base, dt.aresta_base, dt.apotema_base):
				dt.quantidade_laterais = (2*dt.area_base) / (dt.aresta_base * dt.apotema_base)
				dt.calculated_something = True
				return
			
	def solve_specific_cases(self):
		if dt.quantidade_laterais == 4 and are_known(dt.area_base) and dt.aresta_base == None:
			dt.aresta_base = sqrt(dt.area_base)
			dt.calculated_something = True
			
		if dt.quantidade_laterais == 6 and are_known(dt.aresta_base) and dt.apotema_base == None:
			dt.apotema_base = dt.aresta_base * sqrt(3) / 2
			dt.calculated_something = True
		
		
	
	def run(self):
		dt.calculated_something = False
		
		self.solve_aresta_base()
		self.solve_aresta_lateral()
		self.solve_apotema_base()
		self.solve_apotema_lateral()
		self.solve_altura()
		self.solve_area_base()
		self.solve_area_face_lateral()
		self.solve_area_lateral()
		self.solve_area_total()
		self.solve_volume()
		self.solve_quantidade_laterais()
		self.solve_specific_cases()
		
		if dt.calculated_something == True: self.run()

dt = Data_Model()

dt.aresta_base = 4
dt.altura = 3
dt.quantidade_laterais = 6

model = Model(dt)

model.run()

model.show()
		
		
