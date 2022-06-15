from datetime import datetime, timedelta


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dias_da_semana = [
            "segunda", "terça", "quarta", "quinta",
            "sexta", "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]