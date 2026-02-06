from src.sectorization_algorithm import run_sectorization

#Para cenário com 20 bairros
from data.scenario_20_districts import V, A, C

#Para cenário com 30 bairros
#from data.scenario_30_districts import V, A, C 

run_sectorization(V, A, C)