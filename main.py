class Country(object):
    def __init__(self, name, population, area):
        self.population = population
        self.area = area
        self.name = name

    def is_big(self):
        if self.population > 20000000 or self.area > 3000000:
            return True

    def compare(self, another):
        if self.population / self.area > another:
            return f'{country} has a {smaller / larger} population density than {other_country}'

    another = andorra


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)


print(Country.is_big(self=australia))
print(Country.compare(self=australia))
