from flask import Flask, render_template
import asyncio
from db import create_tables

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

async def main():
    await create_tables()
    app.run(debug=True)

if __name__ == '__main__':
    asyncio.run(main())