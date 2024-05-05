# Copy and paste your code from the previous task

# Copy and Paste the House and Apartment classes from the previous task

from typing import Tuple, List, Union
from parent_property import Property

class House(Property):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        land_area: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        super().__init__(prop_id, bedrooms, bathrooms, parking_spaces, full_address, floor_area, price, property_features, coordinates, "house")
        self.land_area = land_area

    def set_floor_number(self, floor_number: int) -> None:
        self.floor_number = floor_number

    def get_floor_number(self) -> Union[int, None]:
        return self.floor_number

    def get_land_area(self) -> Union[int, None]:
        return None

    def set_land_area(self, land_area: int) -> None:
        return None
    # To be implemented
#     def set_land_area(self, land_area: int) -> None:
#         if prop_type == "house":
#             self.land_area = land_area
#         else:
#             return None
#     def get_land_area(self) -> Union[int,None]:
#         if prop_type == "house":
#             return self.land_area
#         else:
#             return None


class Apartment(Property):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_number: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        super().__init__(prop_id, bedrooms, bathrooms, parking_spaces, full_address, floor_area, price, property_features, coordinates, "apartment")
        self.floor_number = floor_number

    def set_land_area(self, land_area: int) -> None:
        self.land_area = land_area

    def get_land_area(self) -> Union[int, None]:
        return self.land_area

    def get_floor_number(self) -> Union[int, None]:
        return None

    def set_floor_number(self, floor_number: int) -> None:
        return None
    # To be implemented
#     def set_floor_number(self, floor_number: int) -> None:
#         if prop_type == "apartment":
#             self.floor_number = floor_number
#         else:
#             return None
#     def get_floor_number(self) -> Union[int,None]:
#         if prop_type == "apartment":
#             return self.floor_number
#         else:
#             return None

if __name__ == '__main__':
    pass

