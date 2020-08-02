from nltk.tokenize import sent_tokenize
print(sent_tokenize("Hi there!,How are you doing?,How is your quarantine days going on?"))
from nltk.chat.util import Chat,reflections
pairs = [
    [
        r"i need (.*)",
        ["Yes how can i help you",]
    ],
    [
        r"i want (.*)",
        ["Okay to apply you must get an KYC form and apply using that form"]
    ],
    [
        r"yes i already(.*)",
        ["Okay then what's ur name??"]
    ],
    [
        r"my name is (.*)",
        ["Your name is %1"]
    ],
    [
        r"Yes",
        ["Give your DOB"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]
def chatty():
        print("Hi, I'm Chatbot and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") 
        chat = Chat(pairs, reflections)
        chat.converse()
if __name__ == "__main__":
    chatty()