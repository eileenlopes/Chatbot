#imports start
##########################################################################################################################################

import discord

import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

##########################################################################################################################################
#imports end

#variables start
##########################################################################################################################################

client = discord.Client()
Base = declarative_base()
engine = create_engine('sqlite:///messages.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

##########################################################################################################################################
#variables end

#functions start
##########################################################################################################################################

#puts the message in the database
def addMessageToDB(message):
    session = DBSession()
    m = Message(sender=message.author.name, content=message.content)
    session.add(m)
    session.commit()

#called when a message is received to further process it.
def ReceivedMessage(message):
    print("received a message from " + message.author.name)
    addMessageToDB(message)

#########################################################################################################################################
#functions end

#discordstuff start
##########################################################################################################################################



def discordConnection():
    TOKEN = 'NDQ2NjU0NzEzMDg2MDgzMDcz.Dd8LRg.jQfWV8UclPrVqBwBR19KS9xeugM'
    client.run(TOKEN)
    return client

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    ReceivedMessage(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
#>>>>>>> 66877c3e8fbedbf2a23b8b645bf2ae222f612739

##########################################################################################################################################
#discordstuff end

#analyse start
##########################################################################################################################################



##########################################################################################################################################
#analyse end

#database start
##########################################################################################################################################

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True) 
    sender = Column(String(50))
    content = Column(String(500))

def createTablesDB():
    Base.metadata.create_all(engine)

##########################################################################################################################################
#database end


#main program start
##########################################################################################################################################







#function that calls other functions, only called when user input starts with "-"
def func_caller(command):
	if command == "-k":
		parameter = input("Enter the keywords you want to add to the keyword list, seperated by spaces \n").split(" ") #aks the user for input and split it on space
		keyword_update(parameter,0)
	elif command == "-s":
		display_keywords()
	elif command == "-d":
		remove_keyword_entry()
	else:
		print("Command not recognized, try again! \n")


def lookup_matching_employee(inp):
	keys = inp.split(" ")
	print("Not implemented yet!")
	#return all users from database who match at least one of the entries in the keys list

def remove_keyword_entry():
	keywords_tobe_removed = input("Enter the keywords you want to remove from the keyword list, seperated by spaces \n").split(" ")
	try:
		f = open("keywords.txt","r")
		content = f.readlines()
		content = [x.strip() for x in content]
		for word in keywords_tobe_removed:
			try:
				content.remove(word)
			except:
				print(word+" was not found in the keyword list \n")
		keyword_update(content,1)

		f.close()
	except:
		print("File not found, create a new keyword list with the -k command")


def keyword_update(new_keywords,id): #updates the keyword file, creates it if it doesn't exist.
	if id == 0:
		f = open("keywords.txt","a+") #open the keywords file in append mode, creating a keywords file if it doesn't exist
	else:
		f = open("keywords.txt","w+") #open the keywords file in write mode, creating a keywords file if it doesn't exist
	for word in new_keywords:
		f.write(word+"\n")
	f.close()
	print("update complete")

def display_keywords(): #prints all keywords, handles the file not found error
	try:
		f = open("keywords.txt","r")
		content = f.readlines()
		content = [x.strip() for x in content] 
		for word in content:
			print(word)
		f.close()
	except:
		print("File not found, create a new keyword list with the -k command")

def message(message):
    print('received a message from ' + message.author.name)


# Define main() function
def main():
	loop = True
	print("use the -k command to add entries to the keyword list"+"\n"+"use the -s command to print all keywords"+"\n"+"use the -d command to delete keywords from the list")
	while loop:
		user_input = input()
		if user_input[:1] != "-":
			lookup_matching_employee(user_input)
		else:
			func_caller(user_input[:2])



state = input("enter 0 for discord bot mode, enter 1 for data retrieval mode \n")
if input == 0:
	client = discordConnection()
else:
	main()



#createTablesDB()





##########################################################################################################################################
#main program end