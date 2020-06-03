from .models import *
import datetime
from faker import Faker
fake = Faker()
from .serializer import JsonDataSerializer


def format_json(dict_data):
    dict_data["id"] = dict_data.get("random_id")
    dict_data.pop("random_id")
    return dict_data

def get_period_list():
    data = []
    for i in range(3):
        dict_data = {}
        demo_start = fake.date_time()
        end_time = demo_start + datetime.timedelta(hours = 4,minutes = 16)
        dict_data["start_time"] = demo_start.strftime("%b %d %Y %I:%M %p")
        dict_data["end_time"] = end_time.strftime("%b %d %Y %I:%M %p")
        data.append(dict_data)
    return data

def populate_data():
    data_list=[]
    for i in range(3):
        dict_data = {}
        dict_data["random_id"] = fake.password(special_chars=False,upper_case=True,lower_case=False,length=9)
        dict_data["real_name"] = fake.name()
        dict_data["tz"] = fake.timezone()
        dict_data["activity_periods"] = get_period_list()
        data_list.append(dict_data)

    for i in data_list:
        serializer = JsonDataSerializer(data=i)
        if serializer.is_valid():
            serializer.save()
        else:
            raise serializer.errors