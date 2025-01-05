from .document import Document, DocumentDBBase, User_Ad, AdDBBaese

beanie_models = [DocumentDBBase, AdDBBaese]

__all__ = [
    "beanie_models",
    "Document",
    "User_Ad"


]
