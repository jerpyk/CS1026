# Name: Eunsung Kim
# Program Description: the program imports Airport class and Flight class to create Airport and Flight objects and
# use the necessary methods for the objects. The program includes functions to convert the text files into containers
# filled with objects and perform the necessary tasks with these containers.
from Flight import *
from Airport import *

# List of Airport objects
allAirports = []
# Dictionary with origin airport code as key and Flight object as value
allFlights = {}


# Function to read the information from text files for filling the allAirports list and allFlights dictionary
def loadData(airportFile, flightFile):
    # Error handling for file read
    try:
        airportContent = open(airportFile, "r")
        flightContent = open(flightFile, "r")
        try:
            # Airport
            for line in airportContent:
                line = line.split(",")  # convert each line into a list
                for i in range(len(line)):
                    line[i] = line[i].strip()  # remove space for each item in the list
                allAirports.append(Airport(line[0], line[2], line[1]))  # add the Airport object
            # Flight
            flightList = []  # list for Flight objects
            origin = ""
            destination = ""
            for line in flightContent:
                line = line.split(",")  # convert each line into a list
                for i in range(len(line)):
                    line[i] = line[i].strip()  # remove space for each item in the list
                for i in range(len(allAirports)):
                    if line[1] == allAirports[i].getCode():
                        origin = allAirports[i]  # set the original Airport object
                    elif line[2] == allAirports[i].getCode():
                        destination = allAirports[i]  # set the destination Airport object
                # add the Flight object created with the Airport objects
                flightList.append(Flight(line[0], origin, destination))
            # traverse all the Flight objects
            for flight in flightList:
                # add the flight object to the list (for each origin Airport key) inside the allFlights dictionary
                allFlights.setdefault(flight.getOrigin().getCode(), []).append(flight)
            # return true if no error and successful run
            return True
        finally:
            airportContent.close()
            flightContent.close()
    # Catch Exception
    except IOError:
        return False


# Function to return the Airport object with the given airport code
def getAirportByCode(code):
    # traverse all the airports
    for airport in allAirports:
        if airport.getCode() == code:
            return airport
    return -1


# Function to return all the flights with the given city in a list, either in origin or destination
def findAllCityFlights(city):
    cityList = []
    # traverse all the origin Airport code
    for code in allFlights:
        # traverse all the Flight objects for each origin Airport code key
        for i in range(len(allFlights[code])):
            flight = allFlights[code][i]
            originCity = allFlights[code][i].getOrigin().getCity()
            destinationCity = allFlights[code][i].getDestination().getCity()
            if originCity == city or destinationCity == city:
                cityList.append(flight)
    return cityList


# Function to return all the flights with the given country in a list, either in origin or destination
def findAllCountryFlights(country):
    countryList = []
    # traverse all the origin Airport code
    for code in allFlights:
        # traverse all the Flight objects for each origin Airport code key
        for i in range(len(allFlights[code])):
            flight = allFlights[code][i]
            originCountry = allFlights[code][i].getOrigin().getCountry()
            destinationCountry = allFlights[code][i].getDestination().getCountry()
            if originCountry == country or destinationCountry == country:
                countryList.append(flight)
    return countryList


# Function to return the direct flight between two airport if there is one, return the single-hop connecting
# airport if there is one, and if there is neither, return -1
def findFlightBetween(origAirport, destAirport):
    xAirportCandidate = []
    xAirportList = []
    # traverse all the origin Airport code
    for code in allFlights:
        if origAirport.getCode() == code:
            # traverse all the Flight objects for each origin Airport code key
            for i in range(len(allFlights[code])):
                # if there is a direct flight
                if allFlights[code][i].getDestination() == destAirport:
                    return "Direct Flight: " + origAirport.getCode() + " to " + destAirport.getCode()
                else:  # if there is no direct flight
                    # add the destination Airport object to possible connecting airports list
                    xAirportCandidate.append(allFlights[code][i].getDestination())
                    # traverse all the possible connecting airports
    for i in range(len(xAirportCandidate)):
        # traverse all the origin Airport code
        for code in allFlights:
            if xAirportCandidate[i].getCode() == code:
                # traverse all the Flight objects for each origin Airport code key
                for j in range(len(allFlights[code])):
                    # if the destination for the candidate airport is same as the destination airport
                    if allFlights[code][j].getDestination() == destAirport:
                        # add the candidate airport code to the xAirportList
                        xAirportList.append(xAirportCandidate[i].getCode())
    # if the length of the connecting airport list is 0, return -1
    if len(xAirportList) == 0:
        return -1
    # return the set of single-hop connecting airport list
    xAirportList = set(xAirportList)
    return xAirportList


# Function to return the flight that is the return flight of the given flight
def findReturnFlight(firstFlight):
    # traverse all the origin Airport code keys
    for code in allFlights:
        # if the destination of the given flight is the origin of this flight
        if firstFlight.getDestination().getCode() == code:
            # traverse all the Flight objects for each origin Airport code key
            for i in range(len(allFlights[code])):
                # if the origin of the given flight is the destination of this flight
                if firstFlight.getOrigin() == allFlights[code][i].getDestination():
                    return allFlights[code][i]  # return the return flight
    # return -1 if there is no return flight
    return -1
