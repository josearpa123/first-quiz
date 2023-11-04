################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

# Función para obtener la temperatura de una ciudad
def get_city_temperature(city):
   if city == "Quito":
      return 22
   if city == "Sao Paulo":
      return 17
   if city == "San Francisco":
      return 16
   if city == "New York":
       return 14

# Función para obtener el clima de una ciudad
def get_city_weather(city):
    sky_condition = None

    if city == "Sao Paulo":
        sky_condition = "cloudy"
    if city == "New York":
       sky_condition = "rainy"

    temperature = get_city_temperature(city)

    if sky_condition is not None:
        return str(temperature)  + " degrees and " + sky_condition
    else:
        return str(temperature) + " degrees and sunny"

# Pruebas para verificar la función get_city_weather
# Pruebas para verificar la función get_city_weather
def test_get_city_weather():
    assert get_city_weather("Quito") == "22 degrees and sunny"
    assert get_city_weather("New York") == "14 degrees and rainy"  # Cambia "Nueva York" por "New York"


# Casos de prueba adicionales
assert get_city_weather("Sao Paulo") == "17 degrees and cloudy"
assert get_city_weather("San Francisco") == "16 degrees and sunny"  


