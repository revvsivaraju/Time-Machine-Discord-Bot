import discord
from discord.ext import commands
import openai

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

openai.api_key = 'sk-#################################'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def future(ctx, years: int):
   
    prompt = f"Step into the near future, just {years} year:2023+{years} from now, and brace yourself for a breathtaking transformation across architecture, vehicles,technology,climate, space exploration and bio-technology, and human lifestyle! Get ready to witness a world that's brimming with excitement and fascination,write it down in points wise\n\n"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7
    )
    future_text = response.choices[0].text.strip()

    
    image_prompt = f"architecture of cities and vehicles in 2023+{years}, digital art" 
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="512x512"
    )

    image_url = image_response['data'][0]['url']

    
    await ctx.send(future_text)
    await ctx.send(image_url)


@bot.command()
async def past(ctx, years: int):
    era = "A.D" if years >= 0 else "B.C"
    abs_years = abs(years)

   
    prompt = f"Travel back in time to the year {abs_years} {era} and explore the highlights of that time. Witness groundbreaking discoveries, technological advancements, significant events, cultural milestones, and influential personalities that shaped the world.\n\n"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7
    )
    past_text = response.choices[0].text.strip()

   
    image_prompt = f"Streets of capital city of popular and dominating empire in {abs_years} {era},digital art"  
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="512x512"
    )

    image_url = image_response['data'][0]['url']

   
    await ctx.send(past_text)
    await ctx.send(image_url)

bot.run('#################################################')
