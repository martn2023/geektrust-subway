from train_tracks import combined_station_dictionary

def report_results(full_train_1st, full_train_2nd, all_post_merge_stations): ##untested
    bogies_list_A = report_arrivals(full_train_1st, all_post_merge_stations)
    bogies_list_B = report_arrivals(full_train_2nd, all_post_merge_stations)
    print(f"ARRIVAL TRAIN_A {printable_arrival(bogies_list_A)}")
    print(f"ARRIVAL TRAIN_B {printable_arrival(bogies_list_B)}")

    ##print(f"train tracks combined station dict {combined_station_dictionary}")

    combined_bogies = report_detachment(combined_station_dictionary, bogies_list_A, bogies_list_B)

    print(f"DEPARTURE TRAIN_AB ENGINE ENGINE{combined_bogies}")

    return None

def report_arrivals(full_train, all_post_merge_stations):
    arriving_train = []
    for each_bogie in full_train:
        if each_bogie in all_post_merge_stations:
            arriving_train.append(each_bogie)
    return arriving_train

def printable_arrival(bogies_list):
    string_result = "ENGINE"
    for each_bogie in bogies_list:
        string_result = string_result + " " + each_bogie
    return string_result

def report_detachment(dictionary_of_stations, arriving_a, arriving_b):
    bogies_sorted_by_distance = []

    for bogie_info in arriving_a:
        if bogie_info in dictionary_of_stations:
            bogies_sorted_by_distance.append([dictionary_of_stations.get(bogie_info),bogie_info])
    for bogie_info in arriving_b:
        if bogie_info in dictionary_of_stations:
            bogies_sorted_by_distance.append([dictionary_of_stations.get(bogie_info), bogie_info])

    bogies_sorted_by_distance.sort()

    string_result = ""
    for each in bogies_sorted_by_distance[::-1]:
        string_result = string_result + " " + each[1]

    return string_result



"""

I want to return the merged train AB that leaves HYB, so I need to feed in

    A) lists of lists of distance from HYB bogies
        i. train A and train B's bogies
        ii. dictionary = all stops that have a positive distance value 
            
    B) sort A by distance, then IN reverse traversal, pull index pos 1 in plus string " " in front, returning the combination



2. merged train (which is presumably in order)

    if i knew
    A) the two arriving trains
    B) sorted merge route
        
        in order to find the sorted merged route:
            
            
    

3. I can combine 1 and 2 to return DETACHMENTS


"""