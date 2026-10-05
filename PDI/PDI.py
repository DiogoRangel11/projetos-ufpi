import cv2 as cv
import sys
import matplotlib.pyplot as plt
import numpy as np

class PDI:
    def __init__(self):
        pass

    def imagem(self,img):
        img_recebida = cv.imread(cv.samples.findFile(img),  cv.IMREAD_GRAYSCALE)
        if img_recebida is None:
            sys.exit("Não é possível realizar a leitura da imagem.")
        return img_recebida
        
    
    def exibir_imagem(self,img):
        im = self.imagem(img)
        # Exibir a imagem original:
        print("Pressione 's' para salvar a imagem")
        cv.imshow("Display window", im)
        k = cv.waitKey(0)
        if k == ord('s'):
            cv.imwrite("polen.png", im)

    def exibir_histograma(self,img):
        im = self.imagem(img)
        plt.figure(figsize=(8,5))
        plt.title("Histograma da imagem")
        plt.xlabel("Intensidade de pixel [0 - 255]")
        plt.ylabel("Quantidade de pixel")

        plt.hist(im.flatten(), bins=256, range=[0, 256], color='red', edgecolor='black')
        plt.xlim([0, 256])
        plt.show()

    def equalizar(self,img):
        im = self.imagem(img)
        vetor_imagem = im.flatten()
        histograma = [0] * 256

        for p in vetor_imagem:
            histograma[p] += 1

        altura, largura = im.shape
        total_pixels = largura * altura

        #Calculo do CDF:
        cdf = [0] * 256
        for i in range(len(histograma)):
            if i == 0:
                prob = histograma[i]/total_pixels
                cdf[i] = prob
            else:
                prob = histograma[i]/total_pixels
                cdf[i] = cdf[i - 1] + prob
        
        #Mapeamento (LUT):
        lut = [0] * 256
        for i in range(len(cdf)):
            s = 255 * cdf[i]
            lut[i] = round(s)

        #Equalização:
        for i in range(len(vetor_imagem)):
            vetor_imagem[i] = lut[vetor_imagem[i]]

        imagem_equalizada = vetor_imagem.reshape(altura, largura)
        res = np.hstack((im,imagem_equalizada))

        cv.imwrite('imagem_equalizada.png',imagem_equalizada)
        cv.imshow("Display window", res)
        k = cv.waitKey(0)
        if k == ord('0'):
            cv.imwrite("polen.png", im)
        print("Imagem equalizada com sucesso!\nSaída:'imagem_equalizada.png'")
        #equ = cv.equalizeHist(im) - Função pronta de equalização do pacote OpenCv

    def especificada(self, img_org, img_ref):
        #Calcular o CDF da imagem original
        img_orginal = self.imagem(img_org)
        vetor_imagem1 = img_orginal.flatten()
        histograma_org = [0] * 256
        
        for p in vetor_imagem1:
            histograma_org[p] += 1
        
        altura_org, largura_org = img_orginal.shape
        total_pixels_org = largura_org * altura_org
        
        #Calculo do CDF:
        cdf_org = [0] * 256
        for i in range(len(histograma_org)):
            if i == 0:
                prob = histograma_org[i]/total_pixels_org
                cdf_org[i] = prob
            else:
                prob = histograma_org[i]/total_pixels_org
                cdf_org[i] = cdf_org[i - 1] + prob

        #Calcular o CDF da imagem de referência        
        img_referencia = self.imagem(img_ref)
        vetor_imagem2 = img_referencia.flatten()
        histograma_ref = [0] * 256
        
        for p in vetor_imagem2:
            histograma_ref[p] += 1
        
        altura_ref, largura_ref = img_referencia.shape
        total_pixels_ref = largura_ref * altura_ref
        
        #Calculo do CDF:
        cdf_ref = [0] * 256
        for i in range(len(histograma_ref)):
            if i == 0:
                prob = histograma_ref[i]/total_pixels_ref
                cdf_ref[i] = prob
            else:
                prob = histograma_ref[i]/total_pixels_ref
                cdf_ref[i] = cdf_ref[i - 1] + prob

        #Mapeamento (LUT):
        lut = [0] * 256
        for i in range(len(cdf_org)):
            menor_distancia = 1
            indice = 0
            for j in range(len(cdf_ref)):
                distancia = abs(cdf_org[i] - cdf_ref[j])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    indice = j
            lut[i] = indice

        #Equalização:
        for i in range(len(vetor_imagem1)):
            vetor_imagem1[i] = lut[vetor_imagem1[i]]

        img_especificada = vetor_imagem1.reshape(altura_org, largura_org)
        #res = np.hstack((img_orginal,img_referencia, img_especificada))
        
        cv.imwrite('imagem_especificada.png',img_especificada)
        cv.imshow("Display window", img_orginal)
        k = cv.waitKey(0)
        cv.imshow("Display window", img_referencia)
        k = cv.waitKey(0)
        cv.imshow("Display window", img_especificada)
        k = cv.waitKey(0)
        if k == ord('0'):
            cv.imwrite("Imagem_especificada.png", img_especificada)
        print("Imagem especificada com sucesso!\nSaída:'imagem_especificada.png'")
     
                


      





