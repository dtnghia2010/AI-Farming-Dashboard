from application.routes import app  # Import the app instance from routes.py

# This function will be invoked by Vercel to process HTTP requests

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)