import discord
import os
import json



client = discord.Client()

with open('skarbce.json') as s:
  skarbce = json.load(s)

with open('herbs_data.json') as h:
  herbs = json.load(h)

with open('magia.json') as m:
  magia = json.load(m)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if msg[0]=='?':
      text = msg[1:]

      if text in magia['magia']:
        answer = magia['magia'][text]+"."
        await message.channel.send(answer)

      elif text in herbs['herb_id_to_use'] :
        answer = text+" ("+ herbs['herb_id_to_odmiana'][text]['mianownik']+") : "
        for x in herbs['herb_id_to_use'][text]:
          action = x['action']
          effect = x['effect']
          answer2 = f"{action} -> {effect}.\n"
          await message.channel.send(answer+answer2)
    

    if msg in skarbce['klucze'] :
      answer = skarbce['klucze'][msg]+"."
      await message.channel.send(answer)
    
    elif 'latarni' in msg:
      if 'jedna' in msg:
        await message.channel.send("podnies pierwsza wajche;podnies druga wajche;podnies trzecia wajche")
      elif 'dwie' in msg:
        await message.channel.send("podnies pierwsza wajche;opusc druga wajche;podnies trzecia wajche")
      elif 'trzy' in msg:
        await message.channel.send("podnies pierwsza wajche;opusc druga wajche;opusc trzecia wajche")
      elif 'cztery' in msg:
        await message.channel.send("opusc pierwsza wache;podnies druga wajche;podnies trzecia wajche")
      elif 'piec' in msg:
        await message.channel.send("opusc pierwsza wajche;podnies druga wajche;opusc trzecia wajche")
        

client.run('OTM1NTI1MzQwNTkwMjYwMzA3.Ye_53g.VtzTnV1VsBuBwTMEtAt9q1-sNbo')

