
# PaperQA

**PaperQA** is a Python-based question-answering application for research papers and documents. It uses OpenAI-powered embeddings and FAISS for vector storage to provide accurate answers based on the content of uploaded papers in `.pdf`, `.docx`, and `.txt` formats.

## Features

- **File Support**: Reads and processes `.pdf`, `.docx`, and `.txt` files.
- **Embeddings & Vector Search**: Converts document text to embeddings with OpenAI for similarity-based search.
- **Interactive Q&A**: Provides an interactive prompt for querying the content.
- **Extensible Design**: Modular code structure for ease of expansion and customization.

## Installation

### Prerequisites

- Python 3.7+
- OpenAI API Key
- [FAISS](https://github.com/facebookresearch/faiss)
- [LangChain](https://langchain.com/) and other dependencies in `requirements.txt`

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/PaperQA.git
   cd PaperQA
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Place your documents in the `data` folder.
2. Run the application:

   ```bash
   python main.py
   ```

3. Enter questions related to the content of the papers in the prompt. Type `end` to exit.

## Project Structure

- **`document_reader.py`**: Functions to read `.pdf`, `.docx`, and `.txt` files.
- **`text_processing.py`**: Splits large texts into manageable chunks.
- **`embeddings.py`**: Generates and stores embeddings for document similarity search.
- **`main.py`**: The main application logic, including the interactive prompt.

## Example

After running `main.py`, you can input questions like:

```text
Ask a question about the paper: What are the main conclusions?
```

The model will return a response based on the document content.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
