import os
import json
from typing import List, Tuple, Dict
from parent_property import Property
from child_properties import House, Apartment
from amenity import Amenity
from ingestion import ingest_files
from score import *


def read_request(request_filename: str) -> Tuple[dict, dict]:
    """
    This method reads a request file in json format
    and returns two dictionaries; one containing the
    house_importance features and one containing the 
    amenity_importance features.
    """
    # TODO: Step 1 - Define this method to read a JSON request and return 2 dictionaries
    with open(request_filename, mode="r", encoding="utf-8-sig") as file:
        json_info = json.load(file)
        # print(json_info)
    house_importance = json_info["request"]["house_importance"]
    # return house_importance
    amenity_accessibility = json_info["request"]["amenities_accessibility"]
    # return amenity_accessibility
    return house_importance, amenity_accessibility


def find_matching_properties(props: List[Property], house_importance: dict) -> List[Property]:
    """
    THis method recevied a list of all properties and a dictionary that
    contains the house importance criteria from a user's request 
    and returns a list of Property objects that match the user's request
    """
    # TODO: Step 2 - Define this method to return a list of matching properties
    matched = []
    try:
        for property in props:
            suburb = property.get_suburb()
            prop_type = property.get_prop_type()
            bedrooms = property.get_bedrooms()
            bathrooms = property.get_bathrooms()
            parking_spaces = property.get_parking_spaces()
            price = property.get_price()
            property_features = property.get_property_features()
            if suburb != house_importance['suburb'] or prop_type != house_importance['prop_type']:
                continue
            if house_importance['property_features'] not in property_features:
                continue
            if bedrooms < house_importance['bedrooms'] or bathrooms < house_importance['bathrooms'] or parking_spaces < \
                    house_importance['parking_spaces']:
                continue
            if price > house_importance['price']:
                continue
            matched.append(property)
        return matched
    except Exception as e:
        print(e)
        return []


def create_response_dict(scored_properties: dict) -> dict:
    """
    This method takes in a dictionary that has the property objects 
    and their star scores and creates a dictionary in JSON format 
    that can be written into a file
    """
    # TODO: Step 3 - Define this method to create a response dictionary
    sorted_data = sorted(scored_properties.items(), key=lambda item: (-float(item[0]), int(item[1].get_prop_id()[1:])),
                         reverse=False)
    _list = []
    for property in sorted_data:
        _list.append({"star_score": property[0], "property_id": property[1].get_prop_id()})
    result = {
        "properties": _list
    }
    return result


def produce_star_scores(request_filename: str, properties_file: str, amenities_files: List[str]) -> dict:
    # Read the properties and amenities
    medical_file, schools_file, train_stations, sport_facilities = amenities_files
    props, amenities = ingest_files(properties_file, medical_file, schools_file, train_stations, sport_facilities)

    # Read the request and get the dictionaries of house_importance and amenity_accessibility
    house_importance, amenity_accessibility = read_request(request_filename)

    # Collect properties that match the property criteria
    matched_props = find_matching_properties(props, house_importance)

    # Score properties using the amenity amenity_accessibility dictionary
    prop_scores = [score_property(x, amenities, amenity_accessibility) for x in matched_props]

    # Now, we can normalise the scores that we just got
    norm_scores = normalise_scores(prop_scores)

    # Create a collection matching property object to Score
    prop_scored = dict(zip(norm_scores, matched_props))

    # Create a response dictionary
    response_dict = create_response_dict(prop_scored)

    # Return the response dictionary from step 3 and the list of matching property family objects
    return response_dict, matched_props


def respond(response_dict: dict) -> None:
    """
    This function reads a response dictionary and creates a JSON 
    file based on the content of the response dictionary
    """
    # TODO: Step 4 - Create this method to read a response dictionary
    # and create a JSON file
    try:
        with open('/home/response.json', 'w') as f:
            json.dump(response_dict, f, indent=4)
    except:
        raise NotImplementedError


if __name__ == '__main__':
    response_dict, matched_props = produce_star_scores('request.json', 'melbourne_properties.csv',
                                                       ['melbourne_medical.csv', 'melbourne_schools.csv',
                                                        'train_stations.csv', 'sport_facilities.csv'])
    print(f"{len(matched_props)} properties matched with the user's request")
    respond(response_dict)
    # Check if response.json exists in the current directory
    if os.path.exists("/home/response.json"):
        print("File created successfully")
    else:
        print("File not created. Some Error occurred")
