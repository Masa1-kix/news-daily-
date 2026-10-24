import os
from google import genai
import feedparser

def summarize_news():
    # Gemini APIクライアントの初期化（環境変数からキーを自動取得）
    client = genai.Client()
    
    # NHKニュースのRSSフィード
    rss_url = "https://www.nhk.or.jp/rss/news/cat0.xml"
    feed = feedparser.parse(rss_url)
    
    news_text = ""
    print("本日のニュースを取得中...")
    for entry in feed.entries[:5]: # 上位5件のニュースを取得
        news_text += f"- タイトル: {entry.title}\n  概要: {entry.summary}\n\n"
        
    prompt = f"以下のニュースを分かりやすく日本語で要約し、重要なポイントをまとめてください。\n\n{news_text}"
    
    print("Geminiで要約を生成中...")
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    
    print("=== ニュース要約結果 ===")
    print(response.text)

if __name__ == "__main__":
    summarize_news()
