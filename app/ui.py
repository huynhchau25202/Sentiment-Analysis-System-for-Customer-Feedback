import streamlit as st
import pandas as pd
from app.utils import load_model, predict_sentiment
import torch

# Tải mô hình và tokenizer
tokenizer, model = load_model()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

def app_ui():
    st.title("📊 Sentiment Analysis for Customer Feedback")

    option = st.radio("Chọn cách nhập dữ liệu:", ("Nhập phản hồi", "Tải lên file Excel"))

    if option == "Nhập phản hồi":
        user_input = st.text_area("Nhập phản hồi của khách hàng tại đây:", height=150)
        if st.button("Phân tích cảm xúc"):
            if user_input.strip() == "":
                st.warning("Vui lòng nhập nội dung phản hồi.")
            else:
                sentiment = predict_sentiment(user_input, tokenizer, model, device)
                st.success(f"Kết quả phân tích cảm xúc: **{sentiment}**")

    else:
        uploaded_file = st.file_uploader("Tải lên file Excel (.xlsx) chứa cột phản hồi", type=["xlsx"])
        if uploaded_file:
            try:
                df = pd.read_excel(uploaded_file)
                st.write("📄 File đã tải lên:")
                st.dataframe(df)  # ✅ Hiện toàn bộ cột gốc (user, app, content...)

                if "content" not in df.columns:
                    st.error("⚠️ File cần có cột tên là 'content' chứa phản hồi văn bản.")
                else:
                    if st.button("Phân tích cảm xúc"):
                        with st.spinner("Đang phân tích cảm xúc..."):
                            df["sentiment"] = df["content"].astype(str).apply(
                                lambda x: predict_sentiment(x, tokenizer, model, device)
                            )

                        st.success("✅ Phân tích xong!")
                        st.dataframe(df)  # ✅ Hiện đầy đủ các cột sau khi thêm sentiment

                        # Tải kết quả về
                        output_excel = "sentiment_results.xlsx"
                        df.to_excel(output_excel, index=False)
                        with open(output_excel, "rb") as f:
                            st.download_button(
                                label="📥 Tải kết quả về",
                                data=f,
                                file_name="/output/sentiment_results.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )
            except Exception as e:
                st.error(f"❌ Lỗi khi xử lý file: {e}")
