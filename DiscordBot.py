import discord
from random import randint
from discord.ext import commands


class TicTacToe:
    __matrix = [["#" for x in range(3)] for y in range(3)]
    __id=0
    __numturns=0
    def __init__(self,id):
        self.__id=id

    def getID(self):
        return self.__id

    def turn(self,x,y):
        if self.__matrix[x][y] is "#":
            self.__matrix[x][y]='X'
        else:
            print('already taken',self.__matrix[x][y])
            return
        completed = False
        counter = 0
        self.__numturns+=1
        while not completed:
            print("loop")
            counter += 1
            xx=randint(0,2)
            yy=randint(0,2)
            if self.__matrix[xx][yy] is "#":
                completed=True
                self.__matrix[xx][yy]="O"
            if counter > 100:
                break


    def getMatrix(self):
        return self.__matrix

    def gameEnd(self):
        return self.__numturns>4


bot = commands.Bot(command_prefix='!')
gamelist = []


def getGameByID(id):
    for t in gamelist:
        if t.getID()==id:
            return t
        else:
            return None

def matrixToText(matrix):
    string = ""
    for list in matrix:
        string += "\n-----------\n|"
        for c in list:
            string += c + " | "
    string += "\n-----------\n"
    return string


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)


@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def tictactoe(ctx):
    game =TicTacToe(ctx.author.id)
    gamelist.append(game)
    await ctx.send("Started game with "+ctx.author.name+"(id="+str(ctx.author.id)+")\n"+matrixToText(game.getMatrix()))

@bot.command()
async def getgames(ctx):
    ids = ""
    for t in gamelist:
        ids+=" "+str(t.getID())
    if ids=="":
        await ctx.send("No active games")
    else:
        await ctx.send(ids)

@bot.command()
async def turn(ctx, x: int, y: int):
    game = getGameByID(ctx.author.id)
    if game==None:
        await ctx.send("No active game found. Please start a game with !tictactoe")
    else:
        game.turn(x,y)
        await ctx.send(matrixToText(game.getMatrix()))
        if game.gameEnd():
            print("End")
            gamelist.remove(game)




@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Name", description="Test Bot", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Arcane")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    #embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="!tictactoe", value="Starts a new game of TicTacToe", inline=False)
    embed.add_field(name="!turn X Y", value="Takes a turn in your game of TTT", inline=False)
    embed.add_field(name="!add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="!multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('<Token here>')
