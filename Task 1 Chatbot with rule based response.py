#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import re

class RuleBot:
    negative_res = ("no", "nope", "nah", "naw", "nothing", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_question = (
        "How was your day today?",
        "What's your favorite hobby?",
        "Tell me about a recent adventure you had.",
        "Do you have a preferred movie genre?",
        "If you had a pet alien, what would you name it?",
        "If you could visit any fictional world, where would you go?",
        "Share a song that always cheers you up.",
        "What's the last book you read?",
        "If you could learn any new skill instantly, what would it be?",
        "If you could time travel, where and when would you go?"
    )

    def __init__(self):
        self.alienbabble = {
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*'
        }

    def greet(self):
        self.name = input("Hi! What is your name?\n")
        will_help = input(f"Hi {self.name}, I am a chatbot. How may I help you?\n")
        if will_help in self.negative_res:
            print("Alright, have a nice day!")
            return
        self.ask_all_questions()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Thanks for reaching out. Have a nice day!")
                return True

    def chat(self, question):
        reply = input(question).lower()
        return self.make_exit(reply), reply

    def ask_all_questions(self):
        for question in self.random_question:
            exit_chat, reply = self.chat(question)
            if exit_chat:
                break
            self.match_reply(reply)

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                return getattr(self, f"{intent}_response")()

        if not found_match:
            return self.no_match_intent()

    def answer_why_intent_response(self):
        responses = ("I come in peace to share knowledge and learn from your unique culture.\n",
                     "I am here to explore the wonders of your planet and forge interstellar connections.\n",
                     "I heard the cosmic coffee is unparalleled, and I'm on a quest to taste it!\n")
        print(random.choice(responses))
        self.ask_follow_up_questions("answer_why_intent")

    def about_intellipaat_response(self):
        responses = ("Intellipaat is a beacon of learning, fostering skills and expertise globally.\n",
                     "In the realm of Intellipaat, every learner's journey is a saga of empowerment.\n",
                     "Intellipaat is where dreams converge with knowledge, shaping destinies.\n")
        print(random.choice(responses))
        self.ask_follow_up_questions("about_intellipaat")

    def ask_follow_up_questions(self, intent):
        if intent == "answer_why_intent":
            follow_up_questions = [
                "How do you think our cultures can benefit from interstellar connections?",
                "What kind of knowledge would you like to share?",
                "Have you ever tasted a unique coffee blend?"
            ]
        elif intent == "about_intellipaat":
            follow_up_questions = [
                "How do you think education contributes to shaping destinies?",
                "What skills are you interested in fostering?",
                "Have you experienced the impact of continuous learning?"
            ]

        for follow_up_question in follow_up_questions:
            exit_chat, reply = self.chat(follow_up_question)
            if exit_chat:
                break
            # Additional logic for handling follow-up questions can be added here

    def no_match_intent(self):
        responses = ("Please share more details. I'm curious to know!\n", "Tell me more!\n",
                     "Okay. Can you elaborate a bit more?\n", "Fascinating! Can you provide more information?\n",
                     "Anything else you'd like to share?\n", "Okay, thank you. Goodbye!")
        print(random.choice(responses))

bot = RuleBot()
bot.greet()


# In[ ]:




