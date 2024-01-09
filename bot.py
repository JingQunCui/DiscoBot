import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE5NDI0MjU2NjE3OTI1ODQzOA.GpxYyZ.AKzZEPXK4uCsXp-jhuX0INxvm2R8b7aU9uZcJ0'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is no running!')

    client.run(TOKEN)

    