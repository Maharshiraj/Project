import json

def main():

    selected_geojson()


def selected_geojson(name_selected):

    with open('IndianDistrict.geojson') as json_file:
        district = json.load(json_file)

        selected_list = district['features']

        for i in range(len(selected_list)):
            if (selected_list[i]['properties']['NAME_2']==name_selected or selected_list[i]['properties']['VARNAME_2']==name_selected):
                outpID= selected_list[i]['properties']['ID_2']
                
        return selected_list[outpID-1]
        #print(selected_list[outp-1]['properties'],selected_list[outp-1]['geometry'])


if __name__ == "__main__":
    main()    