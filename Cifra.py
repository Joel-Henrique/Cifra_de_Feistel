tamanho_bloco = 64
rodadas = 16
tamanho_bloco_divisao = tamanho_bloco // 2
K = "133457799BBCDFF1"

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

def binario_para_hexadecimal(binario_str):
    return f'{int(binario_str, 2):0{len(binario_str)//4}X}'

def hexadecimal_para_binario(texto_hex):
    binario = bin(int(texto_hex, 16))[2:]
    binario = binario.zfill(len(texto_hex) * 4)
    return binario

def remove_8bit(chaveK):
    NewchaveK_56 = ''
    for i in range(tamanho_bloco):
        if (i + 1) % 8 != 0:
            NewchaveK_56 += chaveK[i]
    return NewchaveK_56

def shift_chaveK_pra_direita(chaveK):
    shiftchaveK = ''
    shiftchaveK = chaveK[-1]
    faz_shift = chaveK[:-1]
    shiftchaveK += faz_shift
    # print(f"chave: {chaveK}")
    #print(f"nova chave: {shiftchaveK}")
    return shiftchaveK

def funcaoF(left, chaveK):
    Newright = ''
    for i in range(len(left)):
        if left[i] == chaveK[i]:
            Newright += '0' 
        else:
            Newright += '1' 

    #print(Newright)
    return Newright


if __name__ == "__main__":
    chaveK = hexadecimal_para_binario(K)
    print(f"\nChave hexadecimal em binário: {chaveK}")
    chaveK = remove_8bit(chaveK)
    print(f"\nChave hexadecimal em binário 56: {chaveK}\n")
    texto_entrada = input("Digite um texto em hexadecimal: ").strip()

    try:
        blocos = transforma_em_blocos_64bits(texto_entrada)

        print(f"\nBlocos de {tamanho_bloco} bits:")
        for i, bloco in enumerate(blocos):
            left, right = divide_em_dois_blocos(bloco)
            print(f"\nBloco {i+1}:")
            print(f"Binário completo:  {bloco}")
            print(f"Esquerda ({tamanho_bloco_divisao} bits): {left} ({int(left, 2)})")
            print(f"Direita  ({tamanho_bloco_divisao} bits): {right} ({int(right, 2)})")
            print(f"Esquerda em Hex: {binario_para_hexadecimal(left)}")
            print(f"Direita em Hex:  {binario_para_hexadecimal(right)}")

            for i in range(rodadas):
                 chaveK = shift_chaveK_pra_direita(chaveK)
                 right = funcaoF(right, chaveK)



    except ValueError:
        print("Erro: entrada inválida. Digite apenas caracteres hexadecimais (0-9, A-F).")