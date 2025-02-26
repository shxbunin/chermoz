from flask import Flask, render_template
import asyncio
from db import create_tables

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/album')
def album():
    return render_template("album.html")

@app.route('/auth')
def auth():
    return render_template("auth.html")

async def main():
    await create_tables()
    app.run(debug=True)

if __name__ == '__main__':
    asyncio.run(main())