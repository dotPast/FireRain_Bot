# Some unless info
# Bot made with PyCharm Community Edition
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import discord
from discord import Option
from datetime import timedelta
from discord.ext import commands, bridge
from mojang import MojangAPI


bot = bridge.Bot(command_prefix="?", help_command=None)


# Bot Events
@bot.event
async def on_ready():
    print(f"Discord Bot - Dev. Info. \n"
          f"On Py-cord \n"
          f"Bot name = {str(bot.user)} \n"
          f"Bot ID = {bot.user.id} \n"
          f"By Not_JustFime \n")

# Bot Commands (For Prefixed/Application Commands Those Don`t Work With ext.Bridge)
# Timeout/Mute member
@bot.slash_command(name = 'mute', description = "Замутить участника")
async def timeout(ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False), days: Option(int, max_value = 27, default = 0, required = False), hours: Option(int, default = 0, required = False), minutes: Option(int, default = 0, required = False), seconds: Option(int, default = 0, required = False)): #setting each value with a default value of 0 reduces a lot of the code
    embed = discord.Embed(
        title="Успешно!",
        description="Пользователь замучен! :no_good:",
        color=discord.Colour.dark_green()
    )
    embed.add_field(name="Пользователь", value=f"<@{member.id}>")
    embed.add_field(name="Дней", value=f"{days}", inline=True)
    embed.add_field(name="Часов", value=f"{hours}", inline=True)
    embed.add_field(name="Минут", value=f"{minutes}", inline=True)
    embed.add_field(name="Секунд", value=f"{seconds}", inline=True)
    embed.add_field(name="Причина", value=f"{reason}")
    embed.add_field(name="Модератор", value=f"<@{ctx.author.id}>")

    embed.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")


    embedfailself = discord.Embed(
        title="Ошибка! :x:",
        description=f"Вы НЕ можете замутить себя!",
        color=discord.Colour.dark_red()
    )

    embedno = discord.Embed(
        title="Успешно!",
        description=f"Пользователь замучен! :no_good:",
        color=discord.Colour.dark_green()
    )
    embedno.add_field(name="Пользователь", value=f"<@{member.id}>")
    embedno.add_field(name="Дней", value=f"{days}", inline=True)
    embedno.add_field(name="Часов", value=f"{hours}", inline=True)
    embedno.add_field(name="Минут", value=f"{minutes}", inline=True)
    embedno.add_field(name="Секунд", value=f"{seconds}", inline=True)
    embedno.add_field(name="Причина", value="Отсутствует")
    embedno.add_field(name="Модератор", value=f"<@{ctx.author.id}>")

    embed.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")

    embedmore28d = discord.Embed(
        title="Ошибка! :x:",
        description=f"Нельзя замутить больше чем на 28 дней!",
        color=discord.Colour.dark_red()
    )

    embedmod = discord.Embed(
        title="Ошибка! :x:",
        description=f"Ты не можешь замутить модератора!",
        color=discord.Colour.dark_red()
    )

    if member.id == ctx.author.id:
        await ctx.respond(embed=embedfailself, ephemeral= True)
        return
    if member.guild_permissions.moderate_members:
        await ctx.respond(embed=embedmod, ephemeral= True)
        return
    duration = timedelta(days = days, hours = hours, minutes = minutes, seconds = seconds)
    if duration >= timedelta(days = 28):
        await ctx.respond(embed=embedmore28d, ephemeral = True)
        return
    if reason == None:
        await member.timeout_for(duration)
        await ctx.respond(embed=embedno, ephemeral= True)
    else:
        await member.timeout_for(duration, reason = reason)
        await ctx.respond(embed=embed, ephemeral= True)

# Untimeout/Unmute member
@bot.slash_command(name = 'unmute', description = "Размутить участника")
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False)):
    embed = discord.Embed(
        title="Успешно!",
        description="Пользователь размучен! :adult:",
        color=discord.Colour.dark_green()
    )
    embed.add_field(name="Пользователь", value=f"<@{member.id}>")
    embed.add_field(name="Причина", value=f"{reason}")
    embed.add_field(name="Модератор", value=f"<@{ctx.author.id}>")
    embed.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")

    embednoreason = discord.Embed(
        title="Успешно!",
        description="Пользователь размучен! :adult:",
        color=discord.Colour.dark_green()
    )
    embed.add_field(name="Пользователь", value=f"<@{member.id}>")
    embed.add_field(name="Причина", value="Отсутствует")
    embed.add_field(name="Модератор", value=f"<@{ctx.author.id}>")
    embed.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")

    if reason == None:
        await member.remove_timeout()
        await ctx.respond(embed=embednoreason)
    else:
        await member.remove_timeout(reason=reason)
        await ctx.respond(embed=embed)

@bot.slash_command(name="ban", description="Забанить пользователя навечно")
async def ban(ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False)):
    embednoreason = discord.Embed(
        title="Успешно!",
        description="Пользователь забанен!",
        color=discord.Colour.dark_green()
    )
    embednoreason.add_field(name="Пользователь", value=f"<@{member.id}>")
    embednoreason.add_field(name="Причина", value=f"Отсутствует")
    embednoreason.add_field(name="Модератор", value=f"<@{ctx.author.id}>")
    embednoreason.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")


    embed = discord.Embed(
        title="Успешно!",
        description="Пользователь забанен!",
        color=discord.Colour.dark_green()
    )
    embed.add_field(name="Пользователь", value=f"<@{member.id}>")
    embed.add_field(name="Причина", value=f"{reason}")
    embed.add_field(name="Модератор", value=f"<@{ctx.author.id}>")
    embed.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")



    if reason == None:
        await member.guild.ban(member)
        ctx.respond(embed=embed)
        return
    else:
        await member.guild.ban(member, reason=reason)
        await ctx.respond(embed=embed)
        return



@bot.slash_command(name = "help", description = "Помощь по командам бота")
async def help(ctx):
    help = discord.Embed(
        title="Помощь",
        description="Команды бота",
        color=discord.Colour.blurple()
    )
    help.add_field(name="Обычные (доступны всем)", value=f"help - все команды бота\nКоманда2 - описание\nКоманда3 - описание")
    help.add_field(name="Префикс", value="Команды работают через /. Описания команд также видны через /.")
    help.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")

    helpmod = discord.Embed(
        title="Помощь",
        description="Команды бота",
        color=discord.Colour.blurple()
    )
    helpmod.add_field(name="Обычные (доступны всем)", value=f"help - все команды бота\nКоманда2 - описание\nКоманда3 - описание")
    helpmod.add_field(name="Модерирование (доступны модераторам)", value=f"mute - замутить пользователя\nunmute - размутить пользователя\nban - забанить")
    helpmod.add_field(name="Префикс", value="Команды работают через /. Описания команд также видны через /.")
    helpmod.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")

    if ctx.author.guild_permissions.moderate_members == True:
        await ctx.respond(embed=helpmod)
        return
    else:
        await ctx.respond(embed=help)
        return

"""""
@bot.slash_command(name= "server", description= "О сервере")
async def aboutserver(ctx):
    serverembed = discord.embed(
        title = "Инфо о сервере",
        color = discord.Colour.orange()
    )
    serverembed.add_field(name="Название", value=ctx.guild.name)
    serverembed.add_field(name="Описание (если есть)", value=ctx.guild.description)
    serverembed.add_field(name="ID", value=ctx.guild.id)
    serverembed.add_field(name="Владелец", value=ctx.guild.owner)
    serverembed.add_field(name="Название", value=ctx.guild.name)
"""""

@bot.slash_command(name= "uuid", description= "Узнать UUID игрока")
async def mctouuid(ctx, nickname: Option(str, required=True)):
    uuid = MojangAPI.get_uuid(nickname)

    embed = discord.Embed(
        title="Ник в UUID",
        color=discord.Colour.dark_green()
    )
    embed.add_field(name="Ник", value=nickname, inline=True)
    embed.add_field(name="UUID", value=uuid, inline=True)
    embed.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")

    embednouser = discord.Embed(
        title="Ник в UUID",
        color=discord.Colour.dark_red(),
        description=f"Пользователь {nickname} не найден!"
    )


    if not uuid:
        await ctx.respond(embed=embednouser, ephemeral=True)
    else:
        await ctx.respond(embed=embed)

@bot.slash_command(name= "nick", description= "Узнать ник игрока")
async def mctonick(ctx, uuid: Option(str, required=True)):
    nickname = MojangAPI.get_username(uuid)

    embed = discord.Embed(
        title="UUID в ник",
        color=discord.Colour.dark_green()
    )
    embed.add_field(name="Ник", value=nickname, inline=True)
    embed.add_field(name="UUID", value=uuid, inline=True)
    embed.set_footer(text="FireRain", icon_url="https://i.imgur.com/OLHSUVu.png")

    embednouser = discord.Embed(
        title="UUID в ник",
        color=discord.Colour.dark_red(),
        description=f"Пользователь с UUID '{uuid}' не найден!"
    )

    if not nickname:
        await ctx.respond(embed=embednouser, ephemeral=True)
    else:
        await ctx.respond(embed=embed)

@bot.slash_command(name= "mcabout", description= "Узнать об игроке")
async def mcabout(ctx, nick: Option(str, required=True)):
    nickuuid = MojangAPI.get_uuid(nick)
    info = MojangAPI.get_profile(nickuuid)
    embed = discord.embed(
        name = f"Об игроке {info.name}",
        description = "Информация об игроке",
        color = discord.Colour.orange()
    )
    embed.add_field(name="Имя", value=info.name, inline=True)




# Bot Commands
bot.run("no token for u")
