 # PostBot
 Telegram address - **@smallSenior_bot**

 Bot is created to beautify every message in your channel with unique buttons.
 First, you should add bot to the channel, so, afterwards you have to forward a channel's message to the bot.
 So, that's all. Bot is almost set up.\
 **P.S.** Bot may be added to a group too, so it gonna be filtered of spammers and another bots)

 #### Tasks
 - [X] Beautify posts
 - [X] Filter chat

 #### Stack
 - Python (3.8.2)
 - Aiogram
 - Redis
 
___
### Install on your server using venv
First, you need to install `venv` on your PC
```
sudo apt install -y python3-venv
```
The, you have to create `venv` to isolate libraries, that are used in the app
```shell
python3 -m venv env
source env/bin/activate
```
To disable virtual environment you just need
```
deactivate
```
Install all dependencies
```
pip3 install -r requirements.txt
```
Create config `config.yaml` file in parent`s directory
``` bash
touch config.yaml
```
Fill in from this template:
```yaml
BOT_TOKEN: Your telegram bot token
REDIS_HOST: Redis server address
REDIS_PASS: Redis server pasword
REDIS_PORT: Redis server port
```
Run the application
```
python3 -m app
```
### Install using Docker
```
docker-compose up -d
```
