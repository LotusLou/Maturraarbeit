from app import flaskapp

app = flaskapp()

if __name__ == "__main__":
    app.run(debug=True)