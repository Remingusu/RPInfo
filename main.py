import fnmatch
import os
import discord
import asyncio
import help
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice

bot = commands.Bot(command_prefix="°", description="Informations sur ce RP")
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)
bot.remove_command('help')

def owner(ctx):
    return ctx.author.id == 693761548048531509


@bot.event
async def on_ready():
    path = './cogs'
    root = os.listdir(path)
    file_list = []
    for folders in root:
        new_root = f'{path}/{folders}'
        dirs = os.listdir(new_root)
        for files in dirs:
            if fnmatch.fnmatch(files, '*.py'):
                last_root = f'{new_root}/{files}'
                result = last_root.replace("/", ".")
                result = result.replace(".py", "")
                result = result.replace("..", "")
                file_list.append(result)
    for ext in file_list:
        __import__(ext)
        await asyncio.sleep(0.2)
    print("Ready !")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Permission(s) manquante(s).")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Commande inconnue.")
    elif isinstance(error, commands.ExtensionFailed):
        await ctx.send("Erreur lors du chargement de l'extension. ")
    elif isinstance(error, commands.ExtensionNotFound):
        await ctx.send("Extension inconnue.")
    elif isinstance(error, commands.ExtensionError):
        await ctx.send("Erreur provenant de l'extension.")
    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send("Extension non chargée.")
    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send("Extension déjà chargée.")
    else:
        print(error)
        await ctx.send("Une erreur est survenue !")
        await ctx.send(error)


@bot.command()
async def rp(ctx):
    guild = bot.get_guild(998628148616904894)
    channel = guild.get_channel(998636424964358154)
    message_channel = ctx.message.channel
    author = ctx.message.author
    if message_channel == channel:
        await ctx.send(f"||@here||\n{author.mention} demande à RP !")
    else:
        pass

ext_dico = {"a": "a",
            "i": "i",
            "pro": 'cogs.Promotion.promotion',
            "tra": 'cogs.Info.tradition',
            "descla": 'cogs.Info.descriptions_des_clans',
            "cre": 'cogs.Info.credits',
            "chrlun": 'cogs.Info.chronologie_des_lunes',
            "jeu": 'cogs.Info.jeux',
            "cro": 'cogs.Info.croyance',
            "fic": 'cogs.Fiche.card_manager',
            "car": 'cogs.Info.map',
            "lappche": 'cogs.Info.l_appel_des_chef'}

ext_all = ['cogs.Promotion.promotion',
           'cogs.Info.tradition',
           'cogs.Info.chronologie_des_lunes',
           'cogs.Info.descriptions_des_clans',
           'cogs.Info.credits',
           'cogs.Info.jeux',
           'cogs.Info.croyance',
           'cogs.Info.l_appel_des_chef',
           'cogs.Info.map',
           'cogs.Fiche.card_manager']

ext_info = ['cogs.Info.tradition',
            'cogs.Info.chronologie_des_lunes',
            'cogs.Info.descriptions_des_clans',
            'cogs.Info.credits',
            'cogs.Info.jeux',
            'cogs.Info.l_appel_des_chef',
            'cogs.Info.map',
            'cogs.Info.croyance']


@commands.has_permissions(administrator=True)
@slash.slash(name="load", guild_ids=[998628148616904894], description="Charge une extension",
             options=[create_option(name="extension", description="Choisis une extension", option_type=3,
                                    required=True, choices=[create_choice(name="All", value="a"),
                                                            create_choice(name="Infos", value="i"),
                                                            create_choice(name="Promotion", value="pro"),
                                                            create_choice(name="Tradition", value="tra"),
                                                            create_choice(name="Description des clans", value="descla"),
                                                            create_choice(name="Crédits", value="cre"),
                                                            create_choice(name="Chronologie des Lunes", value="chrlun"),
                                                            create_choice(name="Jeux", value="jeu"),
                                                            create_choice(name="Fiche", value="fic"),
                                                            create_choice(name="Croyance", value="cro"),
                                                            create_choice(name="Carte", value="car"),
                                                            create_choice(name="L'appel des chefs", value="lappche")])])
async def load(ctx, extension):
    selection = ext_dico[extension]
    if selection == "a":
        await ctx.send("Veuillez patientez, le temps du chargement...")
        for ext in ext_all:
            if ext is commands.ExtensionAlreadyLoaded:
                pass
            bot.load_extension(ext)
            await asyncio.sleep(0.5)
    elif selection == "i":
        await ctx.send("Veuillez patientez, le temps du chargement...")
        for ext in ext_info:
            if ext is commands.ExtensionAlreadyLoaded:
                pass
            bot.load_extension(ext)
            await asyncio.sleep(0.5)
    else:
        if selection is commands.ExtensionAlreadyLoaded:
                await ctx.send("L'extension est déjà chargé")
        await ctx.send("Veuillez patientez, le temps du chargement...")
        bot.load_extension(selection)
    await slash.sync_all_commands()
    await ctx.send(f"Terminez !")


@commands.has_permissions(administrator=True)
@slash.slash(name="reload", guild_ids=[998628148616904894], description="Recharge une extension",
             options=[create_option(name="extension", description="Choisis une extension", option_type=3,
                                    required=True, choices=[create_choice(name="All", value="a"),
                                                            create_choice(name="Infos", value="i"),
                                                            create_choice(name="Promotion", value="pro"),
                                                            create_choice(name="Tradition", value="tra"),
                                                            create_choice(name="Description des clans", value="descla"),
                                                            create_choice(name="Crédits", value="cre"),
                                                            create_choice(name="Chronologie des Lunes", value="chrlun"),
                                                            create_choice(name="Jeux", value="jeu"),
                                                            create_choice(name="Fiche", value="fic"),
                                                            create_choice(name="Croyance", value="cro"),
                                                            create_choice(name="Carte", value="car"),
                                                            create_choice(name="L'appel des chefs", value="lappche")])])
async def reload(ctx, extension):
    selection = ext_dico[extension]
    if selection == "a":
        await ctx.send("Veuillez patientez, le temps du rechargement...")
        for ext in ext_all:
            if ext is commands.ExtensionNotLoaded:
                pass
            bot.reload_extension(ext)
            await asyncio.sleep(0.5)
    elif selection == "i":
        if selection is commands.ExtensionNotLoaded:
                pass
        await ctx.send("Veuillez patientez, le temps du rechargement...")
        for ext in ext_info:
            bot.reload_extension(ext)
            await asyncio.sleep(0.5)
    else:
        if selection is commands.ExtensionNotLoaded:
                await ctx.send("L'extension n'est pas chargé.")
        await ctx.send("Veuillez patientez, le temps du rechargement...")
        bot.reload_extension(selection)
    await slash.sync_all_commands()
    await ctx.send(f"Terminez !")


@commands.has_permissions(administrator=True)
@slash.slash(name="unload", guild_ids=[998628148616904894], description="Décharge une extension",
             options=[create_option(name="extension", description="Choisis une extension", option_type=3,
                                    required=True, choices=[create_choice(name="All", value="a"),
                                                            create_choice(name="Infos", value="i"),
                                                            create_choice(name="Promotion", value="pro"),
                                                            create_choice(name="Tradition", value="tra"),
                                                            create_choice(name="Description des clans", value="descla"),
                                                            create_choice(name="Crédits", value="cre"),
                                                            create_choice(name="Chronologie des Lunes", value="chrlun"),
                                                            create_choice(name="Jeux", value="jeu"),
                                                            create_choice(name="Fiche", value="fic"),
                                                            create_choice(name="Croyance", value="cro"),
                                                            create_choice(name="Carte", value="car"),
                                                            create_choice(name="L'appel des chefs", value="lappche")])])
async def reload(ctx, extension):
    selection = ext_dico[extension]
    if selection == "a":
        await ctx.send("Veuillez patientez, le temps du déchargement...")
        for ext in ext_all:
            if ext is commands.ExtensionNotLoaded:
                pass
            bot.unload_extension(ext)
            await asyncio.sleep(0.5)
    elif selection == "i":
        await ctx.send("Veuillez patientez, le temps du déchargement...")
        for ext in ext_info:
            if ext is commands.ExtensionNotLoaded:
                pass
            bot.unload_extension(ext)
            await asyncio.sleep(0.5)
    else:
        if selection is commands.ExtensionNotLoaded:
                await ctx.send("L'extension n'était pas chargé.")
        await ctx.send("Veuillez patientez, le temps du déchargement...")
        bot.unload_extension(selection)
    await slash.sync_all_commands()
    await ctx.send(f"Terminez !")

bot.add_cog(help.help(bot))
bot.run("Token")
