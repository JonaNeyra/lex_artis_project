from resources.protos.extractnomfromurlpb import extractnomfromurlpb_pb2 as proto_extract_nom
from resources.protos.extractnomfromurlpb import extractnomfromurlpb_pb2_grpc as grpc_proto_extract_nom

from ..app.extract_num_usecase import ExtractNomUseCase
from ..infrastructure.html_parser import HtmlParser


class LegalNorm(grpc_proto_extract_nom.ExtractNomService):
    """GRPC Service"""

    def ExtractNom(self, request, context, **kwargs):
        """
        :param request:
        :param context:
        :param kwargs:
        :return:
        """
        print(request.nom_name)
        print(request.nom_url)

        html_parser = HtmlParser(request.nom_url)
        use_case = ExtractNomUseCase(html_parser)
        legal_norm = use_case.execute()
        print(f"{request.nom_name}")

        proto_articles = [
            proto_extract_nom.Article(
                name=article.name,
                description=article.description,
            )
            for article in legal_norm.articles
        ]

        new_norm = proto_extract_nom.LegalNorm(
            name=legal_norm.name,
            description=legal_norm.description,
            jurisdiction=legal_norm.jurisdiction,
            procedure_types=legal_norm.procedure_types,
            articles=proto_articles,
            effective_date=legal_norm.effective_date,
        )

        return proto_extract_nom.ExtractNomResponse(
            legal_norm=new_norm,
        )
