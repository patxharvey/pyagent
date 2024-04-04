import os
import pandas as pd
from dotenv import load_dotenv
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

# define builder functions
def load_datasets_from_folder(data_folder):
    """
    Scan specified folder for CSV files and return a list of file paths.
    """
    dataset_paths = [os.path.join(data_folder, f) for f in os.listdir(data_folder) \
                     if f.endswith('.csv')]
    return dataset_paths


def create_query_engine_for_datasets(file_path, instruction_str):
    """
    Load a dataset from a given file path and create a PandasQueryEngine for it.
    """
    import pandas as pd
    df = pd.read_csv(file_path)
    engine_name = os.path.splitext(os.path.basename(file_path))[0].replace(' ', '_')
    query_engine = PandasQueryEngine(df=df, verbose=True, instruction_str=instruction_str)
    # Assuming 'new_prompt' is a generic prompt applicable for any dataset
    query_engine.update_prompts({"pandas_prompt": new_prompt})
    return query_engine, engine_name

def build_tools_from_datasets(data_folder, instruction_str):
    """
    Build query engines and tools for all datasets in the specified folder.
    """

    import pandas as pd
    tools = [note_engine]  # Assuming 'note_engine' is predefined
    dataset_paths = load_datasets_from_folder(data_folder)
    
    for path in dataset_paths:
        query_engine, name = create_query_engine_for_datasets(path, instruction_str)
        tools.append(
            QueryEngineTool(
                query_engine=query_engine,
                metadata=ToolMetadata(
                    name=f"{name}_data",
                    description=f"Information from the {name} dataset"
                ),
            )
        )
    return tools

# Main script
load_dotenv()

# Load and build tools dynamically from the data folder
data_folder = "data"
tools = build_tools_from_datasets(data_folder, instruction_str)

# Initialize the agent with the dynamically built tools
llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

# Example interactive loop
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)