from PDI import PDI

if __name__ == "__main__":
    imagens = PDI()
    menu = "------ MENU -------\n1- Exibir imagem/histograma\n2- Equalizar imagem\n3- Equalizar a partir da especificação\n4- SAIR"
 
    while True:
        print(menu)
        try:
            n = int(input("Escolha uma opção acima: "))
        except ValueError:
            print("Digite apenas números disponíveis!")
            continue
        if n == 1:
            img = input("Digite o nome da imagem que será tratada: ")
            imagens.exibir_imagem(img)
            imagens.exibir_histograma(img)
        elif n == 2:
            img = input("Digite o nome da imagem: ")
            imagens.equalizar(img)
            
        elif n == 3:
            img_org = input("Digite o nome da imagem original: ")
            img_ref = input("Digite o nome da imagem de referência: ")
            imagens.especificada(img_org, img_ref)
            
        elif n == 4:
            print("Programa finalizado!")
            break
        else:
            print("Digite somente as opções disponíveis!")
