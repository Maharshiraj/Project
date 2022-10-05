from cgitb import text
import re, csv,random,sys
from termcolor import colored
import webbrowser
import folium
from geopy.geocoders import Nominatim
from folium import GeoJson,plugins
import current
from pyfiglet import Figlet
import pyttsx3
import requests

def main():
    
    figlet = Figlet()

    print(""" 
    ⚠️⚠️⚠️  DISCLAIMER  ⚠️⚠️⚠️
    
    This project's geojson file is not completely coherent, it's work in progess. So might not be accurate.
    
    Special Note : Jammu and Kashmir (J&K) map is not according to what the Republic of India mentions.

    So any discrepancies in defining the borders of states is subjected to the geojson file encoding which I could get from the interntet.

    """)
    
    print(colored(f'It displays the associated district map of any RTO registered vehicle number plate from INDIA','yellow'))
    
    print(colored(f'Made by : MAHARSHIRAJSINH CHUDASAMA\n','yellow'))

    print("============================================================================================================================================================================================")
    
    reg_series = get_num_plate()
    
    print("============================================================================================================================================================================================")
    
    state_code=reg_series[:2]
    reg_series = reg_series[:2] + "-" + reg_series[2:]
    
    print("============================================================================================================================================================================================")
    
    district_name = get_district_name(reg_series)
    figlet.setFont(font="roman")
    print(colored(figlet.renderText(f'{district_name}'),'blue'))

    print("============================================================================================================================================================================================")
    
    print("============================================================================================================================================================================================")
    
    website = get_website(state_code)
    website="https://"+website
    figlet.setFont(font="digital")
    print(f"State transport website is mentioned below.✅\n")
    text_speech("State transport website is mentioned below,ctrl click to open it")
    print(colored(link(website),'yellow'))
    #webbrowser.open_new_tab(f"{website}")
    #broswers understands it as robots and prevents opening it
    
    print("============================================================================================================================================================================================")

    print("============================================================================================================================================================================================")
    
    location=get_coordinates(district_name)
    project_coordinates(district_name,location,reg_series)
    
    print("============================================================================================================================================================================================")
    

def get_num_plate()->str:
    """
    Gets the license number plate.

    :return: Input entered by the user.
    :rtype: str
    
    """
    num_plate = input("Enter number plate (without spaces):\n")

    if status := re.fullmatch(r"([A-Z]{2}\d{1,2})[A-Z]{,3}\d{4}", num_plate.upper(), re.IGNORECASE):
        
        return status.group(1)

    else:
        print(colored("Invalid ❌\nNumber plate like doesn't this exists",'red'))
        text_speech("Invalid")
        exit(1)


def get_district_name(reg_series)->str:
    """
    Fetches the name of the district from the registration series provided.

    :param reg_series: State name abbreviation and code part of the registration series.
    :type reg_series: str
    :return: District name of the respective registration code.
    :rtype: str
    
    """

    try:
        with open("RTOcodes.csv") as source_file:
            reader = csv.DictReader(source_file)
            for row in reader:

                if row["Registration Series"] == reg_series:

                    print(colored("Valid ✅\nNumber plate like this exists\n",'green'))
                    text_speech("Valid")
                    
                    print(
                        f"{row['Registration Series']} \nis\n "
                    )
                    
                    return row["Registration Zone / City"].split(" ")[0]
                    
                
            print(f"No registration series starts with {reg_series[:2]}")
            text_speech(f"No registration series starts with {reg_series[:2]}")
            print(colored("Invalid ❌\nNumber plate like doesn't this exists",'red'))
            text_speech("Invalid")
            exit(1)

    except:
        print(f"Registration city/district details not found in RTO csv file for {reg_series} ❌")
        text_speech(f"Registration city/district details not found in RTO csv file for {reg_series}❌")
        exit(1)


def get_coordinates(name):
    """
    Fetches the location co-ordinates of the given district.

    :param name: The district name for which to get coordinates
    :type name: str
    :return: A geopy.location.Location class containing all the related information of that district.
    :rtype: class
    
    """

    try:
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(name,country_codes="IN")
        
        print(location)
        print("\nLocation co-ordinates are")
        print(f"\tlat={location.latitude} ✅")
        print(f"\tlon={location.longitude} ✅")
        return location
    except:
        print("Couldn't able to find co-ordinates ❌")
        text_speech("Couldn't able to find co-ordinates ❌")
        exit(1)


def project_coordinates(name,location,num):
    """
    Displays a folium map of that particular district of India. 
    """

    my_map = folium.Map(location=[location.latitude, location.longitude], zoom_start=5)

    styling1 = {"color": "grey", "weight": "0.5"}
    styling2 = {"color": "grey", "weight": "1.0","Opacity":0.5,"fillColor":"lightgreen","fillOpacity":"0.3"}
    styling3 = {"color": "grey", "weight": "2.0","Opacity":0.7,"fillColor":"skyblue","fillOpacity":"0.5"}
    
    minimap = plugins.MiniMap()
    my_map.add_child(minimap)

    GeoJson(requests.get("https://raw.githubusercontent.com/Subhash9325/GeoJson-Data-of-Indian-States/master/Indian_States").text, name="States", style_function=lambda x: styling1).add_to(my_map)

    
    
    districtfile = open("IndianDistrict.geojson", encoding="utf8")
    text2 = districtfile.read()
    GeoJson(text2, name="District", style_function=lambda x: styling2).add_to(my_map)
    
    
    try:
        text3=current.selected_geojson(name)
        GeoJson(text3, name="Selected", style_function=lambda x: styling3).add_to(my_map)

        folium.Marker( [location.latitude, location.longitude], popup=f"<b>{num}</b>" ,tooltip="Click to reveal district code!" ,icon=folium.Icon(color="green", icon="info-sign") ).add_to(my_map)
        folium.LayerControl().add_to(my_map)

        my_map.save("my_map.html")
        webbrowser.open_new_tab("my_map.html")

    except:
        print("Map not available currently for this district ❌")
        text_speech("Map not available currently for this district ❌")
        exit(1)


def get_website(statecode)->str:
    """
    Provides the respective state government transport organisation website.

    :param statecode: First two letters represnting the statecode.
    :type statecode: str
    :return: Respective state government transport authority website.
    :rtype: str

    """
    try:
        with open("website.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == statecode:
                    return row[1]
    except:
        print("Website not available presently ❌")
        text_speech("Website not available presently ❌")
        exit(1)


def link(uri, label=None):
    """
    Converts the text into a clickable hyperlink.

    :param uri: The text to convert into hyperlink.
    :type uri: str
    :return: A hyperlink of the respective website.
    :rtype: str

    """
    if label is None: 
        label = uri
    parameters = ''
    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'
    return escape_mask.format(parameters, uri, label)


def text_speech(name):
    """
    Converts text to speech.

    :param name: The text to be read aloud.
    :type name: str

    """
    engine = pyttsx3.init()
    engine.say(f"{name}")
    engine.runAndWait()


if __name__ == "__main__":
    main()