# By submitting this assignment, I agree to the following:
#   'Aggies do not lie, cheat, or steal, or tolerate those who do.'
#   'I have not given or received any unauthorized aid on this assignment.'
#
# Name:         Ezra Kuba
#               Owen Bell
#               Ben Goertz
# Section:      ENGR-102:533,557
# Assignment:   Lab 11.09.1
# Date:         08 11 2023


#import os
#os.chdir(r'C:\Users\ezrag\OneDrive\Desktop\VScode\VS_labs')


#Getting file name
thefile = input('Enter the name of the file: ')

#Initializing a lot of the checks that need lists
 
Valid_byr_List = [] #Birth year
Valid_iyr_List = [] #Issue year
Valid_eyr_List = [] #expiration year
Valid_cm_List = []  #Height in cm
Valid_inches_List = []  #Height in inches
Valid_Nums_List = []    #0-9 Numbers for Hair color, passport ID, and country ID
Valid_Letters_List = ['a' , 'b' , 'c' , 'd' , 'e' , 'f'] #Letters for Hair color

for i in range(1920 , 2008):#Birth year checks, first setting up the valid BYs
    Valid_byr_List.append(str(i))
def byr_Check(byr):         #Function for birth year check
    if byr in Valid_byr_List:
        return True
    else:
        return False

for i in range(2013 , 2024):#Setting up valid issue year checks
    Valid_iyr_List.append(str(i))
def iyr_check(iyr):         #Function for issue year check
    if iyr in Valid_iyr_List:
        return True
    else:
        return False

for i in range(2023 , 2034):#Setting up Valid expiration year checks
    Valid_eyr_List.append(str(i))
def eyr_check(eyr):     #Function for eyr check, if it is a valid year, return True
    if eyr in Valid_eyr_List:
        return True
    else:
        return False


#These are the checks for heights, first in cm and then in inches(in is a reserved key)
for i in range(150 , 194):
    Valid_cm_List.append(str(i))
def cm_check(cm):           #Function for Cm check
    if cm in Valid_cm_List:
        return True
    else:
        return False

for i in range(59 , 77):
    Valid_inches_List.append(str(i))
def inches_check(inches):           #Function for Inches check
    if inches in Valid_inches_List:
        return True
    else:
        return False


for i in range(10):         #Setting up Hair Color checks
    Valid_Nums_List.append(str(i))
def hcl_check(hcl):
    if hcl[0] != '#':   #If the first character is not a number, it is invalid
        return False
    else:
        for i in hcl[1:]:
            if i not in Valid_Nums_List and i not in Valid_Letters_List:
            #If there is a problem, check bool of this ^ line, I think it's right, but not 100%
                return False
            #If the char is not a Valid Letter or Number, it is invalid
        return True
        #If the hcl string passes the conditions, then it is true


def pid_check(pid): #Function for Passport ID check
    if len(pid) != 9:       #if the length is not 9, it is false
        return False
    for i in pid:
        if i not in Valid_Nums_List:    #if a non number detected, false
            return False
    return True

def cid_check(cid):     #Function for Country ID check
    for index , num in enumerate(cid):
        Lead_Zero = True
        if num == '0' and Lead_Zero == True:    #CID does not count leading zeroes, so we check for those
            continue
        else:                       #If it is not a lead zero, we continue the check like normal
                                    #Length must be 3
            Lead_Zero == False
            cid_list = list(cid[index:])
            break
    if len(cid_list) != 3:
        return False
    else:
        return True


Check_List = ['byr' , 'iyr', 'eyr' , 'hgt' , 'hcl' , 'pid' , 'cid']
Check_Dict = {'byr':byr_Check,
              'iyr':iyr_check,
              'eyr':eyr_check,
              'hgt':[inches_check , cm_check],
              'hcl':hcl_check,
              'pid':pid_check,
              'cid':cid_check}


with open(f'{thefile}') as File:
    lineN = File.read()
    passlist = lineN.split('\n\n')

#count = 0
Valid_Pass_List = []

for passport in passlist:
    for ident in Check_List:
        if ident in passport:
            thing = True
            continue
        else:
            thing = False
            break
    if thing == True:
        #with open('valid_passports.txt' , 'a') as Valid_Pass:
            #Valid_Pass.write(f'{passport}\n\n')
        Valid_Pass_List.append(passport)
        #count += 1

super_count = 0
for Valid_P in Valid_Pass_List:     #I am trying to split the string of each "person" into
                                    #The indvidual elements in a key:value format
                                    #Then splitting those and running the appropiate check
    
    Valid_P = Valid_P.strip()
    Valid_P = Valid_P.replace('\n',' ')
    Dict4Pass_List = Valid_P.split(' ')
    #print(f'This should be each element in a list:\n{Dict4Pass_List}\n')

    for ID_pair in Dict4Pass_List:
        Big_Bool = True

        ID_Val = ID_pair.split(':')
        #print(f'This should be a list with ID,Val: {ID_Val}')

        if ID_Val[0] in Check_Dict:

            if ID_Val[0] == 'hgt':
                if len(ID_Val[1]) == 5:
                    cm_val = ID_Val[1].replace('cm','')
                elif len(ID_Val[1]) == 4:
                    inches_val = ID_Val[1].replace('in','')

                if ID_Val[1] in Valid_inches_List:
                    Bool = Check_Dict[f'{ID_Val[0]}'][0](inches_val)
                elif ID_Val[1] in Valid_cm_List:
                    Bool = Check_Dict[f'{ID_Val[0]}'][1](cm_val)
            else:
                Bool = Check_Dict[f'{ID_Val[0]}'](ID_Val[1])
                #print(f'{ID_Val[0]} is {ID_Val[1]}, this evaluates to {Bool} based on the parameters given\n')

        if Bool == False:
            Big_Bool = False
            #print(f'False detected! Exiting now, check for error')
            break

    if Big_Bool == True:
        #print(f'This is a valid ID!')
        with open(r'valid_passports2.txt' , 'a') as super_valids:
            super_valids.write(f'{Valid_P}\n\n')
        super_count += 1





#print(f'There are {count} valid passports')
print(f'There are {super_count} valid passports')


