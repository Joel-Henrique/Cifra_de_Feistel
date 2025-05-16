# Configurações iniciais
tamanho_bloco = 64  
rodadas = 16       
tamanho_bloco_divisao = tamanho_bloco // 2  
K = "133457799BBCDFF1"  

# Função para converter texto hexadecimal em blocos de 64 bits
def transforma_em_blocos_64bits(texto_hex):
    binario = hexadecimal_para_binario(texto_hex)
    # Preenchimento para múltiplos de 64 bits
    while len(binario) % tamanho_bloco != 0:
        binario += '0'

    blocos = [binario[i:i+tamanho_bloco] for i in range(0, len(binario), tamanho_bloco)]
    return blocos

# Função para dividir um bloco de 64 bits em dois blocos de 32 bits
def divide_em_dois_blocos(bloco):
    left = bloco[:tamanho_bloco_divisao]
    right = bloco[tamanho_bloco_divisao:]
    return left, right

# Junta dois blocos de 32 bits em um bloco de 64 bits novamente
def junta_em_um_bloco(left, right):
    return left + right

# Converte uma string binária para hexadecimal
def binario_para_hexadecimal(binario_str):
    return f'{int(binario_str, 2):0{len(binario_str)//4}X}'

# Converte uma string hexadecimal para binário
def hexadecimal_para_binario(texto_hex):
    binario = bin(int(texto_hex, 16))[2:]
    binario = binario.zfill(len(texto_hex) * 4)
    return binario

# Faz um shift circular de 1 bit para a direita na chave K
def shift_chaveK_pra_direita(chaveK):
    shiftchaveK = chaveK[-1] + chaveK[:-1]
    return shiftchaveK

# Função F simples: XOR entre right e a chave K
def funcaoF(right, chaveK):
    Newright = ''
    for i in range(len(right)):
        if right[i] == chaveK[i]:
            Newright += '0' 
        else:
            Newright += '1' 
    return Newright

# Realiza XOR entre os blocos left e right
def xorLR(left, right):
    Newright = ''
    for i in range(len(left)):
        if left[i] == right[i]:
            Newright += '0' 
        else:
            Newright += '1' 
    return Newright

# Gera uma lista de subchaves aplicando shifts sucessivos na chave inicial
def gera_subchaves(chave_inicial_bin):
    chaves = []
    chave_atual = chave_inicial_bin
    for _ in range(rodadas):
        chave_atual = shift_chaveK_pra_direita(chave_atual)
        chaves.append(chave_atual)
    return chaves


if __name__ == "__main__":
    chaveK = hexadecimal_para_binario(K)  
    print(f"\nChave hexadecimal em binário: {chaveK}")
    blocos_processados = []

    texto_entrada = input("Digite o texto cifrado em hexadecimal: ").strip()

    try:
        blocos = transforma_em_blocos_64bits(texto_entrada)

        # Gera as subchaves e inverte para simular decifragem
        subchaves = gera_subchaves(chaveK)
        subchaves.reverse()

        print(f"\nBlocos de {tamanho_bloco} bits:")
        for i, bloco in enumerate(blocos):
            left, right = divide_em_dois_blocos(bloco)
            print(f"\nBloco {i + 1}:")
            print(f"Binário completo:  {bloco}")
            print(f"Esquerda ({tamanho_bloco_divisao} bits): {left}")
            print(f"Direita  ({tamanho_bloco_divisao} bits): {right}")

            for rodada in range(rodadas):
                chave_local = subchaves[rodada]
                aux_left = left  # Guarda valor atual de left
                left = funcaoF(left, chave_local)
                left = xorLR(right, left)

                # Troca left e right para a próxima rodada
                right = aux_left

                print(f"Rodada {rodada + 1}: Left: {left} Right: {right}")

            # Junta blocos left e right após as rodadas
            blocox = junta_em_um_bloco(left, right)
            bloco_hex = binario_para_hexadecimal(blocox)

            # Armazena o bloco processado
            blocos_processados.append({
                'bloco_idx': i + 1,
                'bloco_final_bin': blocox,
                'bloco_final_hex': bloco_hex
            })

            print(f"Bloco final binário: {blocox}")
            print(f"Bloco final em Hex: {bloco_hex}")

        print("\nResumo dos blocos processados:")
        bloco_final_bin_total = ''
        bloco_final_hex_total = ''

        for bloco in blocos_processados:
            print(f"Bloco {bloco['bloco_idx']} Final em Hex: {bloco['bloco_final_hex']}")
            bloco_final_bin_total += bloco['bloco_final_bin']
            bloco_final_hex_total += bloco['bloco_final_hex']

        print(f"\nTodos blocos finais concatenados em BINÁRIO:\n{bloco_final_bin_total}")
        print(f"\nTodos blocos finais concatenados em HEXADECIMAL:\n{bloco_final_hex_total}")

    except ValueError:
        print("Erro: entrada inválida. Digite apenas caracteres hexadecimais (0-9, A-F).")
