class LegalNorm:
    """Modelo para las NOMs"""

    def __init__(self, name, description, jurisdiction, procedure_types, articles, effective_date):
        """
        :param name:
        :param description:
        :param jurisdiction:
        :param procedure_types:
        :param articles:
        :param effective_date:
        """
        self.name = name
        self.description = description
        self.jurisdiction = jurisdiction
        self.procedure_types = procedure_types
        self.articles = articles
        self.effective_date = effective_date
