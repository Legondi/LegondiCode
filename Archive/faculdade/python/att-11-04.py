#faça um programa que efetue a leitura de três valores numéricos 
#representando os lados de um  triangulo. O programa devera verificar
#e informar se os lados fornecidos formam realmente um triangulo 
#(cada lado é menor que a soma dos outros lados). Se esta condição
#for verdadeira, deverá ser indicado qual tipo de triângulo foi formado:

#isósceles (dois lados iguais e um diferente) altura = (lado_igual ** 2 - (base / 2) ** 2) ** 0.5
#area = (base * altura) / 2

#escaleno s = (lado_1 + lado_2 + lado_3) / 2
#area = (s * (s - lado_1) * (s - lado_2) * (s - lado_3)) ** 0.5

#equilatero (todos os lados iguais) area = (lado ** 2 * (3 ** 0.5)) / 4


ladoA = float(input("Digite o Lado A do Triângulo"))
ladoB = float(input("Digite o Lado B do Triângulo"))
ladoC = float(input("Digite o Lado C do Triângulo"))

