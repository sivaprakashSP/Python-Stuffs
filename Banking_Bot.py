from nltk.chat.util import Chat, reflections
pairs =[
    [
        r"hi|hey|hello",
        ["Hey there how can i help you??",]
    ],
    [
        r"i want (.*)",
        [
            "Ok But before that provide your personal details to fill in the form!!what's ur name??",
            "Provide us with ur personal details!!what's ur name??",
        ]
    ],
    [
        r"name (.*) | (.*)",
        [
            "Your date of birth??",
            "Your DOB please??",
        ]
    ],
    [
        r"DOB (.*)",
        [
            "Your age??",
            "What's your age??",
        ]
    ],
    [
        r"age (.*)",
        [
            "Your email id??",
            "Give your mail id ??",
        ]
    ],
    [
        r"mail id(.*)",
        [
            "Your residential address??",
            "Your permanent address where u reside??",
        ]
    ],
]
def Bank():
        print("Hi, I'm Bankbot and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
        chat = Chat(pairs, reflections)
        chat.converse()
if __name__ == "__main__":
    Bank()