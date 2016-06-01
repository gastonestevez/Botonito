class Juego(object):
    queryDePreguntasSeleccionadas = None
    preguntasTotales = 0

    @classmethod
    def ingresarQueryDePreguntas(self, listado):
        self.queryDePreguntasSeleccionadas = listado

    @classmethod
    def getQueryDePreguntasSeleccionadas(self):
        return self.queryDePreguntasSeleccionadas

    @classmethod
    def getPreguntasTotales(self):
        return self.preguntasTotales

    @classmethod
    def setPreguntasTotales(self,total):
        self.preguntasTotales = total