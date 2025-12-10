'''
Pandas 2025 - Ensinando Pandas
Ep 03 - Importando dados
'''

# %%
import pandas as pd

df = pd.read_clipboard(sep='\t')
df

# NaN   Acre	    AC	Rio Branco	164 122,2	830 018	    4,30	13 622 000	0,2	16 953,46	0,663	86,9%	17,0‰	73,9 anos
# NaN	Alagoas	    AL	Maceió	    27 767,7	3 127 683	108,61	46 364 000	0,8	13 877,53	0,631	80,6%	19,5‰	71,6 anos
# NaN	Amapá	    AP	Macapá	    142 814,6	733 759	    4,16	13 861 000	0,2	18 079,54	0,708	95%	    23,2‰	73,9 anos
# NaN	Amazonas	AM	Manaus	    1 570 745,7	3 941 613	2,05	86 560 000	1,4	21 978,95	0,674	93,1%	18,2‰	71,9 anos
# NaN	Bahia	    BA	Salvador	564 692,7	14 141 626	24,46	245 025 000	4,1	16 115,89	0,660	87%	    7,3‰	73,5 anos
# NaN	Ceará	    CE	Fortaleza	148 825,6	8 794 957	54,40	130 621 000	2,2	14 669,14	0,682	84,8%	14,4‰	73,8 anos

# fonte: https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil

