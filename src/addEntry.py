#creates a JSON for adding onto a grocery list database

import json,datetime

def main():
    while True:
        filename = input('Please enter initial (A, N, O, or R): \n').upper()
        if filename not in 'ANOR':
            print('Invalid, please try again.\n')
            continue
        while True:
            confirm = input('Confirm initial (Y/N): %s\n'%filename).upper()
            if confirm in 'NY':
                break
            print('Invalid, please try again.\n')
        if confirm == 'Y': break
    filename = filename + datetime.datetime.now().strftime('%b%d') + ' - groceryList.json'
    print('creating file: %s'%filename)
    jsonfile = open(filename,'a+')
    groceries = {}
    while True:
        print('New item Entry:')
        item, price = input('    Enter item name: '),input('    Enter price for item: ')
        try:
            price = float(price)
        except  ValueError:
            print('Error with price, enter price in digits (no $).')
            continue
        while True:
            confirm = input('Confirm item (Y/N): %s - %s\n'%(item,price)).upper()
            if confirm in 'NY':
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

    jsonfile.close()
if __name__ == '__main__':
    main()