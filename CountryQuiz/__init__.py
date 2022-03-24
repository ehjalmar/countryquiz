import logging
from typing import List

import azure.functions as func

allCountries = []
visitedCountries = []


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    country = req.params.get('country')

    if not country:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            country = req_body.get('country')

    if country:

        allCountries.clear()
        visitedCountries.clear()

        loadCountries()

        # Add the provided country to visitedCountries
        visitedCountries.append(country)

        while True:

            try:
                print(f"Finding next country after {country}...")

                newCountry = getCountryBasedOnLastCharacter(
                    country, visitedCountries)

                print(f"Found country {newCountry}...")
                visitedCountries.append(newCountry)

                country = newCountry
            except:
                print("No more country options avilable... sorry")
                break

        return func.HttpResponse('{"countries": ' + str(visitedCountries).replace("'",'"') + '}')

    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a country in the query string or in the request body for a proper response.",
            status_code=200
        )


def last_letter(word):
    return word[::-1]


def loadCountries() -> None:
    file = open('input.txt', 'r')
    lines = file.readlines()
    for element in lines:
        allCountries.append(element.strip())

    print(f"All {len(allCountries)} countries where loaded")


def getCountryBasedOnLastCharacter(countryName: str, exclusions: List) -> str:
    lastChar = countryName[-1]

    possibleMatches = sorted([idx for idx in allCountries if idx[0].lower(
    ) == lastChar.lower()], key=last_letter, reverse=True)

    # Remove exclusions from list
    print(f"Possible matched: {str(possibleMatches)}")
    print(f"Exclusions: {str(exclusions)}")

    filteredMatches = [x for x in possibleMatches if x not in exclusions]
    print(f"Filtered matched: {str(filteredMatches)}")

    if len(filteredMatches) != 0:
        return filteredMatches[0]
    else:
        raise ValueError
