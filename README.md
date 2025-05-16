🛡️ Simulação de Cifra Feistel em Python

    Este projeto é uma simulação de uma cifra do tipo Feistel. Ele recebe um texto hexadecimal como entrada, divide em blocos de 64 bits e aplica 16 rodadas de processamento usando operações de XOR e shift de chave, simulando o funcionamento de algoritmos de criptografia em blocos.

📚 Funcionalidades

    Conversão de hexadecimal para binário.
    Divisão do texto em blocos de 64 bits.
    Processamento em 16 rodadas com chave de 64 bits.
    Operações de XOR entre blocos e chave.
    Troca de blocos (rede de Feistel simples).
    Resultado final em binário e hexadecimal.


⚙️ Como Executar
    Abra o terminal na pasta onde o projeto está localizado.
    Execute um dos seguintes comandos:
        python cifra.py
        ou
        python decriptação.py
🧾 O Que Acontece ao Executar
    Ao rodar o script, será exibido o seguinte prompt no terminal:
    Digite um texto em hexadecimal:
    Você deve inserir um texto qualquer codificado em hexadecimal, por exemplo: 0123456789ABCDEF
    O script processará o texto inserido e, ao final, exibirá uma saída como:
    Todos blocos finais concatenados em HEXADECIMAL:
    6B5AB032706A1DDA
    Este valor final é a chave encriptada resultante.

💡 Importante
    O texto de entrada deve conter apenas caracteres hexadecimais válidos: 0-9 e A-F (maiúsculas ou minúsculas).
    A inclusão de qualquer caractere inválido, como G, símbolos especiais ou espaços, causará erro na execução.


![alt text](image.png)