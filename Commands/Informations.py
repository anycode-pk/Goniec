import asyncio
from discord.ext import commands
import settings
import discord


logger = settings.logging.getLogger("bot")
PURPLE_COLOR = discord.Color.purple()

projects_list = [
        {
            "name": "GoniecBot",
            "description": "This bot serves as a representative function for new discord server members. It's built using Discord.py and Python.",
            "status": "In Development"
        },
        {
            "name": "TableBooking",
            "description": "TableBooking is a web application that allows you to book a table at your favorite restaurant. Using C#, .NET, PostgreSQL, Ionic, and Vue.",
            "status": "In Development",
            "github_link": "[GitHub](https://github.com/anycode-pk/TableBooking)"
        },
        {
            "name": "Chicken Game",
            "description": "Chicken Game is a 2D game written in C# and developed in the Unity engine.",
            "status": "Active",
            "github_link": "[GitHub](https://github.com/anycode-pk/ChickenGame)"
        },
        {
            "name": "Chess Robot",
            "description": "It's a chess arm that plays chess with you, controlled by a chess engine. It uses a Raspberry Pi and Python.",
            "status": "In Development"
        }
    ]

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

class Informations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Information commands"

    @commands.command(
        aliases=['a'],
        help="Provide info about AnyCode organization",
        description="",
        brief="Info about AnyCode"
    )
    async def about(self, ctx):
        """
        Usage: $about or $a

        About AnyCode
        """
        logger.info("Executting command $info...")
        about_message = (
            "Welcome to AnyCode, the Student Science Club at The Koszalin University of Technology! 🚀 Previously known as 'Grupa .NET'\n\n"
            "👤 Our Patron: Doctor of Engineering Rafał Wojszczyk\n"
            "🌐 We create software independently of any framework or language, "
            "embracing the freedom to choose the best tools for the problem.\n"
            "🤝 We work together because we are passionate about writing code and solving challenges.\n"
            "🏢 We also have our own classroom in 103-1D. We meet there every Thursday at 2pm Come visit us!.\n"
            "⏳ Fun Facts: 'Grupa .NET', now known as 'AnyCode' (since October 2023) has been active since 2008, that's over a decade of coding excellence! 🎉\n"
            "More specific information about our organization can be found on our website or by contacting us.\n"
        )

        await ctx.send(about_message)

    @commands.command(
        aliases=['m'],
        help="Members of AnyCode",
        description="",
        brief="Members of AnyCode"
    )
    async def members(self, ctx):
        """
        Usage: $members or $m

        Provide information about AnyCode members
        """
        await ctx.send("Our organization is comprised of a diverse group of members...")
    
    @commands.command(
        aliases=['ach'],
        help="Achievements of AnyCode",
        description="",
        brief="Achievements of AnyCode"
    )
    async def achievements(self,ctx):
        """
        Usage: $achievements or $ach

        Provide information about AnyCode achievements
        """
        table_content = "\n-----\n".join([" | ".join(row) for row in achievements_table])
        embed = discord.Embed(
            title="List of our achievements and our activities",
            description=f"```\n{table_content}```",
            color=PURPLE_COLOR
        )
        await ctx.send(embed=embed)

    @commands.command(
    aliases=['s'],
    help="Links to AnyCode's social media platforms",
    description="This command provides links to AnyCode's official social media profiles and website",
    brief="Access AnyCode's social media and contact"
    )
    async def social(self, ctx):
        """
        Usage: $social or $s

        Provides links to AnyCode's official social media profiles and contact.
        Stay connected with us on various platforms!
        """
        embed = discord.Embed(
            title="🌐 AnyCode Social Links and contact",
            description="Stay connected with us on various platforms!",
            color=PURPLE_COLOR
        )

        embed.add_field(name="Facebook", value="[Facebook](https://www.facebook.com/anycodepk)")
        embed.add_field(name="GitHub", value="[GitHub](https://github.com/anycode-pk)")
        embed.add_field(name="Contact", value="anycodepk@gmail.com")
        #embed.add_field(name="LinkedIn", value="[LinkedIn](https://www.linkedin.com/company/anycode)")

        await ctx.send(embed=embed)

    @commands.command(
    aliases=['p'],
    help="Displays a list of current and past projects your organization has been developing, along with descriptions and status.",
    description="Usage: $projects or $p\n\nDisplays a list of current and past projects your organization has been developing, along with descriptions and status.",
    brief="List of organization's projects"
    )
    async def projects(self, ctx):
        """
        Usage: $projects or $p

        Displays a list of current and past projects your organization has been developing, along with descriptions and status.
        """
        embed = discord.Embed(
            title="List of Organization's Projects",
            color=discord.Color.purple()
        )
        
        for project in projects_list:
            name = project['name']
            description = project['description']
            status = project['status']
            github_link = project.get('github_link', None)

            field_value = f"**Description:** {description}\n**Status:** {status}"
            if github_link:
                field_value += f"\n{github_link}"

            embed.add_field(
                name=name,
                value=field_value,
                inline=False
            )

        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Informations(bot))