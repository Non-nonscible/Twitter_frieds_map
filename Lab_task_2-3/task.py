'''
Lab task 2
'''
import json
def read_file():
    '''
    Reads json file and compiles it
    into a dict
    '''
    with open(r'C:\Users\Andrea\Programing_basics\Programing_Basics_2022\info.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def find(data, searched):
    '''
    Secondary function that searches
    a dict or list for specific values
    '''
    if isinstance(data, dict):
        if searched in data:
            return data[searched]
        for key in data:
            if isinstance(data[key], dict) or isinstance(data[key], list):
                return find(data[key], searched)
    if isinstance(data, list):
        if searched in data:
            return data
        for item in data:
            if isinstance(item, list) or isinstance(item, dict):
                return find(item, searched)

#print(find(read_file(), 'entities'))

def navigate():
    '''
    Main function for navigation
    in json file
    '''
    data = read_file()
    count = 0
    while True:
        print('Enter the key')
        searched = input()
        if count == 0:
            item = find(data, searched)
        else:
            item = find(item, searched)
        if isinstance(item, str):
            return item
        if isinstance(item, dict):
            print('The value of the key is a dict. \
Do you wish to see the all the keys?(y/n)')
            if input() == 'y':
                for key in item.keys():
                    print(key)
            else:
                print(item)
        if isinstance(item, list):
            if len(item) == 0:
                print('The list is empty')
                break
            print('The value of the key is a list. \
What element do you wish to see?([num])')
            line = input()
            if line.isnumeric():
                print(item[line])
            else:
                print(f'{item}:')
                for itm in item:
                    print(itm)
        count += 1
    return 'Search is complete'

#print(navigate())

#print(_finditem(read_file(), 'location'))