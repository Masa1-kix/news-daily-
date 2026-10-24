import os
import feedparser
import requests
from google import genai

# 1. 環境変数からAPIキーを取得
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# 2. RSSからニュースを取得（NHKニュースの例）
RSS_URL = "https://www3.nhk.or.jp/rss/news/cat0.xml"
feed = feedparser.parse(RSS_URL)

# 最新3件の記事タイトルとリンクをまとめる
news_text = ""
for entry in feed.entries[:3]:
    news_text += f"- タイトル: {entry.title}\n  リンク: {entry.link}\n\n"

# 3. Gemini APIで要約を生成
client = genai.Client(api_key=GEMINI_API_KEY)
prompt = f"""
以下のニュース記事を読み、それぞれの要点を「忙しい人向けに2行」で簡潔に要約してください。最後にポジティブな朝の挨拶も添えてください。

{news_text}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)
summary_message = response.text

print(summary_message)
