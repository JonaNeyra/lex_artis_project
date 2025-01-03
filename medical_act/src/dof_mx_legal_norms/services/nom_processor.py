from ..domain.entities import LegalNorm
from ..domain.value_objects import Article


class NomProcessor:
    """
    Clase encargada de procesar el contenido HTML para extraer información
    relevante sobre normas oficiales mexicanas (NOM).
    """

    def __init__(self, html_parser):
        self.html_parser = html_parser
        self.soup = None

    def process_nom(self):
        """
        Procesa el contenido HTML y devuelve un objeto de tipo LegalNorm.

        :return: Instancia de LegalNorm.
        """
        self.soup = self.html_parser.parse()
        title, description = self.nom_label()
        procedure_types = self.nom_procedure_types(description)
        publication_date = self.nom_publication_date()
        articles = self.nom_references()

        return LegalNorm(
            name=title,
            description=description,
            jurisdiction="México",
            procedure_types=procedure_types,
            articles=articles,
            effective_date=publication_date,
        )

    def nom_label(self):
        """
        Extrae el título y descripción de la NOM.

        :return: Título y descripción de la NOM.
        """
        title = ''
        nom_title = self.soup.find('h1', class_='Titulo_1')
        if nom_title:
            title = nom_title.get_text(strip=False).strip()
        split_title = title.split(',')
        nom_description = title[len(split_title[0]) + 1:].strip()
        title = split_title[0]
        return title, nom_description

    def nom_procedure_types(self, nom_description):
        """
        Determina los tipos de procedimientos asociados a la descripción de la NOM.

        :param nom_description: Descripción de la NOM.
        :return: Lista de tipos de procedimientos.
        """
        procedure_types = []
        keywords = {
            "hospital": "Hospitalaria",
            "quirúrgic": "Quirúrgica",
            "estétic": "Estética",
            "diagnóstic": "Diagnóstica",
            "especial": "Especializada",
            "ambula": "Ambulatoria",
            "urgent": "Urgencias",
            "reconstruc": "Reconstructiva",
            "prevent": "Preventiva",
            "rehabilit": "Rehabilitación",
        }
        for keyword, procedure_type in keywords.items():
            if keyword in nom_description.lower():
                procedure_types.append(procedure_type)
        if not procedure_types:
            procedure_types = ["General"]
        return procedure_types

    def nom_publication_date(self):
        """
        Extrae la fecha de publicación de la NOM.

        :return: Fecha de publicación como cadena de texto.
        """
        date_tag = self.soup.find('b')
        publication_date = (
            date_tag.get_text(strip=True).replace('DOF:', '').strip() if date_tag else None
        )
        return publication_date

    def nom_references(self):
        """
        Extrae los artículos referenciados en la NOM.

        :return: Lista de objetos Article.
        """
        articles = []
        for div in self.soup.find_all('div', class_='Texto'):
            content = div.get_text(strip=False)
            refer_prefix = 'Norma Oficial Mexicana NOM'
            if refer_prefix in content:
                partial_content = content.split(refer_prefix)
                content = refer_prefix + partial_content[1]
                name = content.split(',')[0]
                description = self.article_nom_description(content, name)
                name = self.article_nom_name(name)
                articles.append(Article(name=name, description=description))
        return articles

    def article_nom_name(self, name):
        """
        Limpia y procesa el nombre de un artículo referenciado.

        :param name: Nombre del artículo.
        :return: Nombre procesado.
        """
        name = name.replace('Norma Oficial Mexicana ', '')
        name = name.replace('NORMA Oficial Mexicana ', '')
        name = name.split()
        return ''.join(name)

    def article_nom_description(self, content, name):
        """
        Limpia y procesa la descripción de un artículo referenciado.

        :param content: Contenido del artículo.
        :param name: Nombre del artículo.
        :return: Descripción procesada.
        """
        description = content[len(name) + 1:].strip()
        description = description.replace('-', ' - ')
        description = description.split()
        return ' '.join(description)
