import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


def setup(bot):
    bot.add_cog(believe(bot))


class believe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="croyance", guild_ids=[998628148616904894], description="Donne les croyances des chats",
                       options=[create_option(name="croyance", description="Choisis la croyance", option_type=3, required=True,
                                              choices=[create_choice(name="Clan Ancestral", value="ca"),
                                                       create_choice(name="Clan Oublié", value="co")])])
    async def believe(self, ctx, croyance):
        # --------------------------------------------------------------------------------------------------------------------------------------------
        a_embed = discord.Embed(title="Clan Ancestral", color=0xb3b3b3)
        a_embed.set_thumbnail(url="https://i.ibb.co/Npf2vvn/symbole-clan-ancestral.png")
        a_embed.add_field(name="Description", value="Les membres du Clan ancestral regroupe tout les gentils chats. "
                                                    "Ce qui on été bon ou neutre dans leur vie de vivant. "
                                                    "Ils vivent sur le territoire des Clans mais dans le ciel.")
        a_embed.add_field(name="Territoire", value="https://i.ibb.co/c2Hqq6d/carte-ancestral.png", inline=False)
        a_embed.add_field(name="Légende", value="La zone bleu correspond à leur territoire.\n"
                                                "La zone violette correspond au lieu des assemblées.\n"
                                                "La zone rouge c'est chez les bipèdes et "
                                                "La zone marron c'elle des solitaires.\n"
                                                "Leur symbole est l'image en haut à droite")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        o_embed = discord.Embed(title="Clan Oublié", color=0x941D1D)
        o_embed.set_thumbnail(url="https://i.ibb.co/Rydjmr9/clan-oubli.png")
        o_embed.add_field(name="Description", value="Le Clan oublié rassemble les chats meurtriers, assoiffés de pouvoir. "
                                                    "Ce Clan vit autour d'un lac d'eau noir entourer "
                                                    "d'une forêt sombre et brumeuse.")
        o_embed.add_field(name="Territoire", value="https://i.ibb.co/dtM2mJh/carte-oubli.png", inline=False)
        o_embed.add_field(name="Légende", value="La zone grise correspond au lieu des assemblées\n"
                                                "La zone noir correspond à leur territoire\n"
                                                "La zone marron correspon au territoire neutre."
                                                "Leur symbole est en haut à droite.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        dico = {"ca": a_embed,
                "co": o_embed}
        choix = dico[croyance]
        await ctx.send(embed=choix)
