#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Creating ChatBot Instance
bot = ChatBot('CustomerAI Bot')

 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "Hi",
    "Hi there!",
    "I need some help",
    "How can I help you?",
    "I haven't received my flipkart order till know",
    "What's your Name?",
    "Akhila",
    "Is this your Order ID: OD121956813048566000",
    "Yes",
    "Your order is on the way",
    "Thanks for the info",
    "You're welcome."
   
]

trainer = ListTrainer(bot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(bot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 


if __name__ == "__main__":    
   app.run()