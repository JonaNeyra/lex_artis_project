from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Article(_message.Message):
    __slots__ = ["description", "name"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    description: str
    name: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ExtractNomRequest(_message.Message):
    __slots__ = ["nom_name", "nom_url"]
    NOM_NAME_FIELD_NUMBER: _ClassVar[int]
    NOM_URL_FIELD_NUMBER: _ClassVar[int]
    nom_name: str
    nom_url: str
    def __init__(self, nom_name: _Optional[str] = ..., nom_url: _Optional[str] = ...) -> None: ...

class ExtractNomResponse(_message.Message):
    __slots__ = ["legal_norm"]
    LEGAL_NORM_FIELD_NUMBER: _ClassVar[int]
    legal_norm: LegalNorm
    def __init__(self, legal_norm: _Optional[_Union[LegalNorm, _Mapping]] = ...) -> None: ...

class LegalNorm(_message.Message):
    __slots__ = ["articles", "description", "effective_date", "jurisdiction", "name", "procedure_types"]
    ARTICLES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    JURISDICTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_TYPES_FIELD_NUMBER: _ClassVar[int]
    articles: _containers.RepeatedCompositeFieldContainer[Article]
    description: str
    effective_date: str
    jurisdiction: str
    name: str
    procedure_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., jurisdiction: _Optional[str] = ..., procedure_types: _Optional[_Iterable[str]] = ..., articles: _Optional[_Iterable[_Union[Article, _Mapping]]] = ..., effective_date: _Optional[str] = ...) -> None: ...
