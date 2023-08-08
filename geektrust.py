from sys import argv
import data_reader
import train_tracks
import reporting

def validated_file_path():
    if len(argv) != 2:
        raise Exception("ERROR: Expecting A) geektrust file and B) input file")
    return argv[1]


def main():
    returned_data = data_reader.pull_raw_data(validated_file_path())
    ##print(f"RETURNED_DATA {returned_data}")

    reporting.report_results(returned_data[0],returned_data[1],train_tracks.all_post_merge_stations(train_tracks.post_merge_A, train_tracks.post_merge_B))

    
if __name__ == "__main__":
    main()


"""
We need to output 

1. What the trains look like at the detach:
    A) common stations
    B) what the two trains look like entering the MERGE station (HYB)
        i. common stations
        ii. merge station
        iii. detach station
        iv. original listing
    C) 



"""