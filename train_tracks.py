route_a = [["CHN",0],["SLM",350],["BLR",550],["KRN",900],["HYB",1200],["NGP",1600],["ITJ",1900],["BPL",2000],["AGA",2500],["NDL",2700]]
route_b = [["TVC",0],["SRR",300],["MAQ",600],["MAO",1000],["PNE",1400],["HYB",2000],["NGP",2400],["ITJ",2700],["BPL",2800],["PTA",3800],["NJP",4200],["GHY",4700]]

def find_merge_station(route_a, route_b):
    stations_a_set = set()
    for station_data in route_a:
        stations_a_set.add(station_data[0])
    for station_data in route_b:
        if station_data[0] in stations_a_set:
            ##print(f"merge station discovered {station_data[0]}")
            return station_data[0] ## this is the first common station in both routes

merge_station = find_merge_station(route_a,route_b)

def adjust_distances(route, merge_station):
    for station_data in route:
        if station_data[0] == merge_station:
            distance_adjustment = station_data[1]
            break
    for station_data in route:
        station_data[1] -= distance_adjustment
    ##print(f"route corrected for distance {route} at merge station {merge_station}")
    return route

adjust_distances(route_a, merge_station) ## you could technically replace "merge station" with the return from from the find_merge_station function
adjust_distances(route_b, merge_station) ## you could technically replace "merge station" with the return from from the find_merge_station function

def find_post_merge_stations(numerically_adjusted_route):
    post_merge_stations = []
    for station_data in numerically_adjusted_route:
        if station_data[1] >= 0:
            post_merge_stations.append(station_data[0])
    ##print(f"post merge stations now {post_merge_stations}")
    return post_merge_stations

post_merge_A = find_post_merge_stations(adjust_distances(route_a, merge_station))
post_merge_B = find_post_merge_stations(adjust_distances(route_b, merge_station))

def all_post_merge_stations(post_merge_A, post_merge_B):
    result = set(post_merge_A).union(set(post_merge_B)) ## create unionized set of stations to save runtime
    ##print(f"all post merge stations {result}")
    return result

def create_dictionary_of_combined_stations(numerically_adjusted_a, numerically_adjusted_b):
    temp_dictionary = {}

    for each_station_data in numerically_adjusted_a:
        if each_station_data[1] > 0:
            temp_dictionary[each_station_data[0]] = each_station_data[1]

    for each_station_data in numerically_adjusted_b:
        if each_station_data[1] > 0:
            temp_dictionary[each_station_data[0]] = each_station_data[1]

    ##print(f"temp dict {temp_dictionary}")
    return temp_dictionary

combined_station_dictionary = create_dictionary_of_combined_stations(adjust_distances(route_a, merge_station),adjust_distances(route_b, merge_station))


"""
we need to find 

1. merge station (first one of the common route)
2. common route
3. split station (last one of the common route)
"""
