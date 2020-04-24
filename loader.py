from requests import post

def selector():
    """Essa função desenha na tela uma tabela com os cheats

      Returns:
      int:selector: cheat selecionado
     """
    print(
        f'ID{colors["red"]}| {colors["white"]}Developer {colors["red"]}|{colors["white"]} Tipo{colors["red"]} |{colors["white"]} Status')
    for v, c in enumerate(cheat[0]):
        print(f" {cheat[0][v]:^2} {cheat[1][v]}   {cheat[2][v]}   {cheat[3][v]}")
    print('-' * 29)
    selector = int(input(f'Selecione o cheat desejado pelo {colors["red"]} ID {colors["white"]}>>> '))

    return selector

# LISTA DE CHEATS
cheat = [["0", "1"], ["Developer", "Developer"], ["FREE", "FREE"], ["OFF", "ON"]]

# VARIAVEL DE CORES
colors = {}
colors['white'] = "\033[1;30m"
colors['red'] = "\033[1;31m"
colors['green'] = "\033[1;32m"
colors['yeallow'] = "\033[1;33m"
colors['blue'] = "\033[1;34m"
colors['purple'] = "\033[1;35m"
colors['cian'] = "\033[1;36m"
colors['black'] = "\033[1;37m"


# VARIAVEIS DE LOGIN
print(f'{colors["white"]}------------{colors["red"]}LOGIN{colors["white"]}------------')
username = str(input('Username >>> '))
password = str(input('Password >>> '))
print('-' * 29)

# REQUEST
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = post("https://yourpath/loader/login.php", data={"login": "loginmode", "username": username, "password": password}, headers={'User-Agent': user_agent})

# VERIFICANDO SE LOGIN ESTÁ CORRETO
if(request.text == "true"):
    print(f'{selector()} foi o cheat selecionado')
elif (request.text == "incorrect"):
    print("username or password wrong")
