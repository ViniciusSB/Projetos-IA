import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Cria as variáveis do problema
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'comida') #Valor máximo 10
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico') #Valor máximo 10
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta') #Valor máximo 20

# Criando função de pertinencia para a comida
# Essa função cria automaticamente o mapeamento entre valores nítidos e difusos
# Gera um gráfico a partir dos valores setados (valores nebulosos) com os índices de qualificação (0 a 10)
comida.automf(names=['péssima', 'comível', 'deliciosa'])


# Criando função de pertinencia para o serviço (tipos variados)
servico['ruim'] = fuzz.trimf(servico.universe, [0, 0, 5]) #Função triangulo 
servico['aceitável'] = fuzz.gaussmf(servico.universe, 5, 2) #Função gaussiana 
servico['excelente'] = fuzz.gaussmf(servico.universe, 10,3) #Função gaussiana

# Criando função de pertinencia para a gorjeta (tipos variados)
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 13]) #Função triangulo 
gorjeta['média'] = fuzz.trapmf(gorjeta.universe, [0, 13,15, 25]) #Função trapézio
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [15, 25, 25]) #Função triangulo 

# Graficos gerados a partir das funções de partinênci
comida.view()
servico.view()
gorjeta.view()


# Adicionando regras nas funçoes
rule1 = ctrl.Rule(servico['excelente'] | comida['deliciosa'], gorjeta['alta'])
rule2 = ctrl.Rule(servico['aceitável'], gorjeta['média'])
rule3 = ctrl.Rule(servico['ruim'] & comida['péssima'], gorjeta['baixa'])


# Criando e simulando um controlador nebuloso 
gorjeta_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
gorjeta_simulador = ctrl.ControlSystemSimulation(gorjeta_ctrl)

# Atribuindo valores para qualidade da comida e do serviço
gorjeta_simulador.input['comida'] = 9
gorjeta_simulador.input['servico'] = 2

# Computando o valor da gorjeta 
gorjeta_simulador.compute()
print(gorjeta_simulador.output['gorjeta'])

# Mostrando graficamente o resultado
comida.view(sim=gorjeta_simulador)
servico.view(sim=gorjeta_simulador)
gorjeta.view(sim=gorjeta_simulador)