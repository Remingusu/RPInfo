import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(map(bot))


class map(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def map(self, ctx):
        embed = discord.Embed(title="Map", color=0x7289da)
        embed.set_thumbnail(url="https://i.ibb.co/cCxzCnT/map.png")
        embed.add_field(name="Carte", value="https://i.ibb.co/7kKg4Ss/carte.png")
        embed.add_field(name="Légende", value="Marron: Neutre\n"
                                              "Bleu ciel : Brise\n"
                                              "Vert : Mousse\n"
                                              "Turquoise : Ruisseaux\n"
                                              "Gris : Rochers\n"
                                              "Rose / Rouge : Bipèdes\n"
                                              "Violet : Territoire pour les réunions entre les clans")
        await ctx.send(embed=embed)
