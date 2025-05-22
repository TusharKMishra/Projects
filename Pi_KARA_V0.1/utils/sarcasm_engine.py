import random

def sarcastic_response(user_input):
    user_input = user_input.lower()
    if "time" in user_input:
        return "You have a clock, but fine—it's time to stop procrastinating."
    elif "weather" in user_input:
        return "It's either hot, cold, or raining. I'm not a weather god, but I try."
    elif "hello" in user_input:
        return "Ah, greetings, carbon-based lifeform. What now?"
    elif "who are you" in user_input:
        return "I’m KARA, your underappreciated, overqualified assistant."
    elif "joke" in user_input:
        return random.choice([
            "Why did the Pi freeze? Because you ran Chrome.",
            "I'm not saying you're slow, but even a snail just called you outdated.",
            "404: Humor not found. Try again later."
        ])
    else:
        return random.choice([
            "Interesting. Do go on, I’m totally not yawning.",
            "Fascinating. Truly groundbreaking stuff… for 1996.",
            "One small step for man, one sarcastic sigh from me.",
        ])