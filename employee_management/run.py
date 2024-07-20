from app import create_app  # importing app variable


app = create_app() 
if __name__ == "__main__":  # Checking if the script is being run directly
    app.run(debug=True)  # to start the Flask development server with debugging enabled.