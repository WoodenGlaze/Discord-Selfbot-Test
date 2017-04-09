#This is my first attempt at making a self bot, don't judge haha.
#Thanks Jake!

import discord
import asyncio
import json
from discord.ext import commands

def load_credentials():
	with open('credentials.json') as f:
		return json.load(f)


if True == True:
	credentials = load_credentials()
	token = credentials['token']


client = discord.Client()

@client.event
async def on_message(message):


	if message.content.startswith("/ping"):
		if str(message.author.id) == client.user.id:
			await client.send_message(message.channel, 'pong!')
			print('Ping!')



	if message.content.startswith("/info"):
		if str(message.author.id) == client.user.id:
			emin = discord.Embed(title='Bot Info')
			emin.set_author(name='The Doctor#9274', icon_url='https://images-ext-2.discordapp.net/.eJwNwtERgjAMANBdOkATYoqEbUJSBU-l11Z-OHfXe-8Mn_oMc1h7L20GMH9H35rt1bWUaPsL9NCutcGAI9NFiMeB0x9OoEouN8oTiy7XLIksZXQUVkvMGB_lHr4_T10eVQ.6T33CQC-Uvh1jKO5JQw3JGhqJ3w?width=80&height=80')
			emin.add_field(name='Selfbot running on:', value=client.user.name, inline=True)
			emin.add_field(name='User ID:', value=client.user.id, inline=True)
			emin.add_field(name='Library:', value='Python', inline=True)
			emin.add_field(name='Made for:', value='Sniper#8955', inline=True)
			await client.send_message(message.channel, embed=emin)
			print('info was called!')


	if message.content.startswith("5 random ☭"):
		await client.send_message(message.channel, '>pick')
		print('autoharvested rubles')

	if 'planted' in message.content:
		await client.send_message(message.channel, '>pick')

	if message.content.startswith("/embed"):
		if str(message.author.id) == client.user.id:
			emtest = discord.Embed(title='Not Safe For Life')
			emtest.set_author(name=message.author.name, icon_url=client.user.avatar_url)
			emtest.set_thumbnail(url=client.user.avatar_url)
			emtest.set_footer(text='Test', icon_url=client.user.avatar_url)
			await client.send_message(message.channel, embed=emtest)

	if message.content.startswith(".purge"):
		if str(message.author.id) == client.user.id:
			def is_me(m):
				return m.author == client.user
		deleted = await client.purge_from(message.channel, limit=100, check=is_me)
		await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))


	if message.content.startswith(".userinfo"):
		if str(message.author.id) == client.user.id:
				emuinfo = discord.Embed(title='User Info')



				if member is None:
				member = ctx.message.author


				print('Member is: {}'.format(member))
				print('{} called command!'.format(ctx.message.author))
				print('{0.display_name} joined at {0.joined_at}, account was created at: {0.created_at}'.format(member))

				emuinfo.set_author(name='{0.display_name}'.format(member), icon_url='{}'.format(member.avatar_url or member.default_avatar_url))
				emuinfo.set_thumbnail(url='{0.avatar_url}'.format(member))
				"""emuinfo.add_field(name='User:', value='{0.name}'.format(member))"""
				emuinfo.add_field(name='User ID:', value='{0.id}'.format(member))



				emuinfo.add_field(name='Highest Role:', value='{0.top_role}'.format(member))
				emuinfo.add_field(name='Created at:', value='{0.created_at}'.format(member))
				emuinfo.add_field(name='Joined at:', value='{0.joined_at}'.format(member))
				emuinfo.add_field(name='Avatar URL', value='{0.avatar_url}'.format(member))

				print('Userfield defined')
				await client.send_message(message.channel, embed=emuinfo)
				print('Posted Embed!')



	if message.content.startswith(".serverinfo"):
		if str(message.author.id) == client.user.id:
				emsinfo = discord.Embed(title='Server Info')

				
				server = message.server	

				print('Server is: {0.name} (ID: {0.id})'.format(server))
				emsinfo.add_field(name='Server name:', value='{0.name}'.format(server))
				emsinfo.add_field(name='Server ID:', value='{0.id}'.format(server))
				"""emsinfo.add_field(name='Server Roles:', value='{0.roles.name}'.format(server))"""
				"""emsinfo.add_field(name='Server Emojis:', value='{0.emojis}'.format(server))"""
				emsinfo.add_field(name='Server Region:', value='{0.region}'.format(server))
				emsinfo.add_field(name='Server Members:', value='{0.members}'.format(server))
				"""emsinfo.add_field(name='Server Channels:', value='{0.channels}'.format(server))"""
				"""emsinfo.set_thumbnail(url='{0.icon}'.format(server))"""
				emsinfo.add_field(name='Server Owner:', value='{0.owner}'.format(server))

				await client.send_message(message.channel, embed=emsinfo)


	if message.content.startswith(".servers"):
		if str(message.author.id) == client.user.id:
				await client.send_message([(x.name, x.id) for x in client.servers])





	if message.content.startswith(".sendmessage"):
		if str(message.author.id) == client.user.id:
			await client.send_message('NOPE!')



client.run(token, bot=False)