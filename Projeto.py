import csv

def carregar_e_preparar_base(caminho_arquivo):
    """Lê o CSV usando a biblioteca padrão do Python e retorna as versões A e B."""
    dados_lista = []
    
    # Abre o arquivo CSV usando ponto e vírgula como separador
    with open(caminho_arquivo, mode='r', encoding='utf-8-sig') as arquivo: # encoding='utf-8-sig' remove o caractere invisível
        leitor = csv.DictReader(arquivo, delimiter=';')
        
        for linha in leitor:
            # Descobre se a chave chama 'id', '﻿id' ou 'id_cliente'
            chave_id = next(k for k in linha.keys() if 'id' in k.lower())
            
            # Converte o ID para número inteiro
            linha['id'] = int(linha[chave_id])
            dados_lista.append(linha)
            
    print(f"--- Base carregada com sucesso: {caminho_arquivo} ---")
    print(f"Total de registros: {len(dados_lista)}")
    
    # Versão A: Desordenada (como veio no arquivo)
    versao_a = dados_lista.copy()
    
    # Versão B: Ordenada crescentemente pelo 'id'
    versao_b = sorted(dados_lista, key=lambda x: x['id'])
    
    return versao_a, versao_b

# Bloco principal de execução
if __name__ == "__main__":
    caminho = r"C:/Users/Rana Luize/Documents/usuarios (1).csv"
    
    base_a, base_b = carregar_e_preparar_base(caminho)
    
    print("\nPrimeiro elemento da Versão A (Desordenada):")
    print(base_a[0])
    
    print("\nPrimeiro elemento da Versão B (Ordenada):")
    print(base_b[0])

    # ==========================================
# ALGORITMOS DE PESQUISA (Com contagem de comparações)
# ==========================================

# 1. Busca Linear Iterativa (Procura um por um usando um loop normal)
def busca_linear_iterativa(lista, id_alvo):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i]['id'] == id_alvo:
            return i, comparacoes # Retorna a posição (índice) e quantas comparações fez
    return -1, comparacoes # Retorna -1 se não encontrar

# 2. Busca Linear Recursiva (Procura um por um usando função que chama a si mesma)
def busca_linear_recursiva_aux(lista, id_alvo, indice, comparacoes):
    if indice >= len(lista):
        return -1, comparacoes
    comparacoes += 1
    if lista[indice]['id'] == id_alvo:
        return indice, comparacoes
    return busca_linear_recursiva_aux(lista, id_alvo, indice + 1, comparacoes)

def busca_linear_recursiva(lista, id_alvo):
    return busca_linear_recursiva_aux(lista, id_alvo, 0, 0)

# 3. Busca Binária Iterativa (Funciona na lista ordenada, cortando o caminho pela metade)
def busca_binaria_iterativa(lista, id_alvo):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio]['id'] == id_alvo:
            return meio, comparacoes
        elif lista[meio]['id'] < id_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

# 4. Busca Binária Recursiva (Busca binária feita com recursão)
def busca_binaria_recursiva_aux(lista, id_alvo, inicio, fim, comparacoes):
    if inicio > fim:
        return -1, comparacoes
    
    meio = (inicio + fim) // 2
    comparacoes += 1
    
    if lista[meio]['id'] == id_alvo:
        return meio, comparacoes
    elif lista[meio]['id'] < id_alvo:
        return busca_binaria_recursiva_aux(lista, id_alvo, meio + 1, fim, comparacoes)
    else:
        return busca_binaria_recursiva_aux(lista, id_alvo, inicio, meio - 1, comparacoes)

def busca_binaria_recursiva(lista, id_alvo):
    return busca_binaria_recursiva_aux(lista, id_alvo, 0, len(lista) - 1, 0)

if __name__ == "__main__":
    caminho = r"C:/Users/Rana Luize/Documents/usuarios (1).csv"
    base_a, base_b = carregar_e_preparar_base(caminho)
    
    # ID existente (o ID do primeiro cliente da base ordenada)
    id_para_procurar = base_b[0]['id']
    print(f"\n--- Testando buscas pelo ID: {id_para_procurar} ---")
    
    # 1. Testando Linear Iterativa na Base A (Desordenada)
    pos, comp = busca_linear_iterativa(base_a, id_para_procurar)
    print(f"Linear Iterativa -> Índice: {pos} | Comparações: {comp}")
    
    # 2. Testando Binária Iterativa na Base B (Ordenada)
    pos, comp = busca_binaria_iterativa(base_b, id_para_procurar)
    print(f"Binária Iterativa -> Índice: {pos} | Comparações: {comp}")

    # ==========================================
# ALGORITMOS DE ORDENAÇÃO (Com contagem de comparações e movimentações)
# ==========================================

def bubble_sort(arr):
    """Bubble Sort: Simples, O(n^2)."""
    lista = arr.copy()
    n = len(lista)
    comp, mov = 0, 0
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            comp += 1
            if lista[j]['id'] > lista[j + 1]['id']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                mov += 3  # 1 troca = 3 atribuições
                trocou = True
        if not trocou:
            break
    return lista, comp, mov


def selection_sort(arr):
    """Selection Sort: Simples, O(n^2)."""
    lista = arr.copy()
    n = len(lista)
    comp, mov = 0, 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if lista[j]['id'] < lista[min_idx]['id']:
                min_idx = j
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            mov += 3
    return lista, comp, mov


def insertion_sort(arr):
    """Insertion Sort: Simples, ótimo para dados quase ordenados."""
    lista = arr.copy()
    comp, mov = 0, 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if lista[j]['id'] > chave['id']:
                lista[j + 1] = lista[j]
                mov += 1
                j -= 1
            else:
                break
        if j >= 0:
            comp += 1
        lista[j + 1] = chave
        mov += 1
    return lista, comp, mov


def shell_sort(arr):
    """Shell Sort: Variação eficiente do Insertion Sort com lacunas (gaps)."""
    lista = arr.copy()
    n = len(lista)
    comp, mov = 0, 0
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap:
                comp += 1
                if lista[j - gap]['id'] > temp['id']:
                    lista[j] = lista[j - gap]
                    mov += 1
                    j -= gap
                else:
                    break
            if j >= gap:
                comp += 1
            lista[j] = temp
            mov += 1
        gap //= 2
    return lista, comp, mov


def merge_sort(arr):
    """Merge Sort: Eficiente, Divisão e Conquista, O(n log n)."""
    if len(arr) <= 1:
        return arr, 0, 0
    
    meio = len(arr) // 2
    esq_ord, c1, m1 = merge_sort(arr[:meio])
    dir_ord, c2, m2 = merge_sort(arr[meio:])
    
    resultado, c_merge, m_merge = _merge(esq_ord, dir_ord)
    return resultado, c1 + c2 + c_merge, m1 + m2 + m_merge

def _merge(esquerda, direita):
    resultado = []
    i = j = 0
    comp, mov = 0, 0
    while i < len(esquerda) and j < len(direita):
        comp += 1
        if esquerda[i]['id'] <= direita[j]['id']:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
        mov += 1
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
        mov += 1
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
        mov += 1
    return resultado, comp, mov


def quick_sort(arr):
    """Quick Sort: Eficiente, Pivoteamento, O(n log n) médio."""
    if len(arr) <= 1:
        return arr, 0, 0
    
    pivo = arr[len(arr) // 2]['id']
    menores = [x for x in arr if x['id'] < pivo]
    iguais = [x for x in arr if x['id'] == pivo]
    maiores = [x for x in arr if x['id'] > pivo]
    
    # Contagem aproximada para fins didáticos do relatório
    comp = len(arr) - 1
    mov = len(arr)
    
    esq_ord, c_esq, m_esq = quick_sort(menores)
    dir_ord, c_dir, m_dir = quick_sort(maiores)
    
    return esq_ord + iguais + dir_ord, comp + c_esq + c_dir, mov + m_esq + m_dir


def heapify(arr, n, i, metricas):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    
    if esq < n:
        metricas['comp'] += 1
        if arr[esq]['id'] > arr[maior]['id']:
            maior = esq
            
    if dir < n:
        metricas['comp'] += 1
        if arr[dir]['id'] > arr[maior]['id']:
            maior = dir
            
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        metricas['mov'] += 3
        heapify(arr, n, maior, metricas)

def heap_sort(arr):
    """Heap Sort: Eficiente baseado em árvore binária, O(n log n)."""
    lista = arr.copy()
    n = len(lista)
    metricas = {'comp': 0, 'mov': 0}
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i, metricas)
        
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        metricas['mov'] += 3
        heapify(lista, i, 0, metricas)
        
    return lista, metricas['comp'], metricas['mov']

# ==========================================
# FUNÇÃO DE BENCHMARK (30 repetições)
# ==========================================
import time

def benchmark_ordenacao(algoritmo_func, arr, repeticoes=30):
    """Executa o algoritmo 30 vezes para calcular a média de tempo exata."""
    tempos = []
    comp_registrada, mov_registrada = 0, 0
    
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        _, comp, mov = algoritmo_func(arr)
        fim = time.perf_counter()
        
        tempos.append(fim - inicio)
        comp_registrada = comp
        mov_registrada = mov
        
    tempo_medio = sum(tempos) / repeticoes
    return tempo_medio, comp_registrada, mov_registrada


# ==========================================
# BLOCO PRINCIPAL DE EXECUÇÃO
# ==========================================
if __name__ == "__main__":
    caminho = r"C:/Users/Rana Luize/Documents/usuarios (1).csv"
    base_a, base_b = carregar_e_preparar_base(caminho)
    
    # Lista com todos os algoritmos implementados
    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    
    print("\n" + "="*80)
    print(f"{'ALGORITMO':<18} | {'TEMPO MÉDIO (s)':<18} | {'COMPARAÇÕES':<15} | {'MOVIMENTAÇÕES'}")
    print("="*80)
    
    for nome, func in algoritmos:
        tempo, comp, mov = benchmark_ordenacao(func, base_a, repeticoes=30)
        print(f"{nome:<18} | {tempo:<18.6f} | {comp:<15} | {mov}")
        
    print("="*80)
if __name__ == "__main__":
    # Mudando para a base de 10k registros
    caminho = r"C:/Users/Rana Luize/Documents/usuarios (2).csv"
    base_a, base_b = carregar_e_preparar_base(caminho)
    
    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    
    print("\n" + "="*80)
    print(f"{'ALGORITMO':<18} | {'TEMPO MÉDIO (s)':<18} | {'COMPARAÇÕES':<15} | {'MOVIMENTAÇÕES'}")
    print("="*80)
    
    for nome, func in algoritmos:
        tempo, comp, mov = benchmark_ordenacao(func, base_a, repeticoes=30)
        print(f"{nome:<18} | {tempo:<18.6f} | {comp:<15} | {mov}")
        
    print("="*80)