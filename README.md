# Sentiment Analysis System for Customer Feedback

This project is a **Sentiment Analysis System** that uses a fine-tuned **DistilBERT** model to classify customer feedback into sentiment categories (positive, neutral, negative). The system is built with **Streamlit** for an interactive user interface.

## Features

- **Sentiment Analysis**: Analyze customer feedback and classify it into sentiment categories.
- **Batch Processing**: Upload an Excel file with multiple feedback entries for batch analysis.
- **Interactive UI**: Built with Streamlit for ease of use.
- **Pre-trained Model**: Uses a fine-tuned DistilBERT model for high accuracy.

## Project Structure

```
sentiment-analysis-app/
├── LICENSE                        # License file
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── sentiment_analysis_app.py      # Main Streamlit app
├── app/
│   ├── __init__.py                # App initialization
│   ├── ui.py                      # Streamlit UI components
│   ├── utils.py                   # Utility functions for model loading and prediction
│   └── model/
│       ├── bert_tokenizer/        # Pre-trained tokenizer
│       └── sentiment_model/       # Fine-tuned DistilBERT model
├── data/
│   └── file_excel_test.xlsx       # Sample input data
└── output/
    └── sentiment_results.xlsx     # Output results
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/huynhchau25202/Sentiment-Analysis-System-for-Customer-Feedback.git
   cd Sentiment-Analysis-System-for-Customer-Feedback
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Git LFS (if not already installed):
   ```bash
   sudo apt install git-lfs
   git lfs install
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run sentiment_analysis_app.py
   ```

2. Use the web interface to:
   - Enter customer feedback for sentiment analysis.
   - Upload an Excel file for batch processing.

3. View the results directly in the app or download them as an Excel file.

## Model Details

- **Model**: Fine-tuned DistilBERT
- **Tokenizer**: Pre-trained BERT tokenizer
- **Training Data**: Customer feedback labeled with sentiment categories.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)