import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="help", guild_ids=[998628148616904894], description="Donne la liste des commandes et leur fonction.",
                       options=[create_option(name="commande", description="Choisis la commande", option_type=3,
                                              required=True, choices=[create_choice(name="Promotion",
                                                                                    value="/promotion,\n"
                                                                                          "Promeut un chat; **(valideur de fiche et supérieurs)**"),
                                                                      create_choice(name="Enregistrer",
                                                                                    value="/enregistrer,\n"
                                                                                          "Enregistre une fiche; **(valideur de fiche et supérieurs)**"),
                                                                      create_choice(name="Chronologie des lunes",
                                                                                    value="/chronologie,\n"
                                                                                          "Permet de voir la chronologie des lunes"),
                                                                      create_choice(name="Croyance",
                                                                                    value="/croyance,\n"
                                                                                          "Permet de connaitre les croyances"),
                                                                      create_choice(name="Description des clans",
                                                                                    value="/description,\n"
                                                                                          "Permet de lire les descriptions des clans"),
                                                                      create_choice(name="Jeux",
                                                                                    value="/jeux,\n"
                                                                                          "Permet de jouer au jeux des différents clans"),
                                                                      create_choice(name="L'appel des chefs",
                                                                                    value="/chef_call,\n"
                                                                                          "Permet de prendre connaissance des phrases pour appeler les chefs"),
                                                                      create_choice(name="Map",
                                                                                    value="°map,\n"
                                                                                          "Permet de naviguer sur le territoire"),
                                                                      create_choice(name="Tradition",
                                                                                    value="/traditions,\n"
                                                                                          "Permet d'assimiler les traditions des clans"),
                                                                      create_choice(name="Crédits",
                                                                                    value="°credits,\n"
                                                                                          "Remercie les personnes qui ont aidé à la création du serveur")])])
    async def help(self, ctx, commande):
        await ctx.send(commande)
