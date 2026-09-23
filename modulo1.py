# -*- coding: utf-8 -*-

class ModuloFiltros:
    def __init__(self):
        print("[INFO] Módulo de Filtros de Segurança carregado.")

    def validar_filtro(self, sinal):
        # Aqui você pode adicionar regras como: 
        # "Só operar se a confiança for > 80%"
        if sinal.get('confianca', 0) > 70:
            return True
        return False