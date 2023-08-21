import numpy as np

temperaturas = np.array([2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
    6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
    8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
    10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
    7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
    6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
    5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
    6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
    9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
    10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5])

media = np.average(temperaturas)
print(f"media: {media}")

mediana = np.median(temperaturas)
print(f"mediana: {mediana}")

desvio_padrao = np.std(temperaturas)
print(f"desvio padrao: {desvio_padrao}")

temperaturas_classificadas = np.chararray(temperaturas.size,itemsize=8,unicode=True)

for i in range (temperaturas.size):
    if(temperaturas[i] < 3.0):
        temperaturas_classificadas[i] = "Frio"
    elif(temperaturas[i] < 6.0):
        temperaturas_classificadas[i] = "Moderado"
    else:
        temperaturas_classificadas[i] = "Quente"

print(temperaturas_classificadas)

dias_mais_frios = np.where(temperaturas < (media - desvio_padrao))
print(f"Dias mais frios: {dias_mais_frios}")

dias_mais_quentes = np.where(temperaturas > (media + desvio_padrao))
print(f"Dias mais quentes: {dias_mais_quentes}")

