#creates a JSON for adding onto a grocery list database

import json,datetime

def main():
    while True:
        filename = input('Please enter first initial: \n').upper()
        while True:
            confirm = input('Confirm initial (Y/N): %s\n'%filename).upper()
            if confirm in 'NY':
                break
            print('Invalid, please try again.\n')
        if confirm == 'Y': break
        print('Try again.')
    filename = filename + datetime.datetime.now().strftime('%b%d') + '.json'
    print('creating file: %s'%filename)
    jsonfile = open(filename,'a+')
    groceries = {}
    while True:
        print('New item Entry:')
        item, price = input('    Enter item name: '),input('    Enter price for item: ')
        try:
            price = float(price)
        except ValueError:
            print('Error with price, enter price in digits (no $).')
            continue
        while True:
            confirm = input('Confirm item (Y/N): %s - %s\n'%(item,price)).upper()
            if confirm and confirm in 'NY':
                break
            print('Invalid, please try again.\n')
        if confirm == 'Y':
            groceries[item] = price
        else:
            break
        print('Current list: ')
        for key in groceries: print('   %s\t\t\t%s'%(key,groceries[key]))
        print('Total sum:\t\t%s'%sum([groceries[key] for key in groceries]))
        while True:
            confirm = input('If finished, enter "done" or press enter to continue.\n').lower()
            if confirm == 'done' or not(confirm):
                break
            print('Invalid, please try again.\n')
        if confirm == 'done': break

    to_dump = {
        'list':groceries,
        'sum':sum([groceries[key] for key in groceries]),
        'for': 'all' #may add functionality for items shared with specific people
    }
    print('Writing to json file...')
    try:
        json.dump(to_dump,jsonfile)
        jsonfile.close()
        print('Successfully dumped to json file.')
    except:
        print('Unable to write to json, please try again.')
    print('Peace out.')
if __name__ == '__main__':
    main()