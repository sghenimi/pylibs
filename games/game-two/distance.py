from geopy.distance import geodesic

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(
    f"There is {geodesic(newport_ri, cleveland_oh)}  between the two locations")
