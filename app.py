from Tutorial import app

@app.route('/')
def home():
    return f'Hello World'

if __name__ == "__main__":
    app.run(debug=True)