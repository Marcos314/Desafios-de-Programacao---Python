'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
Entrada
O arquivo de entrada contém um valor inteiro N.
Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
Exemplo de Entrada	Exemplo de Saída
556                 0:9:16           '''

n = int(input())
h = n // 3600
m = n % 3600
minutos = m // 60
seg = n % 60
print('{}:{}:{}'.format(h,minutos,seg))
