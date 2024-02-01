def compactar_vetor_booleano(vetor_booleano):
    dados_empacotados = bytearray()
    byte_atual = 0
    posicao_bit = 0

    for valor in vetor_booleano:
        if valor:
            byte_atual |= (1 << posicao_bit)
        posicao_bit += 1

        if posicao_bit == 8:
            dados_empacotados.append(byte_atual)
            byte_atual = 0
            posicao_bit = 0

    if posicao_bit > 0:
        dados_empacotados.append(byte_atual << (8 - posicao_bit))

    return dados_empacotados

def descompactar_vetor_booleano(dados_empacotados, comprimento_vetor):
    vetor_booleano = []

    for byte in dados_empacotados:
        for _ in range(8):
            vetor_booleano.append((byte & 0b10000000) != 0)
            byte <<= 1

    return vetor_booleano[:comprimento_vetor]

# Exemplo de uso
vetor_original = [True, False, False, True, True, True, True, False]

# Compactando o vetor booleano
dados_empacotados = compactar_vetor_booleano(vetor_original)
print("Vetor compactado:", dados_empacotados)

# Descompactando o vetor booleano
vetor_descompactado = descompactar_vetor_booleano(dados_empacotados, len(vetor_original))
print("Vetor descompactado:", vetor_descompactado)
