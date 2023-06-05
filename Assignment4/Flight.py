# Name: Eunsung Kim
# Description: this file includes the Flight class, which uses the Airport class to create each Flight object.
# It has the constructor that defines the instance variables needed when creating a Flight object. It has all
# the necessary methods for each Flight object to use, including the get and set methods.
from Airport import *


class Flight:
    # The Constructor
    def __init__(self, flightNo, origin, destination):
        # Check if the parameters origin and destination are Airport objects
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo  # define the flight number
            self._origin = origin  # define the origin airport
            self._destination = destination  # define the destination airport
        else:
            raise TypeError("The origin and destination must be Airport objects")

    # Representation of Flight object
    def __repr__(self):
        if self.isDomesticFlight():
            return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {domestic}"
        else:
            return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {international}"

    # Method to check if two flights are the same flight
    def __eq__(self, other):
        if isinstance(other, Flight):  # check if the parameter other is a Flight object
            return self._origin == other._origin and self._destination == other._destination
        else:
            return False

    # Method to get the flight number
    def getFlightNumber(self):
        return self._flightNo

    # Method to get the origin Airport object of the flight
    def getOrigin(self):
        return self._origin

    # Method to get the destination Airport object of the flight
    def getDestination(self):
        return self._destination

    # Method to check if the flight is domestic or international
    def isDomesticFlight(self):
        # the flight is domestic if the origin and destination country are the same
        return self._origin.getCountry() == self._destination.getCountry()

    # Method to set the origin Airport object of the flight
    def setOrigin(self, origin):
        self._origin = origin

    # Method to set the destination Airport object of the flight
    def setDestination(self, destination):
        self._destination = destination
