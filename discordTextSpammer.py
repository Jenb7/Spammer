import requests

channelID = enter channel id here
headers = {"authorization": "token goes here"}

file = open("text.txt", "r")
lines = file.readlines()

for line in lines:
    requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", headers = headers, json = {"content": line})
