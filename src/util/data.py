from datetime import date


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        data_str = ''
        if self.dia < 10:
            data_str = '0' + str(self.dia)
        else:
            data_str = str(self.dia)
        if self.mes < 10:
            data_str += "/0" + str(self.mes)
        else:
            data_str += "/" + str(self.mes)
        data_str += "/" + str(self.ano)
        return data_str

    def calcular_idade(self, data_referencia=None):
        if data_referencia is None:
            dia_atual_str, mes_atual_str, ano_atual_str = date.today().strftime("%d/%m/%Y").split('/')
            dia_referencia, mes_referencia, ano_referencia = int(dia_atual_str), int(mes_atual_str), int(ano_atual_str)
        else:
            dia_referencia, mes_referencia, ano_referencia = data_referencia.dia, data_referencia.mes, data_referencia.ano

        idade = ano_referencia - self.ano

        if mes_referencia < self.mes or (mes_referencia == self.mes and dia_referencia < self.dia):
            idade -= 1

        return idade