from jina import Executor, DocumentArray, requests
from typing import Any, Dict


class TagsCopier(Executor):
    def __init__(
        self,
        traversal_paths: str = "@r",
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.traversal_paths = traversal_paths

    @requests
    def copy_tags(self, docs: DocumentArray, parameters: Dict[str, Any], **kwargs):
        traversal_paths = parameters.get("traversal_paths", self.traversal_paths)

        for doc in docs[self.traversal_paths]:
            for chunk in doc.chunks[...]:
                chunk.tags.update(doc.tags)
