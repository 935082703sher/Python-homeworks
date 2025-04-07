class create_note:
    def __init__(self, id, text):
        self.id=id
        self.text=text
    def __str__(self):
        print( f'{self.id} {self.text} added succesfully')
        return f'id :{self.id} text :{self.text}'
class note_list:
    def __init__(self):
        self.list=[]
    def create_notes(self,note):
        self.list.append(note)
    def note(self):
        return self.list
    def des(self):
        for i in self.list:
            print(i)
    def update(self,i,new_value):
        self.list[i]=new_value

from IPython.display import clear_output   
! pip install time 
import time     
def print_menu():
    print('CHOOSE OPTION')
    print('1. SHOW ALL NOTES')
    print('2. SHOW NOTE DETAILS')
    print('3. CREATE NOTE')
    print('4. UPDATE NOTE')
    print('5. DELETE NOTE')
    print('Q. QUITE')
    print('M. MENU')
def main():
    code=note_list()
    while True:
        print_menu()
        choice = input('Enter your choice : ').upper()
        if choice=='1':
            print(code.des())
        elif choice =='2':
            id =int(input('enter:'))
            print(code.note(id-1))
        elif choice=='3':
            id=input("enter id: ")
            text=input('enter text : ')
            note=create_note(id,text)
            print( code.create_notes(note) )
        elif choice=='4':
            id =int(input('enter:'))
            text=input('enter text :')
            g=code.update((id-1),[id,text])
            print(g)
        elif choice=='5':
            id =int(input('enter:'))
            g=code.note()
            del g[id-1]
            print(g)
        elif choice=='Q':
            break
        elif choice=='M':
            print_menu
        else:
            print('enter coorect number or character')
        clear_output(wait=True)
        time.sleep(1)




    
        
