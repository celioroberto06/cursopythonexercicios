def notas(*n, sit=False):
    '''
    -> Função para analizar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit:Valor opcional, idicando se deve ou não adicionar a situação.
    :return:Dicionário com várias informações sobre a turma.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] > 7:
            r['Situação'] = 'Boa'
        elif r['média'] >= 5:
            r['Situação'] = 'Razoavél'
        else:
            r['Situação'] = 'Ruim'
    return r
#programa principal
resp = notas(1.2, 3.8, 7.2, sit=True)
print(resp)
help(notas)
