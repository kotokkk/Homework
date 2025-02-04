"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""


from pyowm import OWM
from pprint import pprint

owm = OWM("b621bcef70b29e32df3a77ae312a0fc5")
mgr = owm.weather_manager()

city = input("Enter city: ")

obs = mgr.weather_at_place(city)

dict_1 = obs.to_dict()

pprint(dict_1)
