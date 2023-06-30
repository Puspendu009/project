from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

# Default route to return index.html
@app.route('/')
def index():
    return render_template('index.html')

# API route to handle POST request
@app.route('/api', methods=['POST'])
def api():
    # Retrieve the string parameter from the request
    input_string = request.form.get('string')

    # Send request to OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the engine to use
        prompt=input_string,
        max_tokens=100  # Adjust as needed
    )

    # Retrieve the generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Return the generated text as the API response
    return generated_text

if __name__ == '__main__':
    app.run()

