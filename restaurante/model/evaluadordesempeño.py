class EvaluadorDesempeño:
    def __init__(self):
        pass

    def evaluar_desempeño(self, mesero, criterios):
        horas_trabajadas = mesero.calcular_horas_trabajadas()
        if horas_trabajadas > 40:
            return "Excelente desempeño"
        elif horas_trabajadas > 30:
            return "Buen desempeño"
        else:
            return "Desempeño regular"
