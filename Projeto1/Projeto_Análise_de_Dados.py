import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"Pesquisa sobre a renda: aumentou, manteve ou diminuiu"


dictionary = {'Parâmetros': ('Aumentou', 'Manteve', 'Diminuiu'), 'Número de pessoas': (316, 1198, 3493)}
schedule = pd.DataFrame(dictionary)

fig, ax = plt.subplots(figsize=(16, 9))

ax.bar(schedule['Parâmetros'], schedule['Número de pessoas'])

ax.set_xlabel('Respostas')
ax.set_ylabel('Número de pessoas')
ax.set_title('Renda dos brasileiros durante a pandemia (até 03/2021)')
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')

plt.show()
plt.close()


"Composição da renda familiar: toda, maior parte, não contribuem, não possuem família"

dictionary_2 = {'Parâmetros': ('Toda', 'Maior parte', 'Não contribuem', 'Não possuem família'), 'Número de pessoas': (1985, 1727, 225, 132)}
schedule_2 = pd.DataFrame(dictionary_2)

fig_2, ax = plt.subplots(figsize=(16, 9))

ax.bar(schedule_2['Parâmetros'], schedule_2['Número de pessoas'])

ax.set_xlabel('Respostas')
ax.set_ylabel('Número de pessoas')
ax.set_title('Participação da composição da renda familiar durante a pandemia (até 03/2021)')
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')

plt.show()
plt.close()

"Aumento nos gastos habituais"

dictionary_3 = {'Parâmetros': ('Sim', 'Não'), 'Número de pessoas': (4350, 657)}
schedule_3 = pd.DataFrame(dictionary_3)

fig_3, ax = plt.subplots(figsize=(16, 9))

ax.bar(schedule_3['Parâmetros'], schedule_3['Número de pessoas'])
ax.set_xlabel('Respostas')
ax.set_ylabel('Número de pessoas')
ax.set_title('Aumento nos gastos habituais durante a pandemia (até 03/2021)')
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')

plt.show()
plt.close()

"Inflação"

meses = ['03/20', '04/20', '05/20', '06/20', '07/20', '08/20', '09/20', '10/20', '11/20', '12/20', '01/21', '02/21', '03/21']
inflacao = [3.3030, 2.399, 1.8775, 2.1322, 2.3055, 2.4383, 3.1352, 3.9182, 4.3111, 4.5173, 4.5591, 5.1953, 6.0993]
dictionary_inflacao = {'Meses': meses, 'Inflação': inflacao}
schedule_inflacao = pd.DataFrame(dictionary_inflacao)
print(schedule_inflacao)

plt.figure(figsize=(16, 9))
sns.lineplot(x='Meses', y='Inflação', data=dictionary_inflacao, label='Inflação', dashes=False, marker="o")
plt.ylim(1.8775, 6.0993)
plt.xlabel('Período')
plt.ylabel('Inflação acumulada (%)')
plt.title('Comportamento da inflação acumulada durante a pandemia (até 03/2021)')
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')

plt.show()
plt.close()
