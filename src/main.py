from encrypt import hash_sha3_256
from os import system
from time import sleep

def interface():
    system('cls')
    print("PR03 - Segurança Computacional: Programação de algoritmos e Aplicações Criptográficas")
    print("Selecione uma opção:\n")
    print("1- Inserir texto para aplicação do algoritmo Hash")
    print("2 - Sair\n")
    option = int(input("Opção desejada: "))

    if option == 1:
        system('cls')
        word_ = (input("Insira o texto desejado: ")).encode('UTF-8')
        obj_hash = hash_sha3_256(word_)
        print(f'\nHash (Em bytes): \n{obj_hash.get_hash_bytes}\nTamanho: {len(obj_hash.get_hash_bytes)} bytes')
        print(f'\nHash (Em hexadecimal): \n{obj_hash.get_hash_hex} \nTamanho: {len(obj_hash.get_hash_hex)} bytes')
        print(f'\nTamanho do bloco interno (Em bits): \n{obj_hash.get_size_block*8}\n')
        input("Pressione Enter para voltar à tela inicial")
        return interface()

    elif option == 2:
        sleep(0.3)
        quit()

    else:
        input("\nOpção não existente.\nPressione Enter para voltar à tela inicial")
        return interface()
        
def main():
    return interface()

if __name__ == "__main__":
    main()