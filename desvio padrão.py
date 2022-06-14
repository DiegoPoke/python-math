import numpy

#capturando numeros e guardando em um vetor tipo lista
contador = 0
quantidade = int(input('quantos numero você vai usar para o calculo? '))
n = []
for contador in range(quantidade):
    nome = (input('numero {} ?'.format(contador + 1)))
    n.append(nome)
    contador+=1

n_float = [float(val) for val in n] #convert lista str to float

print('\033[1:40mDados escolhidos: {}\033[m'.format(n_float)) #print dos dados

md = numpy.average(n_float) #Média
vr = numpy.var(n_float)     #Variância
dp = numpy.std(n_float)     #desvio padrão

print('A Média é:{:.4f} '.format(md))
print('A Variância é:{:.4f} '.format(vr))
print('O Desvio Padrão é:{:.4f}'.format(dp))

