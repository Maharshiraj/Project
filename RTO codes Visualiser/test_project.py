from project import get_num_plate,get_district_name,get_coordinates,get_website
import pytest

def main():

    test_get_district_name()
    
    test_get_website()


def test_get_district_name():
    assert get_district_name("GJ-04")=="Bhavnagar"
    assert get_district_name("MP-43")=="Ratlam"
    assert get_district_name("RJ-20")=="Kota"


def test_get_website():
    assert get_website("MH")=="transport.maharashtra.gov.in"
    assert get_website("MP")=="www.transport.mp.gov.in"
    assert get_website("RJ")=="www.transport.rajasthan.gov.in"
    

if __name__=="__main__":
    main()