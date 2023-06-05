# Name: Eunsung Kim
# Description: this file includes the Airport class, which has the constructor that defines the instance
# variables for each Airport object created, and it includes all the necessary methods to get and set the variables
# of the Airport objects.
class Airport:
    # The Constructor
    def __init__(self, code, city, country):
        self._code = code  # define the code
        self._city = city  # define the city
        self._country = country  # define the country

    # Representation of Airport object
    def __repr__(self):
        return self._code + "(" + self._city + "," + self._country + ")"

    # Method to get the airport code
    def getCode(self):
        return self._code

    # Method to get the city in which the airport is located
    def getCity(self):
        return self._city

    # Method to get the country in which the airport is located
    def getCountry(self):
        return self._country

    # Method to set the city in which the airport is located
    def setCity(self, city):
        self._city = city

    # Method to set the country in which the airport is located
    def setCountry(self, country):
        self._country = country
