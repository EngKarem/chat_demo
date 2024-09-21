from llama_index.core import load_index_from_storage, StorageContext
from llama_index.core.tools import QueryEngineTool, ToolMetadata

#### This function create a tool to answer a question about the given topic
#### For each topic create a tool like this and pass where you stored the indcies for it

indices_path = 'Non_profit_organizations_indices'  ### where index stored from tools.py file check it you will find the same path


def create_tool(indices_path=indices_path):
    storagecontent = StorageContext.from_defaults(persist_dir=indices_path)

    index = load_index_from_storage(storage_context=storagecontent)

    pdf_tool = QueryEngineTool(
        index.as_query_engine(),
        metadata=ToolMetadata(
            name="Non_profit_organizations",  # don't include speaces in tool name use _ or like i did with the name
            description="Contains information about non-profit organizations, including knowledge management, organizational design for learning and innovation, challenges in the non-profit sector, and strategies for implementing knowledge management. Covers topics such as knowledge for impact, knowledge-ready organizations, and roadmaps for adopting knowledge management practices."
            # description="Contain general information about Non-profit organizations"
            # this discription is critical should be carfull when make it
        )
    )

    return pdf_tool
