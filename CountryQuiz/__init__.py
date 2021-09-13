import logging
from typing import List

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    country = req.params.get('country')
    howmany = req.params.get('howmany')
    numberOfCountries = 12
    if howmany:
        numberOfCountries = int(howmany)

    if not country:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            country = req_body.get('country')

    if country:
        
        result = generateCountryList(country, numberOfCountries)
        return func.HttpResponse(str(result))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a country in the query string or in the request body for a proper response.",
             status_code=200
        )

def generateCountryList(startCountry, numberOfCountries: int) -> List:
    file=open('input.txt', 'r')
    lines = file.readlines()
    cleanList = []
    for element in lines:
        cleanList.append(element.strip())

    currentCountry = startCountry
    lastChar = currentCountry[-1]
    print("Starting country: " + currentCountry)

    visited = [currentCountry]

    i = 0
    while i < numberOfCountries:
            res = [idx for idx in cleanList if idx[0].lower() == lastChar.lower()]
            #print("The list of matching first letter : " + str(res))
            foundNew = False
            foo = 0
            while (foundNew == False):
                if res[foo] not in visited:
                    foundNew = True
                    currentCountry = res[foo]
                foo += 1
            
            visited.append(currentCountry)
            print(currentCountry)
            lastChar = currentCountry[-1]
            i += 1

    return(visited)

