from pydantic import BaseModel, Field
from typing import Dict, Any
import xml.etree.ElementTree as ET

from llms.types import LLMDataFormat
from data_structures.utils import to_string_without_declaration

class ContextualDocument(BaseModel):
    source: str = Field(
        ...,
        description="The filename of the contextual document."
    )

    content: str = Field(
        ...,
        description="The content of the contextual document."
    )

    index: int | None = Field(
        None,
        description="The index of the contextual document."
    )

    def serialize(self, format: LLMDataFormat, context: Dict[str, Any] | None = None) -> str | ET.Element:
        if format == LLMDataFormat.XML:

            if context is None:
                root = ET.Element("document")
            else:
                parent = context["parent"]
                root = ET.SubElement(parent, "document")

            if self.index:
                root.set("index", str(self.index))
            
            # Add source
            source = ET.SubElement(root, "source")
            source.text = self.source

            # Add content
            content = ET.SubElement(root, "document_content")
            content.text = self.content

            if context is None:
                return to_string_without_declaration(root)
            else:
                return root

        else:
            raise ValueError(f"Unsupported format: {format}")

class DocumentsForContext(BaseModel):
    documents: list[ContextualDocument] = Field(
        ...,
        min_length=1,
        description="The list of contextual documents."
    )

    def serialize(self, format: LLMDataFormat) -> str:
        if format == LLMDataFormat.XML:

            root = ET.Element("documents")
            
            for document in self.documents:
                _ = document.serialize(format=format, context={"parent": root})

            return to_string_without_declaration(root)

        else:
            raise ValueError(f"Unsupported format: {format}")
