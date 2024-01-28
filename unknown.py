menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 4:
            print('Çıkış yapılıyor.')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')

from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
bool = True

while bool:
        kelime=input("Çevirilecek Kelimeyi girin:")
        if(kelime=="q"):
            bool=False
            print("Çıkıldı")
        else:
            translation=translator.translate(kelime,src='tr',dest='en')
        print(f"{translation.origin} ===> {translation.text}")