import folium
import os
import json

class App():
    def __init__(self):
        self.dap = int()
        self.pi = float()
        self.lat = float()
        self.long = float()
        self.mapa = folium.Map()
        self.dados = dict()
        self.identificador = str()
        self.color = 'blue'
        self.familia = str()
        self.especie = str()
        self.altura = int()
    
    def gerarMapa(self):
        self.nome = input('Digite o nome desse mapa: ')
        self.mapa = folium.Map(
            min_zoom= 3,
            world_copy_jump = True,
            control_scale= True,
            width= '100%' ,
            height= '100%'
            )

    def lerJson(self):
        pass

    def gravarArquivoJson(self):
        pass
    
    def marcarMapa(self):
        self.lat = input('Latitude: ')
        self.long = input('Longitude: ')
        self.dap = int(input('DAP(cm): '))
        self.altura = int(input('Altura(cm): '))
        self.familia = input('Familia: ')
        self.especie = input('Espécie: ')
        print("Identificador: ",end='')
        folium.CircleMarker(
            [self.lat,self.long],
            radius= 1,
            tooltip = f'<b>{input()}</b>',
            popup = (
                    f'<b>DAP:</b> <i>{self.dap/100}m</i>\n'
                    f'<b>Altura:</b> <i>{self.altura/100}m</i>\n'
                    f'<b>Familia:</b> <i>{self.familia}</i>\n'
                    f'<b>Espécia:</b> <i>{self.especie}</i>'
                    )
        ).add_to(self.mapa)

    def salvarMapa(self):
        self.mapa.save(f'{self.nome}.html')

    def abrirMapa(self):
        self.mapa

    def renomearMapa(self):
        self.nome = input("\nDigite o novo nome desse mapa: ")

    def opcoes(self):
        resposta = int(input(
            'Digite:'
            '\n<1> para adicionar um novo marcador\n'
            '<2> para salvar mapa\n'
            '<3> para abrir mapa\n'
            '<4> para renomear mapa\n'
            '<5> para sair\n'
            ))
        return resposta

    def run(self):
        self.gerarMapa()
        while True:
            escolha = self.opcoes()
            if escolha == 1:
                self.marcarMapa()
                print('\nMarcador adicionado com sucesso\n')
            if escolha == 2:
                self.salvarMapa()
                print('\nMapa salvo com sucesso\n')
            if escolha == 3:
                self.abrirMapa()
            if escolha == 4:
                self.renomearMapa()
                print('\nMapa renomeado com sucesso\n')
            if escolha == 5:
                return