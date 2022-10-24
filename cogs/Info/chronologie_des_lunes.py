import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


def setup(bot):
    bot.add_cog(chronologie(bot))


class chronologie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="chronologie", guild_ids=[998628148616904894], description="Donne la chronologie des lunes",
                       options=[create_option(name="classe", description="Choisis la classe d'âge", option_type=3,
                                              required=True,
                                              choices=[create_choice(name="Chaton", value="c"),
                                                       create_choice(name="Adulte", value="ad"),
                                                       create_choice(name="Ancien", value="a")])])
    async def chronologie(self, ctx, classe):
        cembed = discord.Embed(title="Chronologie des Lune", color=0x8B5D5D)
        cembed.set_thumbnail(url="https://i.ibb.co/b7CLSpL/chronologie-des-lunes.png")
        cembed.add_field(name="Les lunes pour les chatons", value="**1 lune:** Le chaton ne fera que téter, gesticuler "
                                                                  "légèrement et miauler mais ne sait pas parler\n"

                                                                  "**2 lunes:** Le chaton commence à pousser de petit "
                                                                  "cris mais ne parle toujours pas. "
                                                                  "Ils ouvrent les yeux à ce moment là "
                                                                  "et rampent légèrement\n"

                                                                  "**3 lunes:** Leurs marches sont faibles, ils ne "
                                                                  "savent pas très bien utiliser leurs petites pattes. "
                                                                  "Ils peuvent commencer à manger un peu de viande "
                                                                  "mais ils continuent à téter\n"

                                                                  "**4 lunes:** Ils peuvent commencer à parler mais "
                                                                  "cela reste très enfantin, pas entier ni "
                                                                  "vraiment précis. Les griffes se forment mais elles "
                                                                  "ne servent encore à rien\n"

                                                                  "**5 lunes:** Ils sont beaucoup plus movibles, "
                                                                  "ils mangent de la viande, les crocs et les griffes "
                                                                  "se forment toujours. Ils grandissent un peu "
                                                                  "chaque jour, mais restent maladroit\n"

                                                                  "**6 lunes:** Les chatons deviennent "
                                                                  "de fier apprentis lors de ce moment !")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        aembed = discord.Embed(title="Chronologie des Lune", color=0x8B5D5D)
        aembed.set_thumbnail(url="https://i.ibb.co/b7CLSpL/chronologie-des-lunes.png")
        aembed.add_field(name="Les Lunes pour les anciens", value="A partir d'un certain âge, les *Sentinelles*, "
                                                                  "*Gardiens*, *Soigneurs*, *Pisteurs*, *Guides* "
                                                                  "et *Conseillers* ne peuvent plus tenir leur rôle.\n"

                                                                  "En général, c'est à partir d'à peu près "
                                                                  "vos 80/85 lunes que vous commencez à vous sentir "
                                                                  "faibles, cependant, il est à noter que vous pouvez "
                                                                  "être envoyé en tant qu'ancien beaucoup plus tôt! "
                                                                  "(maladies, cicatrices handicapantes, "
                                                                  "membres en moins, etc)\n"

                                                                  "Notez que un chat vie en moyenne 180 à 240 lunes.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        adembed = discord.Embed(title="Chronologie des Lune", color=0x8B5D5D)
        adembed.set_thumbnail(url="https://i.ibb.co/b7CLSpL/chronologie-des-lunes.png")
        adembed.add_field(name="Les Lunes pour les adultes", value="A 12 Lunes, un apprenti devient *Sentinelle*, "
                                                                   "*Pisteur* et/ou *Gardien*.\n"

                                                                   "Pour les Apprentis *Soigneurs* c'est 14 Lunes.\n"

                                                                   "Un chat *Pisteur*, *Sentinelle* et *Gardien* "
                                                                   "devient *Vétéran* à 40-45 Lunes.\n"

                                                                   "Les *Vétérans Pisteurs* et *Sentinelles* ont plus "
                                                                   "de chances d'être prit comme *Guide*.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        dico = {"c": cembed,
                "a": aembed,
                "ad": adembed}
        groupe = dico[classe]
        await ctx.send(embed=groupe)
