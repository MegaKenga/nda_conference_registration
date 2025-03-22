from dadata import Dadata
from dotenv import load_dotenv
import os

from conference_registration.models import Person

load_dotenv()


def get_company_by_inn(inn):
    inn = Person.company_inn
    token = os.getenv('TOKEN')
    dadata = Dadata(token)
    result = dadata.find_by_id(name="party", query=str(inn))

    for name in result:
        return(name['value'])


