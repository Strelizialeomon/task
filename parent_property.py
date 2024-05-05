# Copy and paste your class from the previous function

# Copy and paste the Property class from the previous task

from abc import ABC, abstractmethod
from typing import Tuple, List, Union
from amenity import Amenity
import math


class Property(ABC):
    def __init__(self, prop_id: str,
                 bedrooms: int,
                 bathrooms: int,
                 parking_spaces: int,
                 full_address: str,
                 floor_area: int,
                 price: int,
                 property_features: List[str],
                 coordinates: Tuple[float, float],
                 prop_type: str):  # 能否直接加入到init函数中):
        self.prop_id = prop_id
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking_spaces = parking_spaces
        self.full_address = full_address
        self.suburb = full_address.split(" ")[3]
        self.floor_area = floor_area
        self.price = price
        self.property_features = property_features
        self.coordinates = coordinates
        self.prop_type = prop_type

    def get_prop_id(self) -> str:
        return self.prop_id

    def get_full_address(self) -> str:
        return self.full_address

    def get_suburb(self) -> str:
        return self.suburb

    def get_prop_type(self) -> str:
        return self.prop_type

    def set_bedrooms(self, bedrooms: int) -> None:
        self.bedrooms = bedrooms

    def get_bedrooms(self) -> int:
        return self.bedrooms

    def set_bathrooms(self, bathrooms: int) -> None:
        self.bathrooms = bathrooms

    def get_bathrooms(self) -> int:
        return self.bathrooms

    def set_parking_spaces(self, parking_spaces: int) -> None:
        self.parking_spaces = parking_spaces

    def get_parking_spaces(self) -> int:
        return self.parking_spaces

    def get_coordinates(self) -> Tuple[float, float]:
        return self.coordinates

    ##abstractmethod
    @abstractmethod
    def set_floor_number(self, floor_number: int) -> None:
        pass
        # self.floor_number = floor_number

    ##abstractmethod
    @abstractmethod
    def get_floor_number(self) -> Union[int, None]:
        pass
        # return self.floor_number

    ##abstractmethod
    @abstractmethod
    def set_land_area(self, land_area: int) -> None:
        pass
        # self.land_area = land_area

    ##abstractmethod
    @abstractmethod
    def get_land_area(self) -> Union[int, None]:
        pass
        # return self.land_area

    def set_floor_area(self, floor_area: int) -> None:
        self.floor_area = floor_area

    def get_floor_area(self) -> int:
        return self.floor_area

    def set_price(self, price: int) -> None:
        self.price = price

    def get_price(self) -> int:
        return self.price

    def set_property_features(self, property_features: List[str]) -> None:
        self.property_features = property_features

    def get_property_features(self) -> List[str]:
        return self.property_features

    # 在父类方法中加入add和remove最合适，每一个子类都可以调用到
    # add features, 和task1里的情况类似
    def add_feature(self, feature: str) -> None:
        # property_features = self.property_features(In note: Defined in the classes rather than calling the variables themselves. Doing so will result in a loss of marks.)
        property_features = self.get_property_features()
        if feature in property_features:
            print("This feature has already exist!")
        else:
            property_features.append(feature)
            self.set_property_features(property_features)

    # remove features, 和task1里的情况类似
    def remove_feature(self, feature: str) -> None:
        # property_features = self.property_features
        property_features = self.get_property_features()
        if feature in property_features:
            property_features.remove(feature)
            self.set_property_features(property_features)
        else:
            print("This feature isn't in the list, can not do the remove!")

    def nearest_amenity(self, amenities: List[Amenity], amenity_type: str, amenity_subtype: str = None) -> Tuple[
        Amenity, float]:
        try:
            closest_amenity = None
            min_distance = float("inf")  # 定义无限大
            origin_lat = self.coordinates[0]
            origin_lng = self.coordinates[1]

            if amenity_type is None or amenity_type not in ["train_station", "medical_centre", 'sport_facility',
                                                            "school"]:
                return None

            for amenity in amenities:
                if amenity.get_amenity_type() != amenity_type:
                    continue
                if amenity_subtype is not None and amenity_subtype not in ["Primary", "Secondary"]:
                    continue
                coordinates = amenity.get_amenity_coords()
                distance = self.haversine_distance(origin_lat, origin_lng, coordinates[0], coordinates[1])

                if distance < min_distance:
                    min_distance = distance
                    closest_amenity = amenity

            if closest_amenity is None:
                return (None, 0)

            return (closest_amenity, min_distance)
        except Exception as e:
            print(e)

    def haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        radius_of_earth = 6371  # Radius of the earth in kilometers.
        distance = radius_of_earth * c

        return distance


if __name__ == '__main__':
    pass
