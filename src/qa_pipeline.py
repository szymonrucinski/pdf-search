# In-Memory Document Store
from functools import cached_property
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import TfidfRetriever, FARMReader, EmbeddingRetriever
from haystack.pipelines import ExtractiveQAPipeline


def build_document_store(docs):
    document_store = InMemoryDocumentStore(progress_bar=True)
    document_store.write_documents(docs)
    document_store.get_all_documents()
    return document_store


def build_retriever(document_store):
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1",
        model_format="sentence_transformers",
    )
    document_store.update_embeddings(retriever)

    return retriever


def build_reader():
    # Load a  local model or any of the QA models on
    # Hugging Face's model hub (https://huggingface.co/models)
    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)

    return reader


def build_pipeline(book):
    # Extractive Pipeliline
    document_store = build_document_store(book)
    retriever = build_retriever(document_store)
    reader = build_reader()
    pipeline = ExtractiveQAPipeline(reader, retriever)

    return pipeline


def query(query, pipeline):
    print("Querying...")
    prediction = pipeline.run(
        query, params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 3}}
    )
    return prediction
