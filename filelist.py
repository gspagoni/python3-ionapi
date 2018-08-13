# Author: Giampaolo Spagoni
# Title: Senior Solution Architec
# Team: Infor OS service
# Company: Infor
# Version : 1.0.0
# Date : 25th june 2018
#
# Module for readin IONAPI files

import os , glob
import json

# print the welcome message
def welcome_mes():
    print('*************************************************************************')
    print('*                                                                       *')
    print('*          PPPPPP                                       33333           *')
    print('*          P     P Y   Y TTTTT H    H  OOOO  N    N    3     3          *') 
    print('*          P     P  Y Y    T   H    H O    O NN   N          3          *') 
    print('*          PPPPPP    Y     T   HHHHHH O    O N N  N     33333           *')
    print('*          P         Y     T   H    H O    O N  N N          3          *')
    print('*          P         Y     T   H    H O    O N   NN    3     3          *')
    print('*          P         Y     T   H    H  OOOO  N    N     33333           *')
    print('*                                                                       *')
    print('*                                                                       *')
    print('*         Example: Get token from IONAPI                                *')
    print('*         Call API of current logged user                               *')
    print('*         endpoint: /Mingle/SocialService.Svc/User/Detail               *')
    print('*                                                                       *')
    print('*                                          by Giampaolo Spagoni         *')
    print('*                                                                       *')
    print('*************************************************************************')

# Read an IONAPI file and return a dictionary (key,value) where the key is ti,cn,ci,cs.... all elements of the ionapi file
def get_config():    

    valid_path = False
    fileList = []

    while not valid_path:
        try:
            dirlist = input('type path for ionapi files (0 = exit): ')
            if (dirlist) == '0':
                exit()
            os.chdir(dirlist)
            for file in glob.glob('*.ionapi'):
                fileList.append(file)
            if (len(fileList)==0):
                print('No files with extentions ionapi. Type a different path...')
            else:    
                valid_path = True
        except FileNotFoundError:
            print('Path doesn\' t exist. Type a valid path...')
        except PermissionError as err:
            print(err)    

    print(' ')


#print(fileList)  
    idx = 1  
    for f in fileList:
        print('{} '.format(idx) + f)
        idx = idx + 1

    print(' ')
    #choice = input('Select a number from the list above :')
    choice = '-1'
    while (int(choice) < 1 or int(choice) >= idx):
        choice = input('Select a number from the list above (0 = exit): ')
        if choice == '0':
            exit()
# index of selected file into List
        selected = int(choice) - 1
        print(fileList[selected])
        ionapi_file = fileList[selected]
# dictionary containing data read from file ionapi
        tokens = {}
        with open(ionapi_file, 'r') as f:
            line = f.readline()
#    print(line)
        tokens = json.loads(line)
        ti = tokens['ti']
        ci = tokens['ci']
        cs = tokens['cs']
        iu = tokens['iu']
        pu = tokens['pu']
        oa = tokens['oa']
        ot = tokens['ot']
        orr = tokens['or']
#ru = tokens['ru']
        if 'sask' in tokens:
            print('You have selected a BackEnd service file')
            print('Please select a web app file...')
            choice = '-1'
#            exit()


    filled_ru = False
    if 'ru' in tokens:
        ru = tokens['ru']
    else:
        while not filled_ru:
            ru = input('Enter the Redirect URL: (0 = exit) ')
            if ru != '' and ru != '0':
                filled_ru = True
            else:
                if ru != '' and ru == '0':
                    exit()    

    tokens['ru'] = ru
#    print(tokens)
    return tokens

   

