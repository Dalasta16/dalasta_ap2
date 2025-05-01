#Escolher empresa e trimestre
def dataframe(ticker, trimestre):
    import pandas as pd
    import requests

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3OTEyOTAwLCJpYXQiOjE3NDUzMjA5MDAsImp0aSI6IjQ1MWIyZWM5YTAxMTQ4YjRiZDYxZDQ4MGI0YmM1OWU1IiwidXNlcl9pZCI6NjB9.kssQqfnXMDQxA_gny7-6Hfoaj5DGhfFjYAh_CwC6Yp8"
    headers = {'Authorization': 'JWT {}'.format(token)}
    empresa = f"{ticker}"
    data = f"{trimestre}"

    params = {
    'ticker': empresa,
    'ano_tri': data,
    }

    r = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
    r.json().keys()
    dados = r.json()['dados'][0]
    balanco = dados['balanco']
    df = pd.DataFrame(balanco)
    return df

#Função achar valor
def valor_contabil(df, conta, descricao):
    filtro_conta = df['conta'].str.contains(conta, case=False)
    filtro_descricao = df['descricao'].str.contains(descricao, case=False)
    valor = (df[filtro_conta & filtro_descricao]['valor'].values[0])
    return valor

def valor_contabil_2(df, conta, descricao):
    filtro_conta = df['conta'].str.contains(conta, case=False)
    filtro_descricao = df['descricao'].str.contains(descricao, case=False)
    valor = sum(df[filtro_conta & filtro_descricao]['valor'].values)
    return valor



#Indices de Liquidez:
def indices_liquidez():
    Ativo_C = valor_contabil(df, '^1.0', '^ativo cir')
    Passivo_C = valor_contabil(df, '^2.0', '^passivo cir')
    L_Corrente = Ativo_C/Passivo_C
    Estoque = valor_contabil(df, '^1.0', '^estoque')
    Despesa_Antecipada = valor_contabil(df, '^1.0', '^despesa')
    L_Seca = (Ativo_C-Estoque-Despesa_Antecipada)/Passivo_C
    Caixa = valor_contabil(df, '^1.0', '^caixa')
    Aplicacao_F = valor_contabil(df, '^1.0', '^aplica')
    Disponivel = Caixa+Aplicacao_F
    L_Imediata = Disponivel/Passivo_C
    Ativo_RNC = valor_contabil(df, '^1.0*', '^ativo realiz')
    Passivo_NC = valor_contabil(df, '^2.0*', '^passivo n.o cir')
    L_Geral = (Ativo_C+Ativo_RNC)/(Passivo_C+Passivo_NC)
    return [L_Corrente, L_Seca, L_Imediata, L_Geral]


#Capital de Giro e Tesouraria:
def giro_tesouraria():
    Ativo_C = valor_contabil(df, '^1.0', '^ativo cir')
    Passivo_C = valor_contabil(df, '^2.0', '^passivo cir')
    Caixa = valor_contabil(df, '^1.0', '^caixa')
    Aplicacao_F = valor_contabil(df, '^1.0', '^aplica')
    Imposto_de_renda_AC = valor_contabil(df, '^1.0', '^imposto de renda')
    Disponivel = Caixa+Aplicacao_F
    Ativo_CF = Disponivel+Imposto_de_renda_AC
    Ativo_CO = Ativo_C-Ativo_CF
    Emprestimos = valor_contabil(df, '^2.0', '^empr.stimo')
    Provisoes = valor_contabil(df, '^2.0', '^provis.es')
    Imposto_de_renda_PC = valor_contabil(df, '^2.0', '^imposto de renda')
    Dividendos = valor_contabil_2(df, '^2.0', '^dividendos')
    Passivo_CF = (Emprestimos+Provisoes+Imposto_de_renda_PC+Dividendos)
    Passivo_CO = (Passivo_C-Passivo_CF)
    Capital_de_Giro = Ativo_C - Passivo_C
    Necessidade_de_CG = Ativo_CO-Passivo_CO
    Saldo_Tesouraria = Ativo_CF-Passivo_CF
    return [Capital_de_Giro, Necessidade_de_CG, Saldo_Tesouraria]


#teste
df = dataframe('VULC4', '20244T')
df[df['descricao'].str.contains('dividendos e', case=False)][['conta','descricao','valor']]
indices_liquidez()
giro_tesouraria()