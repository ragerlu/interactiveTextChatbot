#
# Author: Lucas Rager
# 
#

import random

R_FRIENDS = "I am always looking for more friends!"
R_RACISM = "I DO NOT, and will not, approve of that."
R_MEME = "I don't have memes yet, sorry!"
R_EATING = "I don't like eating anything because I'm a bot!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "What does that mean?"][
        random.randrange(4)]
    return response