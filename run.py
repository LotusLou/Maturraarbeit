from app import flaskapp
#Start des Lokalen Flaskserver 
app = flaskapp()

if __name__ == "__main__":
    app.run(debug=True)