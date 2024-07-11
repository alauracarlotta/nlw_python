from src.main.server.server import app # ter os files de __inits__ dentro dos diretórios, ajudam nas importações ()inclusive na importação so "app" 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True) # servidor cru, do zero
