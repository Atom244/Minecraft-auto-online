import os

def intro():
    print("\033[1;32;40m")
    print(''' ████     ████ ██ ████     ██ ████████   ██████  ███████       ██     ████████ ██████████
░██░██   ██░██░██░██░██   ░██░██░░░░░   ██░░░░██░██░░░░██     ████   ░██░░░░░ ░░░░░██░░░ 
░██░░██ ██ ░██░██░██░░██  ░██░██       ██    ░░ ░██   ░██    ██░░██  ░██          ░██    
░██ ░░███  ░██░██░██ ░░██ ░██░███████ ░██       ░███████    ██  ░░██ ░███████     ░██    
░██  ░░█   ░██░██░██  ░░██░██░██░░░░  ░██       ░██░░░██   ██████████░██░░░░      ░██    
░██   ░    ░██░██░██   ░░████░██      ░░██    ██░██  ░░██ ░██░░░░░░██░██          ░██    
░██        ░██░██░██    ░░███░████████ ░░██████ ░██   ░░██░██     ░██░██          ░██    
░░         ░░ ░░ ░░      ░░░ ░░░░░░░░   ░░░░░░  ░░     ░░ ░░      ░░ ░░           ░░     ''')
    print('''     ██     ██     ██ ██████████   ███████           ███████   ████     ██ ██       ██ ████     ██ ████████
    ████   ░██    ░██░░░░░██░░░   ██░░░░░██         ██░░░░░██ ░██░██   ░██░██      ░██░██░██   ░██░██░░░░░ 
   ██░░██  ░██    ░██    ░██     ██     ░░██       ██     ░░██░██░░██  ░██░██      ░██░██░░██  ░██░██      
  ██  ░░██ ░██    ░██    ░██    ░██      ░██ █████░██      ░██░██ ░░██ ░██░██      ░██░██ ░░██ ░██░███████ 
 ██████████░██    ░██    ░██    ░██      ░██░░░░░ ░██      ░██░██  ░░██░██░██      ░██░██  ░░██░██░██░░░░  
░██░░░░░░██░██    ░██    ░██    ░░██     ██       ░░██     ██ ░██   ░░████░██      ░██░██   ░░████░██      
░██     ░██░░███████     ░██     ░░███████         ░░███████  ░██    ░░███░████████░██░██    ░░███░████████
░░      ░░  ░░░░░░░      ░░       ░░░░░░░           ░░░░░░░   ░░      ░░░ ░░░░░░░░ ░░ ░░      ░░░ ░░░░░░░░ ''')

    print('\u001b[0m')

def auth(condition):
    if condition == 'in_intro':
        intro()
    else:
        pass
    authtoken = input("Введите команду для добавления токена авторизации: ")
    with open("data_token.txt", 'w') as f:
        f.write(authtoken)
        f.close()
    if authtoken == '/help':
        redata()
    ngrok_folder = input("Введите путь до ПАПКИ с ngrok.exe: ")
    with open("data_folder.txt", 'w') as f:
        f.write(ngrok_folder)
        f.close()
        os.system('cls')
        general()
    if ngrok_folder == '/help':
        redata()

def redata():
    print('\033[3;35;40mВы обратились к команде "/help", введите новые данные: \u001b[0m')
    auth('')

def general():
    with open("data_token.txt", 'r') as f:
        authtoken = f.readline()
        if authtoken == "":
            auth('')
    with open("data_folder.txt", 'r') as f:
        ngrok_folder = f.readline()
        if ngrok_folder == "":
            auth('')

    os.chdir(ngrok_folder)
    os.system(authtoken)
    print('Если случились какие-то проблемы, измените данные, введя команду "/help"')
    print("\033[1;32;40m")

    intro()

    port = input("\033[3;36;40mВведите порт сервера: \u001b[0m")
    if port == '/help':
        redata()
    os.system(f'ngrok.exe tcp --region eu {port}')

    input()


def id():
    case1 = os.path.exists('data_token.txt')
    case2 = os.path.exists('data_folder.txt')
    if case1 == True and case2 == True:
        general()
    else:
        auth('in_intro')


id()
