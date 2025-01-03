from ..services.nom_processor import NomProcessor


class ExtractNomUseCase:
    """Caso de uso para Extraer información de NOMs"""

    def __init__(self, html_parser):
        self.processor = NomProcessor(html_parser)

    def execute(self):
        """
        :return:
        """
        return self.processor.process_nom()
