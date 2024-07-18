from data import User, Menu, pagers,admins,manager,orders
from time import sleep

#Code By Quitto

#Interface
def Start():
    print("Bem Vindo Al Restarante")
    name = input("Digite Seu Nome (opicional): ")
    if name == "":
        name = "tester"
    Card = str(input("Digite Seu Cartao (ID): "))

    global client_user #Em Versoes De Testes Foi Usados Parametros Para evitar conflito de variveis porem isso acabou criando um conflitro de parametros entre as funçoes que n deixava o code andar fazendo um break por falta de informaçaoes entao decidi colcaor a variavel client_user como global para facilitar o uso da variavel
    client_user = User(name=name, Card = Card, Admin = False, Money = 100)
    if Card == "0":
        client_user.Admin = True
        Admin_Panel()
    elif Card == "":
        print("Cartao Nao Pode Ser Aceito Tente Novamente! ")
        Start()
    else:
        Menu_Client()

def Menu_Client():
    client_food = []

    #Add Food
    def Add_Food():
        print(f"Menu: {Menu}")
        option = input("Digite Sua Opiçao: ")

        if option in Menu:
            client_food.append(option)
            run = input("Deseja Continuar ?: (y/n) ")
            if run.lower() == "y":
                Add_Food()
            elif run.lower() == "":
                Add_Food()
            else:
                Exit_Order(food_List=client_food)
        else:
            print("Opção inválida. Tente novamente.")
            Add_Food()
    #Exit Order
    def Exit_Order(food_List):
        total = sum(Menu[item] for item in client_food) #Passa Todos Os iten da dict para a arry pasanmdo os os valores somados
        print(f"Total do pedido: R$ {total:.2f}")

        pager = int(input("Digite Seu Pager: "))
        if pager in pagers:
            print("Pager Aceito!")
            sleep(1)
            if client_user.Money >= total:
                client_user.Money -= total
                print(f"Pedido confirmado! Seu saldo atual é: R$ {client_user.Money:.2f}")
                client_user.Money = 100.0
                orders.append(food_List)
                Start()
            else:
                print("Saldo insuficiente para completar o pedido.")
        else:
            print("Pager inválido. Pedido cancelado.")
            

    Add_Food()

# Adiministraçao (In Dev)
def Admin_Panel():
    def Login():
        if client_user.Admin:
            name = input("Digite Seu Nome: ")
            senha = input("Digite Sua Senha: ")
            for i in admins:
                if name == i["name"] and senha == i["senha"]:
                    Admin_Main()
                else:
                    print("Nome Ou Senha Estão Incorretos. Por favor, tente novamente. Se o problema persistir, informe um gerente.")
                    Start()
            Start()
        else:
            print("Você não possui acesso ao Painel Admin.")
            Start()
    
    def Admin_Main():
        def Manege_Menu():
            def Add_Item():
                item_name = input("Digite o Nome do Item: ")
                if item_name in Menu:
                    print("Este Iten Ja Esta No Menu")
                    sleep(0.5)
                    Add_Item()
                item_value = input("Digite o Valor do Item: ")
                Menu[item_name] = item_value
                print(f"Item {item_name} adicionado com sucesso.")
                Manege_Menu()

            def Remove_Item():
                item_name = input("Digite o Nome do Item: ")
                if item_name in Menu:
                    del Menu[item_name]
                    print(f"Item {item_name} removido com sucesso.")
                else:
                    print(f"Item {item_name} não encontrado.")
                Manege_Menu()

            print(f"Menu: {Menu}")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Voltar")
            c = input("Digite Sua Resposta: ")
            if c == "1":
                Add_Item()
            elif c == "2":
                Remove_Item()
            elif c == "3":
                Admin_Main()
        
        def Manege_Admin():
            def Add_Admin():
                Manager_Senha = input("Digite a Senha do Gerente: ")
                if Manager_Senha == manager:
                    name_new_admin = input("Digite o Nome do Novo Admin: ")
                    senha_new_admin = input("Digite a Senha do Novo Admin: ")
                    admins.append({"name": name_new_admin, "senha": senha_new_admin})
                    print(f"Admin {name_new_admin} adicionado com sucesso.")
                else:
                    print("Senha do gerente incorreta.")
                Manege_Admin()
                
            def Remove_Admin():
                Manager_Senha = input("Digite a Senha do Gerente: ")
                if Manager_Senha == manager:
                    name = input("Digite o Nome do Admin: ")
                    for i in admins:
                        if name == i["name"]:
                            admins.remove(i)
                            print(f"Admin {name} removido com sucesso.")
                            break
                    else:
                        print(f"Admin {name} não encontrado.")
                else:
                    print("Senha do gerente incorreta.")
                Manege_Admin()

            print("Admins: ", admins)
            print("1. Add Admin")
            print("2. Remove Admin")
            print("3. Voltar")
            c = input("Digite Sua Resposta: ")
            if c == "1":
                Add_Admin()
            elif c == "2":
                Remove_Admin()
            elif c == "3":
                Admin_Main()
        def Manege_Orders():
            #Funçoes
            def Remove_Order():
                print(f"Orders: {orders}")
                index_remove = int(input("Digite O Mumero Da Ordern Para Ser Removida (Orders E uma Arry ou seja o 1 valor e indicado como 0): "))
                del orders[index_remove]
                Manege_Orders()

            #Interface
            print(f"Orders: {orders}")
            print("1. Remover Order")
            print("2. Voltar")

            input_client = input("Digite Sua Resposta: ")
            if input_client == "1":
                Remove_Order()
            elif input_client == "2":
                Admin_Main()

            

        print("Bem Vindo ADM!!")
        print(f"Name: {client_user.name}")
        print("1. Manage Menu")
        print("2. Manage Admin")
        print("3. Manage Orders")
        print("4. Exit")
        command = input("Digite Sua Escolha: ")

        if command == "1":
            Manege_Menu()
        elif command == "2":
            Manege_Admin()
        elif command == "3":
            Manege_Orders()
        elif command == "4":
            Start()

    if client_user.Admin:
        Login()
    else:
        print("Você não possui acesso ao Painel Admin.")
        Start()
#Run Cod
if __name__ == "__main__":
    Start()