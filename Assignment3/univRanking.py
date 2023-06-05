# Name: Eunsung Kim
# Program Description: the program uses the getInformation function to get various information from TopUni.csv
# and capitals.csv, and it writes the result to output.txt. The information include universities count, available
# countries, available continents, the universities with top international and national rank, the average score, the
# relative score, the capital city, and the universities that hold the capital name.

# The function that includes all the remaining functions to write the result to output.txt
def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    # Error handling files with try and except
    try:
        # Create univList with information from TopUni.csv
        univList = loadCSVData(rankingFileName)
        # Create capitalsList with information from capitals.csv
        capitalsList = loadCSVData(capitalsFileName)
        # Set the output file to output.txt
        outfile = open("output.txt", "w")
        # Add the capital and continent to the university information
        combinedList = combineList(univList, capitalsList)
        try:
            # Task 1: writing universities count
            outfile.write("Total number of universities => %d" % findUnivCount(univList))
            # Task 2:writing available countries
            outfile.write("\nAvailable countries => ")
            uniqueCountryList = findCountries(univList)
            for country in uniqueCountryList:
                outfile.write(country.upper() + ", ")
            # Task 3: writing available continents
            outfile.write("\nAvailable continents => ")
            uniqueContinentList = findContinent(uniqueCountryList, capitalsList)
            for continent in uniqueContinentList:
                outfile.write(continent.upper() + ", ")
            # Task 4: writing top international university rank and name
            topIntUnivIndex = findTopInternational(selectedCountry, univList)
            topIntUnivRank = univList[topIntUnivIndex][0]
            topIntUnivName = univList[topIntUnivIndex][1]
            outfile.write(
                "\nAt international rank => %s the university name is => %s" % (topIntUnivRank, topIntUnivName.upper()))
            # Task 5: writing top national university rank and name
            topNatUnivIndex = findTopNational(selectedCountry, univList)
            topNatUnivRank = univList[topNatUnivIndex][3]
            topNatUnivName = univList[topNatUnivIndex][1]
            outfile.write(
                "\nAt national rank => %s the university name is => %s" % (topNatUnivRank, topNatUnivName.upper()))
            # Task 6: writing the average score
            averageScore = findAverageScore(selectedCountry, univList)
            outfile.write("\nThe average score => %.1f%%" % averageScore)
            # Task 7: writing the relative score
            continent = findRelativeScore(selectedCountry, combinedList, averageScore)[0]
            highestScore = findRelativeScore(selectedCountry, combinedList, averageScore)[1]
            relativeScore = findRelativeScore(selectedCountry, combinedList, averageScore)[2]
            outfile.write("\nThe relative score to the top university in %s is => (%.2f / %.2f) x 100%% = %.2f%%"
                          % (continent.upper(), averageScore, highestScore, relativeScore))
            # Task 8: writing the capital
            capitalCity = findCapital(selectedCountry, capitalsList)
            outfile.write("\nThe capital is => %s" % capitalCity.upper())
            # Task 9: writing the universities with capital name
            capitalUnivList = findUnivWithCapital(combinedList, capitalCity)
            outfile.write("\nThe universities that contain the capital name =>")
            for i in range(len(capitalUnivList)):
                outfile.write("\n   #" + str(i + 1) + " " + capitalUnivList[i].upper())

        finally:
            # Close the outfile whether exception occurs or not
            outfile.close()
    except IOError:
        # Printed when there is an IOError, when the file does not exist
        print("File Not Found")


# Function for creating list from the two files: TopUni.csv and capitals.csv
def loadCSVData(filename):
    fileList = []
    fileContent = open(filename, "r", encoding='utf8')
    fileContent.readline()  # Skip the headings
    for line in fileContent:
        line = line.strip()
        line = line.split(",")
        if filename == "TopUni.csv":
            del line[4:8]  # Remove the unused information
        elif filename == "capitals.csv":
            del line[2:5]  # Remove the unused information
        fileList.append(line)
    fileContent.close()
    return fileList


# Function for combining two files
def combineList(univList, capitalsList):
    newList = []
    # check for all universities in TopUni.csv
    for i in range(len(univList)):
        # check for all countries in capitals.csv
        for j in range(len(capitalsList)):
            # When the country name in both files are the same
            if univList[i][2].upper() == capitalsList[j][0].upper():
                # append the capital and continent to the univList
                newList.append(univList[i] + capitalsList[j][1:])
    return newList


# 1: finding universities count
def findUnivCount(univList):
    # length of the list is the universities count
    return len(univList)


# 2: finding available countries
def findCountries(univList):
    countryList = [univList[0][2]]  # add the first country
    for i in range(len(univList)):
        # check if the country is in the list and add if not in the list
        if univList[i][2] not in countryList:
            countryList.append(univList[i][2])
    return countryList


# 3: finding available continents
def findContinent(countryList, capitalsList):
    continentList = []
    # check for all countries
    for i in range(len(countryList)):
        # check for all countries in capitalsList
        for j in range(len(capitalsList)):
            # check if the country in each list match, and add the continent if not in the list
            if (countryList[i] == capitalsList[j][0]) and (capitalsList[j][2] not in continentList):
                continentList.append(capitalsList[j][2])
                break  # exit if found a continent for the country
    # check for any continent that was not in the country list but in capitals.csv
    for i in range(len(capitalsList)):
        if capitalsList[i][2] not in continentList:
            continentList.append(capitalsList[i][2])
    return continentList


# 4: finding university with top international rank and name
def findTopInternational(selectedCountry, univList):
    # Set the top international university rank to the lowest rank
    topUnivIndex = len(univList) - 1
    for i in range(len(univList)):
        # check if country name match and the rank is higher than the current top
        if selectedCountry.upper() == univList[i][2].upper() and int(univList[i][0]) < int(univList[topUnivIndex][0]):
            topUnivIndex = i  # set the new top university index if yes
    return topUnivIndex


# 5: finding university with top national rank and name
def findTopNational(selectedCountry, univList):
    # Set the top national university rank to the lowest rank
    topUnivIndex = len(univList) - 1
    for i in range(len(univList)):
        # check if country name match and the rank is higher than the current top
        if selectedCountry.upper() == univList[i][2].upper() and int(univList[i][3]) < int(univList[topUnivIndex][3]):
            topUnivIndex = i  # set the new top university index if yes
    return topUnivIndex


# 6: finding the average score of the selected country
def findAverageScore(selectedCountry, univList):
    scoreSum = 0
    scoreCount = 0
    for i in range(len(univList)):
        # if the country name match, add the total score and score count
        if selectedCountry.upper() == univList[i][2].upper():
            scoreSum += float(univList[i][4])
            scoreCount += 1
    # calculate the average score
    averageScore = scoreSum / scoreCount
    return averageScore


# 7: finding the continent of the country, the highest score, and the relative score
def findRelativeScore(selectedCountry, combinedList, averageScore):
    highestScore = 0
    continent = ""
    for i in range(len(combinedList)):
        # check if country names match and find the continent name
        if selectedCountry.upper() == combinedList[i][2].upper():
            continent = combinedList[i][6]
            break
    for i in range(len(combinedList)):
        # check if the continent names match and find the highest score
        if continent == combinedList[i][6] and float(combinedList[i][4]) > highestScore:
            highestScore = float(combinedList[i][4])
    # calculate the relative score
    relativeScore = (averageScore / highestScore) * 100
    return continent, highestScore, relativeScore  # return these information in a tuple


# 8: finding the capital city of the selected country
def findCapital(selectedCountry, capitalsList):
    capital = ""
    for i in range(len(capitalsList)):
        # check if the country match and find the capital
        if selectedCountry.upper() == capitalsList[i][0].upper():
            capital = capitalsList[i][1]
            break
    return capital


# 9: find the universities that contains the capital city of selected country in its name
def findUnivWithCapital(combinedList, capitalName):
    univWithCapital = []
    for i in range(len(combinedList)):
        # check if a capital name is included in the university name
        if capitalName.upper() in combinedList[i][1].upper():
            # add to the list if yes
            univWithCapital.append(combinedList[i][1])
    return univWithCapital
