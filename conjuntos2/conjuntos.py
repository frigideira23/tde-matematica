##João Pedro Frigeri de Oliveira.
def opUniao(conjunto1, conjunto2):
    uniao = sorted(set(conjunto1) | set(conjunto2))
    return f"União: conjunto 1 {{{', '.join(map(str, conjunto1))}}}, conjunto 2 {{{', '.join(map(str, conjunto2))}}}. Resultado: {{{', '.join(map(str, uniao))}}}"

def opIntersecao(conjunto1, conjunto2):
    intersecao = sorted(set(conjunto1) & set(conjunto2))
    return f"Interseção: conjunto 1 {{{', '.join(map(str, conjunto1))}}}, conjunto 2 {{{', '.join(map(str, conjunto2))}}}. Resultado: {{{', '.join(map(str, intersecao))}}}"

def opDiferenca(conjunto1, conjunto2):
    diferenca = sorted(set(conjunto1) - set(conjunto2))
    return f"Diferença: conjunto 1 {{{', '.join(map(str, conjunto1))}}}, conjunto 2 {{{', '.join(map(str, conjunto2))}}}. Resultado: {{{', '.join(map(str, diferenca))}}}"

def opCartesiano(conjunto1, conjunto2):
    produto_cartesiano = [(x, y) for x in conjunto1 for y in conjunto2]
    return f"Produto Cartesiano: conjunto 1 {{{', '.join(map(str, conjunto1))}}}, conjunto 2 {{{', '.join(map(str, conjunto2))}}}. Resultado: {{{', '.join(map(str, produto_cartesiano))}}}"

def executaOp(arquivos):
    for arquivo in arquivos:
        with open(arquivo, 'r') as f:
            num_operacoes = 0
            for line in f:
                if line.startswith('##'):
                    continue
                try:
                    num_operacoes = int(line.strip())
                    break
                except ValueError:
                    print(f"Aviso: Número de operações inválido no arquivo: {arquivo}")
                    num_operacoes = 0
                    break
            
            if num_operacoes == 0:
                print(f"Aviso: Nenhum número de operações encontrado no arquivo: {arquivo}")
                continue
            
            for _ in range(num_operacoes):
                operacao = next(f, '').strip()
                conjunto1 = [int(x) if x.isdigit() else x for x in next(f, '').strip().split(',') if not x.startswith('##')]
                conjunto2 = [int(x) if x.isdigit() else x for x in next(f, '').strip().split(',') if not x.startswith('##')]
                
                resultado = ""
                if operacao == 'U':
                    resultado = opUniao(conjunto1, conjunto2)
                elif operacao == 'I':
                    resultado = opIntersecao(conjunto1, conjunto2)
                elif operacao == 'D':
                    resultado = opDiferenca(conjunto1, conjunto2)
                elif operacao == 'C':
                    resultado = opCartesiano(conjunto1, conjunto2)
                
                if resultado:
                    print(resultado)

# Chamando a função para executar as operações dos arquivos 'opUm.txt', 'opDois.txt' e 'opTres.txt'
executaOp(['opUm.txt','opDois.txt','opTres.txt'])
