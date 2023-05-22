from abc import ABC, abstractmethod
from typing import List, Sequence, Optional, Tuple, Any
from uuid import UUID
import numpy.typing as npt
from chromadb.api.types import (
    Embeddings,
    Documents,
    IDs,
    Metadatas,
    Metadata,
    Where,
    WhereDocument,
)


class DB(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_collection(
        self,
        name: str,
        metadata: Optional[Metadata] = None,
        get_or_create: bool = False,
    ) -> Sequence[Sequence[Any]]:
        pass

    @abstractmethod
    def get_collection(self, name: str) -> Sequence[Sequence[Any]]:
        pass

    @abstractmethod
    def list_collections(self) -> Sequence[Sequence[Any]]:
        pass

    @abstractmethod
    def update_collection(
        self,
        id: UUID,
        new_name: Optional[str] = None,
        new_metadata: Optional[Metadata] = None,
    ) -> None:
        pass

    @abstractmethod
    def delete_collection(self, name: str) -> None:
        pass

    @abstractmethod
    def get_collection_uuid_from_name(self, collection_name: str) -> UUID:
        pass

    @abstractmethod
    def add(
        self,
        collection_uuid: UUID,
        embeddings: Embeddings,
        metadatas: Optional[Metadatas],
        documents: Optional[Documents],
        ids: List[str],
    ) -> List[UUID]:
        pass

    @abstractmethod
    def add_incremental(
        self, collection_uuid: UUID, ids: List[UUID], embeddings: Embeddings
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        where: Where = {},
        collection_name: Optional[str] = None,
        collection_uuid: Optional[UUID] = None,
        ids: Optional[IDs] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        where_document: WhereDocument = {},
        columns: Optional[List[str]] = None,
    ) -> Sequence[Any]:
        pass

    @abstractmethod
    def update(
        self,
        collection_uuid: UUID,
        ids: IDs,
        embeddings: Optional[Embeddings] = None,
        metadatas: Optional[Metadatas] = None,
        documents: Optional[Documents] = None,
    ) -> bool:
        pass

    @abstractmethod
    def count(self, collection_id: UUID) -> int:
        pass

    @abstractmethod
    def delete(
        self,
        where: Where = {},
        collection_uuid: Optional[UUID] = None,
        ids: Optional[IDs] = None,
        where_document: WhereDocument = {},
    ) -> List[str]:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def get_nearest_neighbors(
        self,
        collection_uuid: UUID,
        where: Where = {},
        embeddings: Optional[Embeddings] = None,
        n_results: int = 10,
        where_document: WhereDocument = {},
    ) -> Tuple[List[List[UUID]], npt.NDArray]:
        pass

    @abstractmethod
    def get_by_ids(
        self, uuids: List[UUID], columns: Optional[List[str]] = None
    ) -> Sequence[Any]:
        pass

    @abstractmethod
    def raw_sql(self, raw_sql):  # type: ignore
        pass

    @abstractmethod
    def persist(self) -> None:
        pass
