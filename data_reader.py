def pull_raw_data(file_path):
    reading_file = open(file_path, 'r')
    listed_lines = reading_file.readlines()
    listed_lines[0] = listed_lines[0][:-1] ##hardcoding based on fact pattern - assuming only 2 trains, the line that isnt the most recent has a linebreak that needs to be removed

    train_records = []
    for each_line in listed_lines:
        train_records.append(bogies_by_destination(each_line))
    return train_records

def bogies_by_destination(each_line):
    tokenized_line = each_line.split(" ")
    return tokenized_line[2:]
