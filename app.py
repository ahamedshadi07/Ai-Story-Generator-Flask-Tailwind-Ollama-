from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.get_json()
    prompt = "Write a short, creative story based on this prompt: " + request.json.get("prompt", "")
   # prompt = data.get('prompt', '')

    try:
        # Run Ollama to generate a story
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"  # : Explicitly set UTF-8 encoding
        )

        story = result.stdout.strip()
        return jsonify({"story": story})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
