from pprint import pp
contact = {'emergency' : 112}
while True:
    # menu
print('1. Add contact')
print('2. View contact')   
print('3. Delete contact')
print('4. Exit')  
print("Select a number:") 
ch = int(input('Enter your choice: '))
if ch == 1:
    name = input('Enter name: ') 
    number = input('Enter number: ')
    contacts[name] = number 
    print("contacts saved")
elif ch == 2:
    pp(contacts, width=1)
elif ch == 3:
    name = input('Enter name: ')
    if name        
