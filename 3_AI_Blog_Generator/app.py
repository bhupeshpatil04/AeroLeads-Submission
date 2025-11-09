# AI Blog Generator (Flask App)
# ------------------------------
# Uses OpenAI / Gemini / Perplexity APIs to generate blog articles.

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY_HERE"

@app.route('/generate', methods=['POST'])
def generate_blog():
    data = request.get_json()
    title = data.get('title', 'Untitled')
    prompt = f"Write a detailed blog post about: {title}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    article = response['choices'][0]['message']['content']
    return jsonify({"title": title, "content": article})

if __name__ == "__main__":
    app.run(debug=True)
