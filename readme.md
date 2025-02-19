# OneDrive AI File Search

## 📌 Overview
OneDrive AI File Search is a Streamlit-powered web application that leverages LLM-based search capabilities to help users find relevant files, images, and documents in their OneDrive storage. The app integrates with Microsoft OneDrive API and utilizes Ollama with Qwen (or DeepSeek) to enhance search accuracy.

## 🚀 Features
- **🔑 Secure Login**: Authenticate with your Microsoft account to access OneDrive.
- **💡 AI-powered Search**: Generate intelligent search queries using LLMs (Qwen, DeepSeek).
- **📂 File Retrieval**: Fetch and display relevant files based on search prompts.
- **🕒 Search History**: Maintain a history of past searches for easy reference.
- **🎨 Enhanced UI**: Styled interface with visually appealing elements.
- **📊 Duplicate File Management (Upcoming)**: Periodically detect and suggest duplicate file removal.

## 🛠️ Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip
- Streamlit
- Microsoft Authentication Library (MSAL)
- Requests
- Ollama

### Setup Steps
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-repo/onedrive-llm-search.git
   cd onedrive-llm-search
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables:**
   - Update `CLIENT_ID`, `TENANT_ID`, and `REDIRECT_URI` in the script.
4. **Run the App:**
   ```sh
   streamlit run app.py
   ```

## 🔑 Authentication
- The app uses Microsoft OAuth for authentication.
- Upon login, an access token is obtained and used to query OneDrive.

## 📖 Usage
1. **Login to OneDrive** using your Microsoft credentials.
2. **Enter a Search Prompt**, e.g., "Find my invoices from last month."
3. **AI Generates a Search Query** using Qwen/DeepSeek.
4. **Retrieve Files** matching the query from OneDrive.
5. **View Search History** for easy access to past queries and results.

## 🏗️ Future Enhancements
- **Duplicate File Detection**: AI-based duplicate file removal suggestions.
- **Advanced Filtering**: Search by file type, date range, and metadata.
- **Batch Actions**: Bulk delete, move, or archive files.

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a Pull Request

## 📜 License
This project is licensed under the MIT License.

## 📬 Contact
For issues or support, reach out to **your-email@example.com** or open an issue on GitHub.

---
Made with ❤️ using Streamlit & Ollama 🚀

