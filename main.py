# Júlia Moraes da Silva 20230014434
#Fiz uma funçaõ de menu para facilitar a visualização, assim pode ver elas funcionando uma de cada vez.Recomendo aumentar o terminal para pode ver os prints sem ter que ficar subindo. 

from table import *

def menu():
    print("1. Criar tabela")
    print("2. Adicionar uma linha")
    print("3. Remover uma linha")
    print("4. Adicionar uma coluna")
    print("5. Remover uma coluna")
    print("6. Somar colunas numéricas")
    print("7. Média das colunas numéricas")
    print("8. Exibir tabela")
    print("9. Abrir CSV")
    print("10. Filtrar a tabela")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            tabela1 = criar_tabela(['Ator','Personagem','Idade'],[['Zendaya','Hunter Schafer','Jacob Elordi','Sydney Sweeney','Maude Apatow','Barbie Ferreira','Algee Smith'],['Rue Bennet','Jules Vaughn','Nate Jacobs','Cassie Howard','Lexie Howard','Kat Hernandez','Mackay'],[27,25,26,26,26,27,29]])
            print(tabela1)
        elif escolha == '2':
            print(adicionar_linha(tabela1, ['Alexa Demie', 'Madelaine Perez', 33]))
        elif escolha == '3':
            print(remover_linha(tabela1,6))
        elif escolha == '4':
            print(adicionar_coluna(tabela1,'Altura',[1.78,1.78,1.96,1.61,1.63,1.68,1.67]))
        elif escolha == '5':
            print(remover_coluna(tabela1, 'Personagem'))
        elif escolha == '6':
            print(somar_coluna(tabela1))
        elif escolha == '7':
            print(media_coluna(tabela1))
        elif escolha == '8':
            exibir_tabela(tabela1)
        elif escolha == '9':
            tabela2 = abrir_csv('catalogo_livros.csv') 
            print(tabela2)
        elif escolha == '10':
            print(filtro(tabela1,verific_idade))
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()









