class Command:
	quanity_bread = 0
	quanity_wheat_flour = 0

	mony_of_command = 1000

	production_of_wheat_flour = 0

	improvement_indicator_of_production_of_wheat_flour = 1

	def __init__(self, name_of_command, name_of_production):
		self.name_of_command = name_of_command
		self.name_of_production = name_of_production
		print(f'Команда: {self.name_of_command}, имеет: {self.mony_of_command} - денег, производство: {self.name_of_production}')
		match self.name_of_production:#Определение производства команды, присвоение начального значения в зависимости от этого
			case "Мучное":
				self.production_of_wheat_flour = 10
			case _:
				print("hyi")

	def update_production_of_wheat_flour(self):#Улучшение производства конкретного производства на индикатор улучшения, за 600 валюты, и увиличение индикатора на 2
		self.production_of_wheat_flour += self.improvement_indicator_of_production_of_wheat_flour
		self.mony_of_command -= 600
		self.improvement_indicator_of_production_of_wheat_flour += 2

	def receiving_of_wheat_flour(self):#Увеличение количества ресурсов в зависимости от мощности производства
		self.quanity_wheat_flour += self.production_of_wheat_flour

	



first_command=Command("Мука", "Мучное")
# first_command.match_production(first_command.name_of_production)
print(first_command.production_of_wheat_flour)

