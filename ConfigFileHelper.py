import json
import sys


def open_or_create_file(filename):
    # Open the file with writing permission
    try:
        config_file = open(filename, 'r+')
    except FileNotFoundError:
        config_file = open(filename, 'x')
    except Exception:
        sys.exit('Can not create or open the file' + str(filename))
    return config_file


def get_file_content(filename):
    file = open_or_create_file(filename)
    keys = read_mapped_keys(file)
    file.close()
    return keys


def get_keyboard_event_key_ids():
    return 0


def get_midi_event_key_id():
    return 1


def read_mapped_keys(file):
    mappingList = list()
    filelines = file.readlines()
    for line in filelines:
        # cols are mappend in "key"~"value"~"Shortcut"
        row = list(line.replace('\n', '').split('~'))
        element = {}
        if len(row) == 2:
            element = {'midi_key': row[0],
                       'keys': {
                           'on': row[1],
                           'off': ''
                       },
                       'wait': 0}
        elif len(row) == 4:
            element = {'midi_key': row[0],
                       'keys': {
                           'on': row[1],
                           'off': row[2]
                       },
                       'wait': row[3]}
        mappingList.append(element)
    return mappingList


def write_map_key(file):
    old_lines = read_mapped_keys(file)
    return old_lines
