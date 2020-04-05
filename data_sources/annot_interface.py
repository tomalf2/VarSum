from typing import Optional, List, Union
from sqlalchemy.engine import Connection
from sqlalchemy.sql.expression import FromClause
from data_sources.io_parameters import *


class AnnotInterface:

    # MAP ATTRIBUTE NAMES TO TABLE COLUMN NAMES
    col_map: dict = {}

    def annotate(self, connection: Connection, genomic_interval: GenomicInterval,
                 attrs: Optional[List[Vocabulary]]) -> FromClause:
        raise NotImplementedError('Any subclass of AnnotInterface must implement the abstract method "annotate"')

    def find_gene_region(self, connection: Connection, gene_name: str, gene_type: Optional[str],
                         gene_id: Optional[str], output_attrs: List[Vocabulary]) -> FromClause:
        raise NotImplementedError('Any subclass of AnnotInterface must implement the abstract method "find_gene_region"')

    @classmethod
    def get_available_annotation_types(cls):
        if len(cls.col_map) == 0:
            raise NotImplementedError('Source concrete implementations need to override class '
                                      'dictionary "col_map"')
        return cls.col_map.keys()
