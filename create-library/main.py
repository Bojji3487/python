from pynput.keyboard import Listener as keyb
import time
class Library:
    count: int
    lentbooks: dict
    def __init__(self,books: list,libName):
        print(libName)
        self.count=0
        self.books=books
        self.libName=libName
        self.lentbooks={"example":"Neeraj"}
    
    def displayBooks(self,name: str):
        if(name=="all"):
            print('\n')
            print('\n')

            print('List of availaible books:')
            for item in self.books:
                print(item)
            print('\n')  
            print('List of lent books:') 
            for key,item in self.lentbooks.items():
                print(key,item)
        else:
            if name in self.books:
                time.sleep(1)
                print('\n')
                print(f'Yes.{name} exists in our library')
                print('Enter B to borrow this book: ')
                if(input()=="b"):
                    self.borrowBook(name)

                               
            elif name in self.lentbooks.keys():
                print(f'name={self.lentbooks[name]}')
            else:
                print('Not Found')
                return
        print('\n')

    def donateBook(self,name: str):
            if(name):
                if name not in self.books and name not in self.lentbooks.keys():
                    self.books.append(name)
                    print("Added succesfuly")
                else:
                    print('Already in Library')
            else:
                print("Invalid entry")

        
    def borrowBook(self,name):
        if name in self.books:
            if name in self.lentbooks.keys():
                print('Already Taken. Please wait till it is returned')
            else:
                print('Enter your name:')
                username=str(input())
                self.lentbooks[name]=username
                self.books.remove(name)
                print('Succesfully borrowed!! Please return after reading')
        else:
            print('Not available yet :(')
        
    def menu(self):

        temp=True
        while temp:
            time.sleep(1)
            print(f'\n Welcome to the menu')
            time.sleep(0.5)
            print('1. Display Book/s')
            time.sleep(0.5)
            print('2. Donate a Book')
            time.sleep(0.3)
            print('3. Borrow a book')
            time.sleep(0.2)
            print('4. Return a borrowed book')
            time.sleep(0.1)
            print('5. Exit\n')
            print('Enter your choice:',end=' ')
            choice=input()
            match choice:
                case "1":
                    name=input('Enter Name of book or enter all to display list:')
                    self.displayBooks(name)
                    time.sleep(1)
                case "2":
                    name=input('Enter Name of the book you want to donate:')
                    self.donateBook(name)
                case "3":
                    name=input('Enter Name of the book you want to borrow:')
                    self.borrowBook(name)
                case "4":
                    name=input('Enter Name of the book you want to return:')
                    if name in self.books:
                        print('Already present')
                        continue
                    if name not in self.lentbooks.keys():
                        print('Not lent, Don\'t lie')
                    else:
                        self.lentbooks.pop(name)
                        self.books.append(name)
                        print(f"Returned succesfuly!! Thank You")

                case "5":
                    temp=False
                    
                

libName = "Adam\'s Library"
libName = libName.center(100)
Lib1=Library(['A song of Ice and Fire','1984','Six of Crows'],libName)


Lib1.menu()
