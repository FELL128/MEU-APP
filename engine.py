# -*- coding: utf-8 -*-

from intelligence import BotIntelligence
from modulo1 import ModuloFiltros

class TradingEngine:
    def __init__(self, logger):
        self.logger = logger
        self.ai = BotIntelligence()
        self.filtro = ModuloFiltros()
        self.is_running = False

    def start(self):
        self.is_running = True
        self.logger.info("[MOTOR] Motor de trading iniciado.")

    def executar_ciclo(self):
        if not self.is_running:
            return None
        
        # 1. Obter sinal da IA
        sinal = self.ai.analisar_mercado()
        
        # 2. Passar pelo filtro de segurança
        if self.filtro.validar_filtro(sinal):
            return sinal
        
        return None

    def stop(self):
        self.is_running = False
        self.logger.info("[MOTOR] Motor de trading parado.")