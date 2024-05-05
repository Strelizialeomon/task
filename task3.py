import csv
import json

def process_schools(file_name: str) -> dict:
    # with open("melbourne_schools.csv", mode="r") as file:
    with open(file_name) as file:
        # 创建一个CSV阅读器对象
        school = csv.reader(file)
        melbourne_schools = {}
        # 遍历CSV文件
        for index,schools_separate_list in enumerate(school):
            if index ==0:
                continue
            if schools_separate_list[0] == "school_no":
                continue
            school_no = schools_separate_list[0]
            school_name = schools_separate_list[1]
            school_type = schools_separate_list[2]
            school_lat = schools_separate_list[18]
            school_lat = float(school_lat)
            school_lon = schools_separate_list[17]
            school_lon = float(school_lon)

            schools_dict = {
                "school_no" : school_no,
                "school_name" : school_name,
                "school_type" : school_type,
                "school_lat" : school_lat,
                "school_lon" : school_lon
            }
            melbourne_schools[school_no] = schools_dict
    return melbourne_schools

def process_medicals(file_name: str) -> dict:
    with open(file_name) as file:
        # 创建一个CSV阅读器对象
        medical = csv.reader(file)
        melbourne_medical = {}
        # 遍历CSV文件
        for index,medical_separate_list in enumerate(medical):
            if index == 0:
                continue
            if medical_separate_list[0] == "gp_code":
                continue
            gp_code = medical_separate_list[0]
            gp_name = medical_separate_list[1]
            # Address = medical_separate_list[2]
            # Phone = medical_separate_list[3]
            location = medical_separate_list[-1]
            print(location)
            if location == " " or location == "NA":
                continue
            try:
                loc = json.loads(location)
                print(loc)
                lat = loc['lat']
                lng = loc['lng']
                print(lat, lng)

                medical_dict = {
                    "gp_code": gp_code,
                    "gp_name": gp_name,
                    # "Address" : Address,
                    # "Phone" : Phone,
                    # "gp_lat" : gp_lat,
                    # "gp_lon" : gp_lon,
                    "gp_lat": lat,
                    "gp_lon": lng
                }
                melbourne_medical[gp_code] = medical_dict
            except Exception as e:
                print('here----: ',e)
    return melbourne_medical


def process_sport(file_name: str) -> dict:
    # with open("sport_facilities.csv", mode="r") as file:
    with open(file_name) as file:
        # 创建一个CSV阅读器对象
        sport = csv.reader(file)
        sport_facilities = {}
        # 遍历CSV文件
        for index,facilities_separate_list in enumerate(sport):
            if index == 0:
                continue
            if facilities_separate_list[0] == "facility_id":
                continue
            facility_id = facilities_separate_list[0]
            facility_name = facilities_separate_list[2]
            if facilities_separate_list[3] != '':
                sport_lat = float(facilities_separate_list[3])
            if facilities_separate_list[4] != '' :
                sport_lon = float(facilities_separate_list[4])
            sport_played = facilities_separate_list[5]

            facilities_dict = {
                "facility_id" : facility_id,
                "facility_name" : facility_name,
                "sport_lat" : sport_lat,
                "sport_lon" : sport_lon,
                "sport_played" : sport_played
            }
            sport_facilities[facility_id] = facilities_dict
    return sport_facilities


def main():
    school_dict = process_schools('sample_melbourne_schools.csv')
    medical_dict = process_medicals('sample_melbourne_medical.csv')
    sport_dict = process_sport('sample_sport_facilities.csv')

    sample_medical_code = 'mgp0041'
    print(f"There are {len(school_dict)} schools and {len(sport_dict)} sport facilities in our dataset")
    print(f"The location for {medical_dict[sample_medical_code]['gp_name']} is {medical_dict[sample_medical_code]['gp_lat']}, {medical_dict[sample_medical_code]['gp_lon']}")

if __name__ == '__main__':
    main()

