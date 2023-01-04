#Goal of this excerise is to create a fuction that creates a new discionary and nest it into a list travel_log


##### SOLUTION #####
#Existing list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#Funtion that appends the list with inputted values.
def add_new_country(country, times_visited, cities):
    new_dict = {
        "country": country,
        "visits": times_visited,
        "cities": cities
    }
    travel_log.append(new_dict)
       
#Calling the function and inputing entries   
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)