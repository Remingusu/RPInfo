import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


def setup(bot):
    bot.add_cog(description(bot))


class description(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="description", guild_ids=[998628148616904894], description="Donne la description des clans",
                       options=[create_option(name="clan", description="Le nom du clan", option_type=3, required=True,
                                              choices=[create_choice(name="Mousses", value="m"),
                                                       create_choice(name="Brises", value="b"),
                                                       create_choice(name="Ruisseaux", value="ru"),
                                                       create_choice(name="Rochers", value="ro")])])
    async def description(self, ctx, clan):
        # --------------------------------------------------------------------------------------------------------------------------------------------
        embed_rochers = discord.Embed(title="Description du clan des *Rochers*", color=0x999999)
        embed_rochers.set_thumbnail(url="https://i.ibb.co/KsxC6DK/clan-des-rochers.png")
        embed_rochers.add_field(name="Territoire", value="Les chats du Clan des rochers vivent sur un territoire rocailleux. "
                                                         "Environ 3/4 de leur territoire est composé de cailloux !")
        embed_rochers.add_field(name="Physique", value="Ses félins ont un pelage dans les ton sombres et brun. "
                                                       "Par exemple noir, gris (foncé au claire ect) et brun. "
                                                       "On peut voir, assez rarement , des félins couleur crème."
                                                       "Ses chats sauvages, appelait *Matou des cailloux*, sont très tenace. "
                                                       "Leur corps est musclés ."
                                                       "Ils sont aussi très imposants mais moyen ou petit.")
        embed_rochers.add_field(name="Caractères", value="Les membres du Clan des rochers sont assez dure et pas très sentimental. "
                                                         "Ils ont malgré tout des bon sens !", inline=False)
        embed_rochers.add_field(name="Qualités", value="- Courageux\n"
                                                       "- Costaux\n"
                                                       "- Fort\n"
                                                       "- Tenace")
        embed_rochers.add_field(name="Défauts", value="- Non sentimental\n"
                                                      "- Ne sauverons pas un chaton ou une personne "
                                                      "dans le besoin pour la plus par des membres.\n"
                                                      "- Sont moqueur\n"
                                                      "- Rabaisse les autres")

        # --------------------------------------------------------------------------------------------------------------------------------------------
        embed_brises = discord.Embed(title="Description du clan des *Brises*", color=0xE8FEFF)
        embed_brises.set_thumbnail(url="https://i.ibb.co/SmDrJ95/clan-des-brises.png")
        embed_brises.add_field(name="Territoire", value="Les chats du Clan des brises vivent sur un territoire de lande. "
                                                        "Environ 1/6 de leur territoire est composé de champ de bipèdes (de blés)")
        embed_brises.add_field(name="Physique", value="Ses félins ont le pelage dans les tons chauds comme le brun "
                                                      "claire, le roux, le crème ect... Vous ne verrez jamais de chat "
                                                      "de ce Clan avec une fourrure noir ! "
                                                      "Sauf si c'est un ancien solitaire.")
        embed_brises.add_field(name="Caractères", value="Les membres du Clan des brises sont très sage et diplomate. "
                                                        "Même si ils ont aussi des défauts ! Ses chats sauvages, appelait Matou des vents, sont très grands. "
                                                        "Leur patte son musclés et fine. Le corps et fin et élancé.", inline=False)
        embed_brises.add_field(name="Qualités", value="- Sage\n"
                                                      "- Diplomate\n"
                                                      "- Calme\n"
                                                      "- Ignore les insultes")
        embed_brises.add_field(name="Défauts", value="- Parle peu\n"
                                                     "- Se sente supérieure\n"
                                                     "- Dicte la conduite aux autres\n"
                                                     "- Fragile (physique)")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        embed_ruisseaux = discord.Embed(title="Description du clan des *Ruisseaux*", color=0x00D5DC)
        embed_ruisseaux.set_thumbnail(url="https://i.ibb.co/7jthD83/clan-des-ruisseaux.png")
        embed_ruisseaux.add_field(name="Territoire", value="Les chats du Clan des ruisseaux vivent sur un territoire "
                                                           "de ruisseaux et de rivière comportant un UNIQUE torrent.")
        embed_ruisseaux.add_field(name="Physique", value="Ses félins ont le pelage dans les ton froids comme du blanc, "
                                                         "du gris ect... Certains ont le pelage crème ou "
                                                         "brun claire. Ses chats sauvages, appelait Matou des eaux,"
                                                         " ont une fourrure épaisse pour les protéger du froid "
                                                         "dans l'eau avec des pattes musclés .")
        embed_ruisseaux.add_field(name="Caractère", value="Les membres du Clan des brises sont très énergique. "
                                                          "Ils ont aussi leurs défauts !", inline=False)
        embed_ruisseaux.add_field(name="Qualités", value="- Agile\n"
                                                         "- Gentil\n"
                                                         "- Drôle\n"
                                                         "- D'étende l'atmosphère")
        embed_ruisseaux.add_field(name="Défauts", value="- Naïf\n"
                                                        "- Pas suffisament sérieux\n"
                                                        "- Trop énergique\n"
                                                        "- Ne suivent pas les règles")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        embed_mousses = discord.Embed(title="Description du clan des *Mousses*", color=0x1B8D25)
        embed_mousses.set_thumbnail(url="https://i.ibb.co/xMGh3nc/clan-des-mousses.png")
        embed_mousses.add_field(name="Territoire", value="Les chats du Clan des mousses vivent sur un territoire "
                                                         "forestier avec différents arbres comme des bouleaux, "
                                                         "des chênes, de pins ect... Environ 95%' de leur "
                                                         "territoire est constitué de forêt.")
        embed_mousses.add_field(name="Physique", value="Ses félins ont le pelage dans les ton assez sombres. "
                                                       "Vous verrez rarement du blanc sauf pour les solitaires. "
                                                       "Ses chats sauvages, appelait Matou écureuils, ont des pattes "
                                                       "musclés pour escalader les arbres. Leur fourrure peu être touffu, "
                                                       "court ou mi-long ")
        embed_mousses.add_field(name="Caractère", value="Les membres du Clan des mousses sont très calme et courageux. "
                                                        "Aussi très intelligent, ils ont aussi leur défauts !", inline=False)
        embed_mousses.add_field(name="Qualités", value="- Intelligent\n"
                                                       "- Rusée\n"
                                                       "- Calme\n"
                                                       "- Agile")
        embed_mousses.add_field(name="Défauts", value="- Trop sérieux\n"
                                                      "- Calculatrice\n"
                                                      "- Se sente un peu supérieure\n"
                                                      "- Aide trop de personne")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        dico = {"m": embed_mousses,
                "b": embed_brises,
                "ru": embed_ruisseaux,
                "ro": embed_rochers}

        choix = dico[clan]
        await ctx.send(embed=choix)
