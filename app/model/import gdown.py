import gdown

url = "https://drive.google.com/file/d/1cAYWlmiaSf5-oeQKKdT9phmhYzW266nc/view?usp=sharing"
output = "sentiment_model.zip"
gdown.download(url, output, quiet=False)