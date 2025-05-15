tamanho_bloco = 64
rodadas = 16
tamanho_bloco_divisao = tamanho_bloco // 2
K = "133457799BBCDFF1"
#6B5AB032706A1DDA
def transforma_em_blocos_64bits(texto_hex):
    binario = hexadecimal_para_binario(texto_hex)
    while len(binario) % tamanho_bloco != 0:
        binario += '0'
    blocos = [binario[i:i+tamanho_bloco] for i in range(0, len(binario), tamanho_bloco)]
    return blocos

def divide_em_dois_blocos(bloco):
    left = bloco[:tamanho_bloco_divisao]
    right = bloco[tamanho_bloco_divisao:]
    return left, right

def junta_em_um_bloco(left, right):
    return left + right

def binario_para_hexadecimal(binario_str):
    return f'{int(binario_str, 2):0{len(binario_str)//4}X}'

def hexadecimal_para_binario(texto_hex):
    binario = bin(int(texto_hex, 16))[2:]
    binario = binario.zfill(len(texto_hex) * 4)
    return binario

def shift_chaveK_pra_direita(chaveK):
    shiftchaveK = ''
    shiftchaveK = chaveK[-1]
    faz_shift = chaveK[:-1]
    shiftchaveK += faz_shift
    return shiftchaveK

def funcaoF(right, chaveK):
    Newright = ''
    for i in range(len(right)):
        if right[i] == chaveK[i]:
            Newright += '0' 
        else:
            Newright += '1' 

    return Newright

def xorLR(left, right):
    Newright = ''
    for i in range(len(left)):
        if left[i] == right[i]:
            Newright += '0' 
        else:
            Newright += '1' 
    return Newright

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
                aux_left = left
                left = funcaoF(left, chave_local)
                left = xorLR(right, left)
                right = aux_left
                print(f"Rodada {rodada + 1}: Left: {left} Right: {right}")

            blocox = junta_em_um_bloco(left, right)
            bloco_hex = binario_para_hexadecimal(blocox)
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
