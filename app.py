from flask import Flask
import threading
from pyrogram import Client
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png">
    <titleSudoR2spr Repository</title>
	<link rel="icon" type="image/x-icon" href="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png">

</head>

<body>
    <div class="container" style="bg-dark text-red text-center py-3 mt-5">
        <a href="https://github.com/nikhilsaini098" class="card">
            <p>
              />▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄<br 
	      />██░▄▄▄░█░▄▄▀█▄░▄██░▀██░█▄░▄██<br 
              />██▄▄▄▀▀█░▀▀░██░███░█░█░██░███<br 
	      />██░▀▀▀░█░██░█▀░▀██░██▄░█▀░▀██<br 
              />▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀<br />
                                             <br>

                <b>v2.0.0</b>
            </p>
        </a>
    </div>
	<br></br><br></br><br></br>
	<footer class="bg-dark text-white text-center py-3 mt-5">
	<center><img loading="lazy" class="object-none object-center" src="https://tinypic.host/images/2025/04/28/IMG_20250428_085026_585.jpg" width="40" height="40">
        Powered By SAINI 
		<img loading="lazy" class="object-none object-center" src="https://tinypic.host/images/2025/04/28/IMG_20250428_085026_585.jpg" width="40" height="40">
		<div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2024 Video Downloader. All rights reserved.
            </p>
        </div>
    </footer></center>
</body>

</html>
"""



# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running on Render!"

# Pyrogram Bot setup
bot = Client(
    "my_bot",
    api_id=123456,  # apna api_id dalna
    api_hash="your_api_hash",  # apna api_hash dalna
    bot_token="your_bot_token"  # apna bot_token dalna
)

def run_bot():
    bot.run()

# Flask + Bot dono ek sath start karna
if __name__ == "__main__":
    # Bot ko background thread me run karo
    threading.Thread(target=run_bot).start()

    # Flask ko Render ke port par run karo
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
	
if __name__ == "__main__":
    app.run()
