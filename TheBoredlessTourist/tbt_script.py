

# List of destinations

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

traveler_destination_index = 0

attractions = []

attractions_for_destination = [] 

for x in destinations:
    attractions.append([])

def get_destination_index(destination):
    destination_index = 0
    for x in destinations:
        if x == destination:
            destination_index = destinations.index(x)
            break
        else:
            pass
    return destination_index


def get_traveler_location(traveler):

    traveler_destination = test_traveler[1]

    get_index = get_destination_index(traveler_destination)

    global traveler_destination_index 

    traveler_destination_index = get_index



def get_traveler_index():
    
    global traveler_destination_index

    return traveler_destination_index


def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions[destination_index].append(attraction)

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]

    attractions_with_interest = []

    for a in attractions_in_city:
        possible_attractions = a[0]
        for b in a[1]:
            attraction_tags = b
            for z in interests:
                if z == attraction_tags:
                    attractions_with_interest.append(possible_attractions)
                else:
                    pass
    
    
    return attractions_with_interest


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: {traveler_attractions[0]}"

    return interests_string


get_traveler_location(test_traveler)

test2 = get_traveler_index()

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)