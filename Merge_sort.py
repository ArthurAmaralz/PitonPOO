def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    l_esq = merge_sort(lista[:meio])
    l_dir = merge_sort(lista[meio:])

    return l_esq, l_dir

def merge(l_esq, l_dir):
    if not l_dir:
        return l_esq
    if not l_esq:
        return l_dir
    if l_esq[0] < l_dir[0]:
        return [l_esq[0]] + merge(l_esq[1:], l_dir)

    return [l_dir[0]] + merge(l_esq, l_dir[1:])