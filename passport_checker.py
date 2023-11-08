#  By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Kuba
#               Ben Goertz
#               Owen Bell
# Section:      ENGR-102:533,557
# Assignment:   ASCII Art
# Date:         21 10 2023

thefile = input('Enter the name of the file: ')

Check_List = ['byr' , 'iyr', 'eyr' , 'hgt' , 'hcl' , 'pid' , 'cid']


with open(f'{thefile}') as File:
    lineN = File.read()
    passlist = lineN.split('\n\n')

count = 0

for passport in passlist:
    #ident is the type of identification
    for ident in Check_List:
        if ident in passport:
            thing = True
            continue
        else:
            thing = False
            break
    if thing == True:
        with open('valid_passports.txt' , 'a') as Valid_Pass:
            Valid_Pass.write(f'{passport}\n\n')
        count += 1



print(f'There are {count} valid passports')

