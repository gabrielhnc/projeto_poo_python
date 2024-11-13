from menu import Menu
from bancodedados import BancoDeDados

if __name__ == "__main__":
    banco = BancoDeDados(host="host", user="user", password="password", database="database") #Entrada de dados para a conexão com o banco

    banco.conectar()

    menu = Menu(banco)
    opcao = menu.exibir_menu_principal()

    banco.desconectar()
