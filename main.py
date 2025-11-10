class Planet:
    def __init__(self, name, planet_type, star):

        if any(not isinstance(arg, (str)) for arg in [name, planet_type, star]):
            raise TypeError(f"name, planet type, and star must be strings")

        if any([len(arg) == 0 for arg in [name, planet_type, star]]):
            raise ValueError(f"name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

# Create instances of the Planet class
planet_1 = Planet("Earth","Terrestrial (rock and metal)","Sun")
planet_2 = Planet("Mars", "Terrestrial (rock and metal","Sun")
planet_3 = Planet("Jupiter","Gas Giant (hydrogen and helium)", "Sun")

print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
