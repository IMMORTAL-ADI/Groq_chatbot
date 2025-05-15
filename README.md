# CodeCopilot: AI Coding Assistant

CodeCopilot is a Streamlit-based chatbot that leverages the Groq API to provide intelligent coding assistance. It can answer programming questions, generate code snippets, explain concepts, debug code, and more.

## Features
- Interactive chat interface for coding help
- Supports Python, JavaScript, C++, Java, SQL, and more
- Provides code explanations, best practices, and debugging tips
- Chat history displayed in the sidebar
- Easy reset/clear chat functionality

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your environment variables**:
   - Create a `.env` file in the project root with your Groq API key:
     ```env
     groq_api_key="YOUR_GROQ_API_KEY"
     ```
4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## Usage
- Type your programming question or request in the chat input box.
- View the conversation and responses in the main area.
- See the chat history in the sidebar.
- Use the "Clear Chat" button to reset the conversation.

## Security
- The `.env` file is included in `.gitignore` and should not be committed to version control.

## License
This project is for educational and personal use.
