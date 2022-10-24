import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(credits(bot))


class credits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def credits(self, ctx):
        await ctx.send("Merci à :\n"
                       "- **Naksis#8234** + **NekoCookieEva#4299** + **🧡𝓜𝓪𝓽𝓱𝓲𝓵𝓭𝓮 𝓛𝓪𝓱𝓮𝔂 ✌#6550** "
                       "pour la chronologie des lunes ||(le discord -> https://discord.gg/2QUqekfEGx )||\n"
                       "- **Remingusu33#2155** pour la création du bot *RPInfo*\n"
                       "- **Ethianna#2407** pour l'installation du bot *Tupperbox*")
