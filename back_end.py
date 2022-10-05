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
		if self.dt.aresta_base == None:
			if are_known(self.dt.area_base, self.dt.apotema_base, self.dt.quantidade_laterais):
				self.dt.aresta_base = (2 * self.dt.area_base) / (self.dt.apotema_base * self.dt.quantidade_laterais)
				self.dt.calculated_something = True
				return

	def solve_aresta_lateral(self):
		if self.dt.aresta_lateral == None:
			if are_known(self.dt.apotema_lateral, self.dt.apotema_base):
				self.dt.aresta_lateral = sqrt(self.dt.apotema_lateral ** 2 + (self.dt.apotema_base / 2) ** 2)
				self.dt.calculated_something = True
				return

	def solve_apotema_base(self):
		if self.dt.apotema_base == None:
			if are_known(self.dt.area_base, self.dt.aresta_base, self.dt.quantidade_laterais):
				self.dt.apotema_base = (2*self.dt.area_base) / (self.dt.aresta_base * self.dt.quantidade_laterais)
				self.dt.calculated_something = True
				return
		
	def solve_apotema_lateral(self):
		if self.dt.apotema_lateral == None:
			if are_known(self.dt.apotema_base, self.dt.altura):
				self.dt.apotema_lateral = sqrt(self.dt.apotema_base ** 2 + self.dt.altura ** 2)
				self.dt.calculated_something = True
				return
			
	def solve_altura(self):
		if self.dt.altura == None:
			if are_known(self.dt.apotema_lateral, self.dt.apotema_base):
				self.dt.altura = sqrt(self.dt.apotema_lateral ** 2 - self.dt.apotema_base ** 2)
				self.dt.calculated_something = True
				return
		
	def solve_area_base(self):
		if self.dt.area_base == None:
			if are_known(self.dt.aresta_base, self.dt.apotema_base, self.dt.quantidade_laterais):
				self.dt.area_base = self.dt.aresta_base * self.dt.apotema_base / 2 * self.dt.quantidade_laterais
				self.dt.calculated_something = True
				return

			if are_known(self.dt.aresta_base):
				self.dt.area_base = self.dt.aresta_base ** 2
				self.dt.calculated_something = True
				return
			
	def solve_area_face_lateral(self):
		if self.dt.area_face_lateral == None:
			if are_known(self.dt.apotema_lateral, self.dt.apotema_base):
				self.dt.area_face_lateral = self.dt.apotema_lateral * self.dt.apotema_base / 2
				self.dt.calculated_something = True
				return
			
	def solve_area_lateral(self):
		if self.dt.area_lateral == None:
			if are_known(self.dt.aresta_base, self.dt.apotema_lateral, self.dt.quantidade_laterais):
				self.dt.area_lateral = self.dt.aresta_base * self.dt.apotema_lateral / 2 * self.dt.quantidade_laterais
				self.dt.calculated_something = True
				return
		
	def solve_area_total(self):
		if self.dt.area_total == None:
			if are_known(self.dt.area_lateral, self.dt.area_base):
				self.dt.area_total = self.dt.area_lateral + self.dt.area_base
				self.dt.calculated_something = True
				return
		
	def solve_volume(self):
		if self.dt.volume == None:
			if are_known(self.dt.area_base, self.dt.altura):
				self.dt.volume = self.dt.area_base * self.dt.altura / 3
				self.dt.calculated_something = True
				return
			
	def solve_quantidade_laterais(self):
		if self.dt.quantidade_laterais == None:
			if are_known(self.dt.area_base, self.dt.aresta_base, self.dt.apotema_base):
				self.dt.quantidade_laterais = (2*self.dt.area_base) / (self.dt.aresta_base * self.dt.apotema_base)
				self.dt.calculated_something = True
				return
			
	def solve_specific_cases(self):
		if self.dt.quantidade_laterais == 4 and are_known(self.dt.area_base) and self.dt.aresta_base == None:
			self.dt.aresta_base = sqrt(self.dt.area_base)
			self.dt.calculated_something = True
			
		if self.dt.quantidade_laterais == 6 and are_known(self.dt.aresta_base) and self.dt.apotema_base == None:
			self.dt.apotema_base = self.dt.aresta_base * sqrt(3) / 2
			self.dt.calculated_something = True
		
		
	
	def run(self):
		self.dt.calculated_something = False
		
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
		
		if self.dt.calculated_something == True: self.run()

		
