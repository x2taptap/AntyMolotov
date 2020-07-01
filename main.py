from spellchecker import SpellChecker
import discord
client = discord.Client()
spell = SpellChecker(language=None, case_sensitive=True)
print("Ładowanie Słownika")
spell.word_frequency.load_text_file('dict.txt')
print("Załadowany")
@client.event
async def on_ready():
    print('Zalogowałem sie jako {0.user}'.format(client))
@client.event

async def on_message(message):
    global lastmsg
    if message.author == client.user:
        return
    if client.user.mentioned_in(message):
        try:
            misspelled = spell.unknown(lastmsg.split(" "))
            if len(misspelled) > 0:
                embed=discord.Embed(title="AntyMolotov [Wykryto Debila]", color=0xff0000)
                embed.add_field(name="Błedy znalezione w ostatnim zdaniu:", value=" ".join(misspelled), inline=False)
                if len(misspelled) == 1:
                    embed.add_field(name="Mogło tobie chodzić o:", value=(spell.correction("".join(misspelled))), inline=False)
                embed.set_footer(text="System AntyMolotov Stworzony przez kasjan321")   
                await message.channel.send(embed=embed)      
            else:
                embed=discord.Embed(title="AntyMolotov [Wszystkie systemy działają poprawnie]", description="Miłego Dnia ", color=0x2bff00)
                await message.channel.send(embed=embed)  
        except NameError:
            await message.channel.send("Nie widziałem ostatniej wiadomosci >w<")
    else:
        lastmsg = message.content
        return




client.run('token')

