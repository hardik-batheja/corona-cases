import pycountry
import random
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inspecthoa.settings')
django.setup()
from basic.models import Country

def populate(n=20):
    countr=list(pycountry.countries)
    for i in range(0,n):
        ccode=countr[i].numeric
        cname=countr[i].name
        tc=random.randint(2,10000)
        rc = random.randint(0,tc)
        dc= random.randint(0,tc-rc)
        coun=Country.objects.get_or_create(country=cname,countrycode=ccode,tcases=tc,rcases=rc,dcases=dc)


if __name__ == "__main__":
    print("Populating")
    populate(30)
    print("Populated")
