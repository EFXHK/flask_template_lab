from models.event import *
import datetime

event1 = Event(datetime.date(2022, 10, 8), "Birthday party", 16, "Hyde Park", "Murder mystery")
event2 = Event(datetime.date(2022, 11, 8),"Work meeting", 8, "the barn", "sales targets")
event3 = Event(datetime.date(2022, 12, 22),"NASA launch", 800, "Washington Park", "Artemis 1 launch")


events = [event1, event2, event3]

def save_event(new_event):
    events.append(new_event)


# date, name_of_event, number_of_guests, room_location, description):
