from jina import DocumentArray, Document
from executor import TagsCopier

docs = DocumentArray(
    [
        Document(
            text="J.R.R. Tolkien turns to p.3 on www.google.com",
            tags={"foo": "bar"},
            chunks = DocumentArray.empty(3)
        ),
    ]
)

ex = TagsCopier(parameters={})
ex.copy_tags(docs, parameters={})

for doc in docs:
    print(doc.tags)
    for chunk in doc.chunks:
        print(chunk.tags)
