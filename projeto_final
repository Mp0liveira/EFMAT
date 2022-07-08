import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import pandas as pd
import plotly.express as px
import base64

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
df = pd.read_csv('assets/Campeoes_Libertadores')
df2 = pd.read_csv('assets/titulos_por_pais')
df3 = pd.read_csv('assets/mais_titulos')
df3_1 = pd.read_csv('assets/percentual_campeoes')
df4 = pd.read_csv('assets/artilheiros')
df5 = pd.read_csv('assets/artilheiros_brasileiros')
df6 = pd.read_csv('assets/artilheiros_brasileiros_atividade')
df7 = pd.read_csv('assets/ultimos_10_campeoes')
df8 = pd.read_csv('assets/ultimos_10_campeos_pais')
df9 = pd.read_csv('assets/paises_finais')
df10 = pd.read_csv('assets/artilheiros_por_edicao')
df11 = pd.read_csv('assets/maiores_participantes')
df12 = pd.read_csv('assets/maiores_participantes_br')
df13 = pd.read_csv('assets/mais_vices')
df14 = pd.read_csv('assets/vitorias')
df15 = pd.read_csv('assets/tecnicos_vitorias')
df16 = pd.read_csv('assets/tecnicos_br_vitorias')
df17 = pd.read_csv('assets/campoes_seculo_xxi')
df18 = pd.read_csv('assets/campeoes_pais_seculo_xxi')
df19 = pd.read_csv('assets/decisoes')
df20 = pd.read_csv('assets/finais_mesmo_paises')
df21 = pd.read_csv('assets/times_mais_gols')
image_penarol = 'assets/campeao.jpg'
image_estudiantes = 'assets/estudiantes.jpg'
image_santos = 'assets/santos.jpg'


def b64_penarol(image_penarol):
    with open(image_penarol, 'rb') as f:
        image = f.read()
    return 'data:campeao/jpg;base64,' + base64.b64encode(image).decode('utf-8')


def b64_estudiantes(image_estudiantes):
    with open(image_estudiantes, 'rb') as f:
        image = f.read()
    return 'data:estudiantes/jpg;base64,' + base64.b64encode(image).decode('utf-8')


def b64_santos(image_santos):
    with open(image_santos, 'rb') as f:
        image = f.read()
    return 'data:santos/jpg;base64,' + base64.b64encode(image).decode('utf-8')


opcoes = ['Títulos por país', 'Maiores campeões', 'Maiores artilheiros', 'Maiores artilheiros brasileiros',
          'Maiores artilheiros brasileiros em atividade', 'Maiores artilheiros em uma única edição', 'Clubes com mais'
                                                                                                     ' participações',
          'Clubes brasileiros com mais participações', 'Clubes que mais vezes disputaram a final',
          'Clubes com mais vitórias', 'Técnicos com mais vitórias', 'Técnicos brasileiros com mais vitórias',
          'Clubes com mais gols em uma única edição']

opcoes_pizza = ['Títulos por país', 'Todos os campeões', 'Últimos 10 campeões (por time)',
                'Últimos 10 campeões (por país)', 'Finais disputadas por país', 'Campeões (por time) no século XXI',
                'Campeões (por país) no século XXI', 'Tipos de decisões', 'Finais entre países']

fig = px.bar(df2, x='Países', y='Títulos')
fig_percentual = px.pie(df2, values='Títulos', names='Países')

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

style_img = {
    "margin-left": "-1rem",
    "margin-right": "15rem",
    "padding": "2rem 1rem"
}

style_legend = {
    "margin-left": "0rem"

}

style_estudiantes = {
    "margin-left": "20rem"

}
sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        html.P(
            "Escolha sobre o que quer saber da Copa Libertadores!", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("História", href="/", active="exact"),
                dbc.NavLink("Estatísticas", href="/page-1", active="exact"),
                dbc.NavLink("Sobre", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(children=[
            html.H1(children='História da Copa Libertadores da América'),
            html.H2(
                children='Aqui você vai ler brevemente sobre como surgiu a Copa Libertadores da América e qual a sua '
                         'importância para o futebol sulamericano!'),
            html.P(children='   A Copa Libertadores da América é a principal competição de clubes da América do Sul, '
                            'criada em 1960 pela CONMEBOL. O seu nome faz referência aos principais líderes da '
                            'independência dos países sulamericanos.\n    A primeira edição foi disputada em 1960, '
                            'contava com a participação de sete equipes e foi'
                            'vencida pelo Peñarol, equipe uruguaia. Até a atual edição (2022), 25 times diferentes '
                            'foram capazes de eternizarem seus nomes na tão sonhada taça. Só no Brasil, temos 7 times '
                            'distintos que já foram campeões. Para saber sobre mais dados como esses, acesse nossa '
                            'aba "Estatísticas" na barra lateral da página.'),
            html.Div(children=[
                html.Img(title='Time do Peñarol em 1960', src=b64_penarol(image_penarol), style=style_img),
                html.Img(title='Time Santos em 1962', src=b64_santos(image_santos)),
                html.Img(title='Time Estudiantes em 1968', src=b64_estudiantes(image_estudiantes),
                         style=style_estudiantes),
                html.H6('Da esquerda pra direita, temos os times do Peñarol (1960), Santos (1962) e Estudiantes '
                        '(1968), respectivamente. Peñarol foi o primeiro campeão, o Santos foi o primeiro  '
                        'brasileiro a conquistar a Taça, enquanto o Estudiantes foi o primeiro time a conquistar o '
                        'tricampeonato consecutivo.')
            ])
        ]),

    elif pathname == "/page-1":
        return html.Div(children=[
            html.H1(children='Estatísticas da Copa Libertadores da América'),
            html.H2(children='Aqui você encontra tudo sobre a Copa Libertadores! Experimente usar os nossos gráficos '
                             'interativos abaixo!'),

            dcc.Dropdown(opcoes, value='Títulos por país', id='opcoes_graficos'),
            html.H6(children='Este gráfico mostra a quantidade de títulos conquistados por países participantes.',
                    id='info'),

            dcc.Graph(
                id='grafico_titulos_pais',
                figure=fig
            ),

            dcc.Dropdown(opcoes_pizza, value='Títulos por país', id='opcoes_percentual'),
            html.H6(children='Este gráfico mostra o percentual de títulos conquistados por países participantes.',
                    id='info_percentual'),
            dcc.Graph(
                id='grafico_percentual',
                figure=fig_percentual
            )

        ])
    elif pathname == "/page-2":
        return html.Div(children=[
            html.H1(children='Sobre'),
            html.P(children='Projeto criado em base do trabalho final de Python (administrado pelo professor Lucas '
                            'Loureiro) do curso da EFMAT (Escola de Física e Matemática Aplicada). O foco do projeto'
                            ' constitui na criação de uma dashboard (aba "Estatística" do menu), o qual eu escolhi '
                            'fazer análises das estatísticas do campeonato de futebol "Copa Libertadores da América", '
                            'trazendo dados sobre os campeões, artilheiros, técnicos, clubes participantes, países'
                            ' e diversos dados quais julguei interessantes.'),
            html.P(children='Todos os dados foram retirados de pesquisas feitas pela internet, com base nos '
                            'dados oficiais da CONMEBOL (organizadora oficial da Copa Libertadores da América). Também'
                            ' foi utilizada a plataforma "Transformarket".  Todos '
                            'os dados estão atualizados com as informações disponíveis até o dia 29/06/2022, no qual o '
                            'último jogo da copetição foi a vitória do Athletico Paranaense sobre o Libertad por 2x1, '
                            'válido pelas oitavas de final da edição de 2022 da Copa Libertadores da América.'),
            html.P(children='Esse trabalho é de autoria de Marcos Paulo de Oliveira. ')

        ])


@app.callback(
    Output('grafico_titulos_pais', 'figure'),
    Input('opcoes_graficos', 'value')
)
def update_graph(value):
    if value == 'Títulos por país':
        figg = px.bar(df2, x='Países', y='Títulos', title='Títulos conquistados por país')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Maiores campeões':
        figg = px.bar(df3, x='Times', y='Títulos', title='Top 5 campeões da Libertadores')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Maiores artilheiros':
        figg = px.bar(df4, x='Artilheiros', y='Gols', title='Top 5 maiores artilheiros da Libertadores')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Maiores artilheiros brasileiros':
        figg = px.bar(df5, x='Artilheiros brasileiros', y='Gols', title=' Top 5 maiores artilheiros brasileiros '
                                                                        'da Libertadores')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Maiores artilheiros brasileiros em atividade':
        figg = px.bar(df6, x='Artilheiros brasileiros que ainda estão em atividade', y='Gols',
                      title='Top 5 maiores artilheiros brasileiros que ainda estão em atividade')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Maiores artilheiros em uma única edição':
        figg = px.bar(df10, x='Jogadores', y='Gols', title='Top 5 maiores artilheiros da Libertadores em uma'
                                                           ' única edição')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Clubes com mais participações':
        figg = px.bar(df11, x='Times', y='Participações', title='Top 5 clubes com mais participações na'
                                                                ' Libertadores')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Clubes brasileiros com mais participações':
        figg = px.bar(df12, x='Times', y='Participações', title='Top 5 clubes brasileiros com mais participações'
                                                                ' na Libertadores')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Clubes que mais vezes disputaram a final':
        figg = px.bar(df13, x='Times', y='Finais', title='Top 5 times com mais finais')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Clubes com mais vitórias':
        figg = px.bar(df14, x='Times', y='Vitórias', title='Top 5 times com mais vitórias na Libertadores *')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Técnicos com mais vitórias':
        figg = px.bar(df15, x='Técnicos', y='Vitórias', title='Top 5 técnicos com mais vitórias na Libertadores')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Técnicos brasileiros com mais vitórias':
        figg = px.bar(df16, x='Técnicos', y='Vitórias',
                      title='Top 5 técnicos brasileiros com mais vitórias na Libertadores')
        figg.update_traces(marker_color='orange')
        return figg
    elif value == 'Clubes com mais gols em uma única edição':
        figg = px.bar(df21, x='Times', y='Gols', title='Top 5 times com mais gols em uma única edição de Libertadores')
        figg.update_traces(marker_color='orange')
        return figg


@app.callback(
    Output('info', 'children'),
    Input('opcoes_graficos', 'value')
)
def update_text(value):
    if value == 'Títulos por país':
        return 'Este gráfico mostra a quantidade de títulos conquistados por países participantes.'
    elif value == 'Maiores campeões':
        return 'Este gráfico mostra os maiores campeões da Libertadores.'
    elif value == 'Maiores artilheiros':
        return 'Este gráfico mostra os maiores artilheiros da história da Libertadores.'
    elif value == 'Maiores artilheiros brasileiros':
        return 'Este gráfico mostra os maiores artilheiros brasileiros da história da Libertadores.'
    elif value == 'Maiores artilheiros brasileiros em atividade':
        return 'Este gráfico mostra os maiores artilheiros brasileiros da história da Libertadores que ainda estão em' \
               ' atividade.'
    elif value == 'Maiores artilheiros em uma única edição':
        return 'Este gráfico mostra os maiores artilheiros em uma única edição da Libertadores.'
    elif value == 'Clubes com mais participações':
        return 'Este gráfico mostra os clubes com mais participações na história da Libertadores.'
    elif value == 'Clubes brasileiros com mais participações':
        return 'Este gráfico mostra os clubes brasileiros com mais participações na história da Libertadores.'
    elif value == 'Clubes que mais vezes disputaram a final':
        return 'Este gráfico mostra os clubes que mais participaram das finais da Libertadores.'
    elif value == 'Clubes com mais vitórias':
        return 'Este gráfico mostra os clubes com mais vitórias na história da Libertadores *(dados atualizados no ' \
               'dia 18/08/2021).'
    elif value == 'Técnicos com mais vitórias':
        return 'Este gráfico mostra os treinadores com mais vitórias na história da Libertadores.'
    elif value == 'Técnicos brasileiros com mais vitórias':
        return 'Este gráfico mostra os treinadores brasileiros com mais vitórias na história da Libertadores.'
    elif value == 'Clubes com mais gols em uma única edição':
        return 'Este gráfico mostra os times com mais gols em uma única edição da Libertadores.'


@app.callback(
    Output('grafico_percentual', 'figure'),
    Input('opcoes_percentual', 'value')
)
def update_percentual(value):
    if value == 'Títulos por país':
        return px.pie(df2, values='Títulos', names='Países', title='Títulos conquistados por país '
                                                                   '(em percentual)')
    elif value == 'Todos os campeões':
        return px.pie(df3_1, values='Títulos', names='Times', title='Todos os campeões (em percentual)')
    elif value == 'Últimos 10 campeões (por time)':
        return px.pie(df7, values='Títulos', names='Times', title='Últimos 10 times campeões '
                                                                  '(em percentual)')
    elif value == 'Últimos 10 campeões (por país)':
        return px.pie(df8, values='Títulos', names='País', title='Últimos 10 países campeões '
                                                                 '(em percentual)')
    elif value == 'Finais disputadas por país':
        return px.pie(df9, values='Finais', names='Países', title='Quantidade de vezes em que os países '
                                                                  'foram finalistas (em percentual)')
    elif value == 'Campeões (por time) no século XXI':
        return px.pie(df17, values='Títulos', names='Times', title='Clubes campeões no século XXI (em percentual')
    elif value == 'Campeões (por país) no século XXI':
        return px.pie(df18, values='Títulos', names='Países', title='Países campeões no século XXI (em percentual')
    elif value == 'Tipos de decisões':
        return px.pie(df19, values='Quantidade', names='Tipos de decisões', title='Maneira quais os campeões '
                                                                                  'foram '
                                                                                  'definidos (em percentual)')
    elif value == 'Finais entre países':
        return px.pie(df20, values='Quantidade de vezes', names='Finais', title='Finais entre países (em percentual)')


@app.callback(
    Output('info_percentual', 'children'),
    Input('opcoes_percentual', 'value')
)
def update_text_percentual(value):
    if value == 'Títulos por país':
        return 'Este gráfico mostra o percentual de títulos conquistados por países participantes.'
    elif value == 'Maiores campeões':
        return 'Este gráfico mostra o percentual de títulos conquistados por times participantes.'
    elif value == 'Últimos 10 campeões (por time)':
        return 'Este gráfico mostra o percentual de títulos conquistados por times participantes nas últimas dez' \
               ' edições.'
    elif value == 'Últimos 10 campeões (por país)':
        return 'Este gráfico mostra o percentual de títulos conquistados por países participantes nas últimas dez' \
               ' edições.'
    elif value == 'Finais disputadas por país':
        return 'Este gráfico mostra o percentual de finais por países participantes.'
    elif value == 'Campeões (por time) no século XXI':
        return 'Este gráfico mostra o percentual de títulos conquistados por times participantes no século XXI.'
    elif value == 'Campeões (por país) no século XXI':
        return 'Este gráfico mostra o percentual de títulos conquistados por países participantes no século XXI.'
    elif value == 'Tipos de decisões':
        return 'Este gráfico mostra o percentual das maneiras de como o título foi definido.'
    elif value == 'Finais entre países':
        return 'Este gráfico mostra o percentual entre finais disputadas entre times de mesmo país ou não.'


if __name__ == '__main__':
    app.run_server(debug=True)
