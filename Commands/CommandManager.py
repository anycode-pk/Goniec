from discord.ext import commands
import settings
import discord

logger = settings.logging.getLogger("bot")

achievements_table = [
    ["✅","2016", "Promocja WEiI w ramach Dni Otwartych na Politechnice Koszalińskiej"],
    ["✅","2017", "Udział konferencji informatycznej (IT Aacademic Day – Szczecin) organizowany na uczelniach w całej Polsce przez studentów z Grup .NET i Grup IT skierowany do uczniów szkół średnich, studentów oraz osób zainteresowanych nowoczesnymi technologiami."],
    ["✅","2017", "Udział w hackathonie (Hackathon of Things Poznań)"],
    ["✅","2017", "Udział w warsztatach nt. wzorców Repository i Unit of Work w architekturze MVC, które poprowadził Piotr Stola z QuickSolutions"],
    ["✅","2017", "Organizacja konferencji IT Fun Day (4 warsztaty oraz 4 prelekcje)"],
    ["✅","2017", "Środkowopomorskie Targi Pracy GlobalLogic Job Fair - Prezentacja działalności koła oraz Politechniki Koszalińskiej"],
    ["✅","2017", "Wygłoszenie dwóch prelekcji na temat Arduino z praktycznymi przykładami, dla uczniów szkół średnich"],
    ["✅","2017", "Prezentacja działalności koła podczas Dni Otwartych na Politechnice Koszalińskiej"],
    ["✅","2017", "Praca przy projekcie z wykorzystaniem Kinect 2.0, oprogramowania Unity."],
    ["✅","2018", "Praca nad modelami oraz animacjami 3D"],
    ["✅","2018", "Środkowopomorskie Targi Pracy GlobalLogic Job Fair - Prezentacja działalności koła oraz Politechniki Koszalińskiej"],
    ["✅","2018", "Prezentacja działalności koła podczas Dni Otwartych na Politechnice Koszalińskiej"],
    ["✅","2019", "Środkowopomorskie Targi Pracy - Prezentacja działalności koła oraz Politechniki Koszalińskiej"],
    ["✅","2019", "Rozpoczęto prace nad ramieniem robota DIY"],
    ["✅","2019", "Spotkania wyjazdowe w firmach Homanit z Karlina, GlobalLogic z Koszalina"],
    ["✅","2019", "Przygotowania do współpracy Koła .NET z Kołem Pasjonatów Elektroniki i GlobalLogic"],
    ["✅","2019", "Prezentacja Kinect podczas Festiwalu Nauki PK."],
    ["✅","2019", "Prezentacja działalności koła oraz Politechniki Koszalińskiej na targach pracy w Kołobrzegu"],
    ["✅","2019", "Opracowano prototyp nowej strony internetowej Koła"],
    ["✅","2020", "Współudział i pomoc w realizacji projektu UE „Aplikacja bazodanowa do zarządzania finansami wydziału”"],
    ["✅","2020", "Odbyły się wirtualne spotkania z przedstawicielami Objectivity i Fundacja.IT"],
    ["✅","2020", "Zorganizowano mini-hackhaton dla członków koła"]
]

class CommandManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=['i'],
        help="Provide info about AnyCode organization",
        description="",
        brief="Info about AnyCode"
    )
    async def info(self, ctx):
        """Info about AnyCode"""
        logger.info("Executting command $info...")
        await ctx.send("We are student science club \'AnyCode\' at the Koszalin University of Technology")

    @commands.command(
        aliases=['his'],
        help="History of AnyCode",
        description="",
        brief="History of AnyCode"
    )
    async def history(self, ctx):
        """Provide history of AnyCode"""
        logger.info("Executting command $history...")
        await ctx.send("Our organization has a rich history...")

    @commands.command(
        aliases=['m'],
        help="Members of AnyCode",
        description="",
        brief="Members of AnyCode"
    )
    async def members(self, ctx):
        """Provide information about AnyCode members"""
        await ctx.send("Our organization is comprised of a diverse group of members...")
    
    @commands.command(
        aliases=['ach'],
        help="Achievements of AnyCode",
        description="",
        brief="Achievements of AnyCode"
    )
    async def achievements(self,ctx):
        """Provide information about AnyCode achievements"""
        table_content = "\n-----\n".join([" | ".join(row) for row in achievements_table])
        embed = discord.Embed(
            title="Lista Osiągnięć i Działań Koła",
            description=f"```\n{table_content}```",
            color=discord.Color.purple() #kolor embedu
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CommandManager(bot))
