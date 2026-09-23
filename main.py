# -*- coding: utf-8 -*-

import logging
import time
from config import ATIVO_PADRAO
from engine import TradingEngine
from network import NetworkManager

# Configuração de Logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class AutomationOrchestrator:
    def __init__(self):
        self.logger = logging.getLogger("Orchestrator")
        self.logger.info("--- Inicializando Sistema de Automação ---")
        
        self.network_manager = NetworkManager(self.logger)
        self.engine = TradingEngine(self.logger)
        self.is_running = True

    def run(self):
        # Passo 1: Conectar à Rede
        if not self.network_manager.connect():
            self.logger.error("Falha ao conectar. Encerrando.")
            return

        # Passo 2: Iniciar o Motor
        self.engine.start()
        
        self.logger.info(f"=== SISTEMA ATIVO: {ATIVO_PADRAO} ===")
        
        try:
            # Loop principal de operação
            while self.is_running:
                self.logger.info("[SISTEMA] Iniciando novo ciclo de análise...")
                
                sinal = self.engine.executar_ciclo()
                
                if sinal:
                    self.logger.info(f"🚀 SINAL ENCONTRADO: {sinal['direcao']}")
                    self.logger.info(f"📊 Detalhes: {sinal['detalhes']} | Confiança: {sinal['confianca']}%")
                else:
                    self.logger.info("[SISTEMA] Aguardando sinal seguro...")

                time.sleep(5) # Tempo entre uma análise e outra
                
        except KeyboardInterrupt:
            self.logger.info("\n[SISTEMA] Interrompido pelo usuário.")
        finally:
            self.shutdown()

    def shutdown(self):
        self.is_running = False
        self.logger.info("[SISTEMA] Encerrando módulos...")
        self.engine.stop()
        self.network_manager.disconnect()
        self.logger.info("[SISTEMA] Sistema Offline.")

if __name__ == "__main__":
    bot = AutomationOrchestrator()
    bot.run()