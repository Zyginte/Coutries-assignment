class Country(object):
    def __init__(self, name, population, area):
        self.population = population
        self.area = area
        self.name = name
        self.population_density = self.population / self.area

    def is_big(self):
        if self.population > 20000000 or self.area > 3000000:
            return True
        else:
            return False

    def compare(self, another):
        if self.population_density > another.population_density:
            return f'{self.name} has a larger population density'
        elif self.population_density < another.population_density:
            return f'{self.name} has a smaller population density'
        else:
            return f'Population density is the same'


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(andorra.is_big())
print(australia.is_big())
print(australia.compare(andorra))
print(andorra.compare(australia))
