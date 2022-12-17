a = '''Here are some terms used in the databases and their translations.

PT(BR)  -  EN(USA)
CENTRO OESTE - brazilian region
SUL - brazilian region
SUDESTE - brazilian region
NORTE - brazilian region
NORDESTE - brazilian region
Acre (AC) - Brazilian states
Alagoas (AL) - Brazilian states
Amapá (AP) - Brazilian states
Amazonas (AM) - Brazilian states
Bahia (BA) - Brazilian states
Ceará (CE) - Brazilian states
Distrito Federal (DF) - Brazilian states
Espírito Santo (ES) - Brazilian states
Goiás (GO) - Brazilian states
Maranhão (MA) - Brazilian states
Mato Grosso (MT) - Brazilian states
Mato Grosso do Sul (MS) - Brazilian states
Minas Gerais (MG) - Brazilian states
Pará (PA) Paraíba (PB) - Brazilian states
Paraná (PR) - Brazilian states
Pernambuco (PE) - Brazilian states
Piauí (PI) - Brazilian states
Rio de Janeiro (RJ) - Brazilian states
Rio Grande do Norte (RN) - Brazilian states
Rio Grande do Sul (RS) - Brazilian states
Rondônia (RO) - Brazilian states
Roraima (RR) - Brazilian states
Santa Catarina (SC) - Brazilian states
São Paulo (SP) - Brazilian states
Sergipe (SE) - Brazilian states
Tocantins (TO)- Brazilian states
DATA INICIAL - Start date
DATA FINAL - End date
REGIÃO - REGION
ESTADO - states
PRODUTO - product
NÚMERO DE POSTOS PESQUISADOS
UNIDADE DE MEDIDA - UNIT OF MEASUREMENT
PREÇO MÉDIO REVENDA - AVERAGE RESALE PRICE
DESVIO PADRÃO REVENDA - RESALE STANDARD DEVIATION
PREÇO MÍNIMO REVENDA - MINIMUM RESALE PRICE
PREÇO MÁXIMO REVENDA - MAXIMUM RESALE PRICE
MARGEM MÉDIA REVENDA - AVERAGE MARGIN RESALE
COEF DE VARIAÇÃO REVENDA - COEFFICIENT OF RESALE VARIATION
PREÇO MÉDIO DISTRIBUIÇÃO - AVERAGE DISTRIBUTION PRICE
DESVIO PADRÃO DISTRIBUIÇÃO - STANDARD DEVIATION DISTRIBUTION
PREÇO MÍNIMO DISTRIBUIÇÃO - MINIMUM DISTRIBUTION PRICE
PREÇO MÁXIMO DISTRIBUIÇÃO - MAXIMUM DISTRIBUTION PRICE
COEF. (COEFICIENTE) DE VARIAÇÃO DISTRIBUIÇÃO - DISTRIBUTION COEFFICIENT OF VARIATION
ETANOL HIDRATADO - HYDROUS ETHANOL
ETANOL - ETHANOL
GASOLINA COMUM - REGULAR GASOLINE
DIESEL - DIESEL
'''

def subtittle():
    texto = ""
    texto += a
    
    while True:
        print(texto)
        if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break