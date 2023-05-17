import time
import math

# Sair do programa    
def sair():
    
    print("\nDesligando...")
    time.sleep(1)

# Menu do programa
def menu():
    
    while True:
        # Exibição do menu
        print("---------------Menu---------------")
        print("Selecione uma opção:")
        print("1 - ")
        print("2 - Sair\n")
    
        # Solicita a escolha do usuário
        escolha = input()
        
        # Caso 1 -
        if escolha == "1":
            # placeholder
            break
        elif escolha == "2":
            sair()
            break
        else: # Validação de entrada
            print("Opção inválida. Tente novamente.")

menu() # Execução do algoritmo