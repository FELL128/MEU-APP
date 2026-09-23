# -*- coding: utf-8 -*-

import time
import random

class NetworkManager:
    def __init__(self, logger):
        self.logger = logger
        self.connected = False

    def connect(self):
        self.logger.info("[REDE] Estabelecendo conexão com o servidor...")
        time.sleep(1)
        self.connected = True
        self.logger.info("[REDE] Conexão estabelecida com sucesso.")
        return True

    def disconnect(self):
        self.connected = False
        self.logger.info("[REDE] Conexão encerrada.")

    def check_connection(self):
        return self.connected