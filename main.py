import discord
import asyncio
import datetime
import time
import os

client = discord.Client()


@client.event
async def on_ready():
    print('<----------KiKo#7385---------->')
    print(client.user.name)
    print(client.user.id)
    print('<----------KiKo#7385---------->')


    while True:
        await client.change_presence(game=discord.Game(name="O nosso Server do Discord está agora com {} membros!".format(str(len(set(client.get_all_members())))), type=1, url='https://twitch.tv/loja.invyctusmc.com.br'),status='streaming')
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name="O meu criador é o KiKo#7385"))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name="Eu pertenço à Rede Invyctus!"))
        await asyncio.sleep(10)


@client.event
async def on_member_join(member):
    canal = client.get_channel("454581249604976650")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("496078168462065664")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("451940054072557568")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("451941281157873665")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("451940448026755083")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("490286310104236032")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("496105438941675521")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("497870092928024584")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))


@client.event
async def on_member_remove(member):
    canal = client.get_channel("454581249604976650")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("496078168462065664")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("451940054072557568")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("451941281157873665")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("451940448026755083")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("490286310104236032")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("496105438941675521")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
    canal = client.get_channel("497870092928024584")
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))


client.run(os.environ.get('TOKEN'))