import torch  # Thêm dòng này để import thư viện torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# Đường dẫn đến mô hình và tokenizer
TOKENIZER_PATH = 'app/model/bert_tokenizer'
MODEL_PATH = 'app/model/sentiment_model'

def load_model():
    # Tải tokenizer và model từ các thư mục lưu mô hình
    tokenizer = DistilBertTokenizerFast.from_pretrained(TOKENIZER_PATH)
    model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
    return tokenizer, model

# Hàm phân tích cảm xúc
def predict_sentiment(text, tokenizer, model, device):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    label_map = {0: "Negative 😠", 1: "Neutral 😐", 2: "Positive 😊"}
    return label_map[predicted_class]
