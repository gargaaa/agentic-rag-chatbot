from utils.document_parser import parse_file
from utils.mcp import create_message

class IngestionAgent:
    def run(self, files, trace_id):
        documents = [parse_file(f) for f in files]
        return create_message(
            sender="IngestionAgent",
            receiver="RetrievalAgent",
            type_="DOCUMENTS_PARSED",
            payload={"docs": documents},
            trace_id=trace_id
        )
