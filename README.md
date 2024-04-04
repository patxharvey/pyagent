# pyAgent: Dynamic Data Query Engine Project with RAG

This project leverages the Retrieval-Augmented Generation (RAG) approach to enhance the capability of language models by dynamically querying structured datasets. It enables the integration of live data from CSV files into the generative responses of a language model, making it ideal for applications requiring up-to-date information or context-specific data retrieval.

Future iterations will include support for .pdf, .docx, .epub file types.

Performs best when data is cleaned beforehand.

## Features

- **Dynamic Dataset Loading**: Automatically scans a specified folder for CSV files and loads them as datasets for querying.
- **Query Engine Integration**: Utilizes the `PandasQueryEngine` for efficient data querying and retrieval based on user prompts.
- **Flexible Tool Support**: Supports the integration of multiple query engines and tools, making it versatile for different data types and sources.
- **RAG Approach**: Enhances response generation by incorporating relevant data retrieved from the datasets into the language model's outputs.

## Getting Started

### Prerequisites

- Python 3.9 or later
- OpenAI API Key

### Installation

1. Clone the repository to your local machine:

   ```
   git clone git@github.com:pxthxrv/pyagent.git
   ```

2. Navigate to the project directory:

    ```
    cd your/path/py-agent
    ```

3. (Optional) Create and activate virtual environment

4. Install the required Python packages:
    
    ```
    pip install -r requirements.txt
    ```

5. Set up your .env file with the necessary environment variables.

### Usage

1. Place your CSV data files into the data folder.

2. Run the main script to start the interactive prompt:

    ```
    python3 main.py
    ```

3. Follow the interactive prompts to enter your queries and receive pandas generated insights from your datasets.

## Contributing

Contributions to improve the project are welcome. Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.