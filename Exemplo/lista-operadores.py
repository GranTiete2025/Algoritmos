def exercicio1():
    """Cálculo de Área de Retângulo"""
    print("\n" + "="*50)
    print("EXERCÍCIO 1: CÁLCULO DE ÁREA DO RETÂNGULO")
    print("="*50)
    
    try:
        comprimento = float(input("Digite o comprimento do retângulo: "))
        largura = float(input("Digite a largura do retângulo: "))
        
        area = comprimento * largura
        
        print(f"\nComprimento: {comprimento}")
        print(f"Largura: {largura}")
        print(f"Área = {area}")
        
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def exercicio2():
    """Conversão de Temperatura Celsius para Fahrenheit"""
    print("\n" + "="*50)
    print("EXERCÍCIO 2: CONVERSÃO DE TEMPERATURA")
    print("="*50)
    
    try:
        tempC = float(input("Digite a temperatura em Celsius: "))
        
        tempF = (tempC * 9/5) + 32
        
        print(f"\nTemperatura em Celsius: {tempC}°C")
        print(f"Temperatura em Fahrenheit: {tempF}°F")
        
    except ValueError:
        print("❌ Erro: Digite um valor numérico válido!")

def exercicio3():
    """Cálculo de Média Aritmética"""
    print("\n" + "="*50)
    print("EXERCÍCIO 3: MÉDIA ARITMÉTICA")
    print("="*50)
    
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        media = (nota1 + nota2 + nota3) / 3
        
        print(f"\nNota 1: {nota1}")
        print(f"Nota 2: {nota2}")
        print(f"Nota 3: {nota3}")
        print(f"Média = {media:.2f}")
        
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def exercicio4():
    """Cálculo de Distância Percorrida"""
    print("\n" + "="*50)
    print("EXERCÍCIO 4: CÁLCULO DE DISTÂNCIA")
    print("="*50)
    
    try:
        velocidade = float(input("Digite a velocidade (km/h): "))
        tempo = float(input("Digite o tempo (horas): "))
        
        distancia = velocidade * tempo
        
        print(f"\nVelocidade: {velocidade} km/h")
        print(f"Tempo: {tempo} horas")
        print(f"Distância = {distancia} km")
        
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def exercicio5():
    """Verificação de Número Par"""
    print("\n" + "="*50)
    print("EXERCÍCIO 5: VERIFICAÇÃO DE NÚMERO PAR")
    print("="*50)
    
    try:
        num = int(input("Digite um número inteiro: "))
        
        eh_par = (num % 2 == 0)
        
        print(f"\nNúmero: {num}")
        print(f"É par? {eh_par}")
        
        # Explicação adicional
        if eh_par:
            print(f"✅ {num} é par porque {num} % 2 = {num % 2}")
        else:
            print(f"❌ {num} é ímpar porque {num} % 2 = {num % 2}")
            
    except ValueError:
        print("❌ Erro: Digite um número inteiro válido!")

def exercicio6():
    """Cálculo do Delta da Equação do Segundo Grau"""
    print("\n" + "="*50)
    print("EXERCÍCIO 6: CÁLCULO DO DELTA")
    print("="*50)
    
    try:
        print("Equação: ax² + bx + c = 0")
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        
        delta = (b ** 2) - (4 * a * c)
        
        print(f"\nEquação: {a}x² + {b}x + {c} = 0")
        print(f"Delta = b² - 4ac")
        print(f"Delta = ({b})² - 4*{a}*{c}")
        print(f"Delta = {delta}")
        
        # Análise do delta
        if delta > 0:
            print("📊 Análise: Duas raízes reais e distintas")
        elif delta == 0:
            print("📊 Análise: Uma raiz real (raiz dupla)")
        else:
            print("📊 Análise: Nenhuma raiz real")
            
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def exercicio7():
    """Comparação de Valores com Diferença"""
    print("\n" + "="*50)
    print("EXERCÍCIO 7: COMPARAÇÃO DE VALORES")
    print("="*50)
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        condicao = (num1 > num2) and ((num1 - num2) > 10)
        diferenca = num1 - num2
        
        print(f"\nNúmero 1: {num1}")
        print(f"Número 2: {num2}")
        print(f"Diferença: {diferenca}")
        print(f"Resultado: {condicao}")
        
        # Explicação detalhada
        if num1 > num2:
            print(f"✅ {num1} > {num2} → Verdadeiro")
            if diferenca > 10:
                print(f"✅ Diferença {diferenca} > 10 → Verdadeiro")
                print("✅ Ambos verdadeiros → Resultado: True")
            else:
                print(f"❌ Diferença {diferenca} > 10 → Falso")
                print("❌ Um falso → Resultado: False")
        else:
            print(f"❌ {num1} > {num2} → Falso")
            print("❌ Primeira condição falsa → Resultado: False")
            
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def exercicio8():
    """Cálculo de Salário Líquido"""
    print("\n" + "="*50)
    print("EXERCÍCIO 8: CÁLCULO DE SALÁRIO LÍQUIDO")
    print("="*50)
    
    try:
        salario_bruto = float(input("Digite o salário bruto: R$ "))
        
        # Cálculos passo a passo
        desconto_inss = salario_bruto * 0.10
        salario_apos_inss = salario_bruto - desconto_inss
        
        desconto_ir = salario_apos_inss * 0.15
        salario_liquido = salario_apos_inss - desconto_ir
        
        print(f"\nSalário bruto: R$ {salario_bruto:.2f}")
        print(f"Desconto INSS (10%): R$ {desconto_inss:.2f}")
        print(f"Salário após INSS: R$ {salario_apos_inss:.2f}")
        print(f"Desconto IR (15%): R$ {desconto_ir:.2f}")
        print(f"Salário líquido: R$ {salario_liquido:.2f}")
        
    except ValueError:
        print("❌ Erro: Digite um valor numérico válido!")

def exercicio9():
    """Verificação de Triângulo Válido"""
    print("\n" + "="*50)
    print("EXERCÍCIO 9: VERIFICAÇÃO DE TRIÂNGULO VÁLIDO")
    print("="*50)
    
    try:
        a = float(input("Digite o primeiro lado do triângulo: "))
        b = float(input("Digite o segundo lado do triângulo: "))
        c = float(input("Digite o terceiro lado do triângulo: "))
        
        # Verifica as três condições
        cond1 = (a + b) > c
        cond2 = (a + c) > b
        cond3 = (b + c) > a
        
        eh_valido = cond1 and cond2 and cond3
        
        print(f"\nLados: a={a}, b={b}, c={c}")
        print(f"Condição 1: {a} + {b} > {c} → {cond1} ({a + b} > {c})")
        print(f"Condição 2: {a} + {c} > {b} → {cond2} ({a + c} > {b})")
        print(f"Condição 3: {b} + {c} > {a} → {cond3} ({b + c} > {a})")
        print(f"É válido? {eh_valido}")
        
        if eh_valido:
            print("✅ Triângulo VÁLIDO - Todas as condições são verdadeiras")
        else:
            print("❌ Triângulo INVÁLIDO - Pelo menos uma condição é falsa")
            
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def exercicio10():
    """Cálculo de Resistência Equivalente em Paralelo"""
    print("\n" + "="*50)
    print("EXERCÍCIO 10: RESISTÊNCIA EQUIVALENTE EM PARALELO")
    print("="*50)
    
    try:
        r1 = float(input("Digite o valor do primeiro resistor (ohms): "))
        r2 = float(input("Digite o valor do segundo resistor (ohms): "))
        
        # Verifica se os resistores são positivos e diferentes de zero
        if r1 <= 0 or r2 <= 0:
            print("❌ Erro: Os valores dos resistores devem ser positivos!")
            return
            
        req = (r1 * r2) / (r1 + r2)
        
        print(f"\nResistor 1 (R1): {r1} ohms")
        print(f"Resistor 2 (R2): {r2} ohms")
        print(f"Fórmula: Req = (R1 × R2) / (R1 + R2)")
        print(f"Resistência equivalente = {req:.2f} ohms")
        
        # Explicação do cálculo
        print(f"\n📊 Cálculo passo a passo:")
        print(f"   R1 × R2 = {r1} × {r2} = {r1 * r2}")
        print(f"   R1 + R2 = {r1} + {r2} = {r1 + r2}")
        print(f"   Req = {r1 * r2} / {r1 + r2} = {req:.2f}")
        
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")
    except ZeroDivisionError:
        print("❌ Erro: A soma dos resistores não pode ser zero!")

def main():
    """Menu principal do programa"""
    exercicios = {
        '1': ("Cálculo de Área do Retângulo", exercicio1),
        '2': ("Conversão de Temperatura", exercicio2),
        '3': ("Média Aritmética", exercicio3),
        '4': ("Cálculo de Distância", exercicio4),
        '5': ("Verificação de Número Par", exercicio5),
        '6': ("Cálculo do Delta", exercicio6),
        '7': ("Comparação de Valores", exercicio7),
        '8': ("Cálculo de Salário Líquido", exercicio8),
        '9': ("Verificação de Triângulo Válido", exercicio9),
        '10': ("Resistência Equivalente", exercicio10)
    }
    
    while True:
        print("\n" + "="*60)
        print("           🎯 MENU DE EXERCÍCIOS - OPERADORES")
        print("="*60)
        
        for key, (descricao, _) in exercicios.items():
            print(f"{key:2}. {descricao}")
        print(" 0. Sair")
        print("="*60)
        
        opcao = input("\nEscolha um exercício (0-10): ").strip()
        
        if opcao == '0':
            print("\n👋 Obrigado por usar o programa! Até mais!")
            break
        elif opcao in exercicios:
            try:
                print(f"\n▶️ Executando: {exercicios[opcao][0]}")
                exercicios[opcao][1]()
                input("\n⏸️ Pressione Enter para continuar...")
            except KeyboardInterrupt:
                print("\n\n⏹️ Exercício interrompido pelo usuário.")
        else:
            print("❌ Opção inválida! Escolha um número entre 0 e 10.")

# Executar o programa
if __name__ == "__main__":
    main()