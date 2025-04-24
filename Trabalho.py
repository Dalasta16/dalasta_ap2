import pandas as pd

#Função achar valor
def valor_contabil(df, conta, descricao):
    filtro_conta = df['conta'].str.contains(conta, case=False)
    filtro_descricao = df['descricao'].str.contains(descricao, case=False)
    valor = (df[filtro_conta & filtro_descricao]['valor'].values[0])
    return valor

def valor_contabil_2(df, conta, descricao):
    filtro_conta = df['conta'].str.contains(conta, case=False)
    filtro_descricao = df['descricao'].str.contains(descricao, case=False)
    valor = (df[filtro_conta & filtro_descricao]['valor'].values[1])
    return valor

#2024 4T
arquivo = 'C:\\Users\\CRDalas\\Desktop\\Programacao\\Análise de Dados\\Trabalho_Cont\\dados\\vulc.xlsx'
df = pd.read_excel(arquivo)
#pesquisar
df[df['descricao'].str.contains('', case=False)][['conta','descricao','valor']]

#AC e PC
AC_24 = valor_contabil(df, '^1.0', '^ativo cir')

PC_24 = valor_contabil(df, '^2.0', '^passivo cir')



#Liquidez Corrente(LS)
LC_24 = AC_24/PC_24

#Liquidez Seca(LS)
estoque_24 = valor_contabil(df, '^1.0', '^estoque')
DA_24 = valor_contabil(df, '^1.0', '^despesa')
LS_24 = (AC_24-estoque_24-DA_24)/PC_24 

#Liquidez Imediata(LI)
caixa_24 = valor_contabil(df, '^1.0', '^caixa')
aplicacao_f_24 = valor_contabil(df, '^1.0', '^aplica')
disponivel_24 = caixa_24+aplicacao_f_24
LI_24 = disponivel_24/PC_24

#Liquidez Geral(LG)
ARNC_24 = valor_contabil(df, '^1.0*', '^ativo realiz')
PNC_24 = valor_contabil(df, '^2.0*', '^passivo n.o cir')
LG_24 = (AC_24+ARNC_24)/(PC_24+PNC_24)




#ACF
imposto_de_renda_ac_24 = valor_contabil(df, '^1.0', '^imposto de renda')
disponivel_24 = caixa_24+aplicacao_f_24
ACF_24 = disponivel_24+imposto_de_renda_ac_24
#ACO
ACO_24 = AC_24-ACF_24

#PCF
emprestimos_24 = valor_contabil(df, '^2.0', '^empr.stimo')
provisoes_24 = valor_contabil(df, '^2.0', '^provis.es')
imposto_de_renda_pc_24 = valor_contabil(df, '^2.0', '^imposto de renda')
dividendos_24 = valor_contabil_2(df, '^2.0', '^dividendos')
PCF_24 = (emprestimos_24+provisoes_24+imposto_de_renda_pc_24+dividendos_24)
#PCO
PCO_24 = (PC_24-PCF_24)

#Capital de Giro(CDG)
CDG_24 = AC_24 - PC_24

#Necessidade de Capital de Giro(NCG)
NCG_24 = ACO_24-PCO_24

#ST
ST_24 = ACF_24-PCF_24

#RELACAO CT/CP = PASSIVO/PL
PL_24 = valor_contabil(df,'^2.*','patrim.nio')
CTCP_24 = (PC_24+PNC_24)/PL_24

#ENDIVIDAMENTO GERAL = PASSIVO/PASSIVO+PL
endividamento_geral_24 = (PC_24+PNC_24)/(PC_24+PNC_24+PL_24)

#SOLVENCIA = ATIVO TOTAL/PASSIVO
AT_24 = valor_contabil(df,'^1.*','ativo total')
Solvencia_24 = AT_24/(PC_24+PNC_24)

#CE = PC/PASSIVO
CE_24 = PC_24/(PC_24+PNC_24)

#IPL = 3Is/PL
investimentos_24 = valor_contabil(df,'^1.*','^invest')
imobilizado_24 = valor_contabil(df,'^1.*','^imobilizado$')
intangivel_24 = valor_contabil(df,'^1.*','^intang*')
PL_24 = valor_contabil(df,'^2.*','patrim.nio')
IPL_24 = (investimentos_24+intangivel_24+imobilizado_24)/PL_24



#2023 4T
import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3OTEyOTAwLCJpYXQiOjE3NDUzMjA5MDAsImp0aSI6IjQ1MWIyZWM5YTAxMTQ4YjRiZDYxZDQ4MGI0YmM1OWU1IiwidXNlcl9pZCI6NjB9.kssQqfnXMDQxA_gny7-6Hfoaj5DGhfFjYAh_CwC6Yp8"
headers = {'Authorization': 'JWT {}'.format(token)}

params = {
'ticker': 'VULC4',
'ano_tri': '20234T',
}

r = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
r.json().keys()
dados = r.json()['dados'][0]
balanco = dados['balanco']
df_23 = pd.DataFrame(balanco)



#pesquisar
df_23[df_23['descricao'].str.contains('ativo total', case=False)][['conta','descricao','valor']]

#AC e PC
AC_23 = valor_contabil(df_23, '^1.0', '^ativo cir')
PC_23 = valor_contabil(df_23, '^2.0', '^passivo cir')



#Liquidez Corrente(LS)
LC_23 = AC_23/PC_23
#Liquidez Seca(LS)
estoque_23 = valor_contabil(df_23, '^1.0', '^estoque')
DA_23 = valor_contabil(df_23, '^1.0', '^despesa')
LS_23 = (AC_23-estoque_23-DA_23)/PC_23 
#Liquidez Imediata(LI)
caixa_23 = valor_contabil(df_23, '^1.0', '^caixa')
aplicacao_f_23 = valor_contabil(df_23, '^1.0', '^aplica')
disponivel_23 = caixa_23+aplicacao_f_23
LI_23 = disponivel_23/PC_23
#Liquidez Geral(LG)
ARNC_23 = valor_contabil(df_23, '^1.0*', '^ativo realiz')
PNC_23 = valor_contabil(df_23, '^2.0*', '^passivo n.o cir')
LG_23 = (AC_23+ARNC_23)/(PC_23+PNC_23)



#ACF
imposto_de_renda_ac_23 = valor_contabil(df_23, '^1.0', '^imposto de renda')
disponivel_23 = caixa_23+aplicacao_f_23
ACF_23 = disponivel_23+imposto_de_renda_ac_23
#ACO
ACO_23 = AC_23-ACF_23
#PCF
emprestimos_23 = valor_contabil(df_23, '^2.0', '^empr.stimo')
provisoes_23 = valor_contabil(df_23, '^2.0', '^provis.es')
imposto_de_renda_pc_23 = valor_contabil(df_23, '^2.0', '^imposto de renda')
dividendos_23 = valor_contabil_2(df_23, '^2.0', '^dividendos')
PCF_23 = (emprestimos_23+provisoes_23+imposto_de_renda_pc_23+dividendos_23)
#PCO
PCO_23 = (PC_23-PCF_23)
#Capital de Giro(CDG)
CDG_23 = AC_23 - PC_23
#Necessidade de Capital de Giro(NCG)
NCG_23 = ACO_23-PCO_23
#ST
ST_23 = ACF_23-PCF_23



#RELACAO CT/CP = PASSIVO/PL
PL_23 = valor_contabil(df_23,'^2.*','patrim.nio')
CTCP_23 = (PC_23+PNC_23)/PL_23
#ENDIVIDAMENTO GERAL = PASSIVO/PASSIVO+PL
endividamento_geral_23 = (PC_23+PNC_23)/(PC_23+PNC_23+PL_23)
#SOLVENCIA = ATIVO TOTAL/PASSIVO
AT_23 = valor_contabil(df_23,'^1.*','ativo total')
Solvencia_23 = AT_23/(PC_23+PNC_23)
#CE(Composição do endividamento) = PC/PASSIVO
CE_23 = PC_23/(PC_23+PNC_23)
#Indice de PL = 3Is/PL
investimentos_23 = valor_contabil(df_23,'^1.*','^invest')
imobilizado_23 = valor_contabil(df_23,'^1.*','^imobilizado$')
intangivel_23 = valor_contabil(df_23,'^1.*','^intang*')
PL_23 = valor_contabil(df_23,'^2.*','patrim.nio')
IPL_23 = (investimentos_23+intangivel_23+imobilizado_23)/PL_23



#Ciclos
df[df['descricao'].str.contains('fornecedor', case=False)][['conta','descricao','valor']]

#PME = (estoque med*360)/CMV
estoque_med = (estoque_23+estoque_24)/2
CMV = valor_contabil(df,'^3.*','custo')
PME = ((estoque_med*360)/CMV)*(-1)
#PMRV= (clientes med*360/Receita liquida))
clientes_23 = valor_contabil(df_23,'^1.*','clientes')
clientes_24 = valor_contabil(df,'^1.*','clientes')
clientes_med = (clientes_23+clientes_24)/2
Receita_liquida = valor_contabil(df,'^3.*','receita')
PMRV = (clientes_med*360)/Receita_liquida
#PMPF(fornecedor med*360/(Compra = Estoque Final - Estoque Inicial +CMV))
fornecedor_23 = valor_contabil(df_23,'^2.*','fornecedor')
fornecedor_24 = valor_contabil(df,'^2.*','fornecedor')
fornecedor_med = (fornecedor_23+fornecedor_24)/2
compra = estoque_24 - estoque_23 + CMV
PMPF = ((fornecedor_med*360)/compra)*(-1)


#CO
CO = PME + PMRV
#CF
CF = CO - PMPF
#CE
CE = PME