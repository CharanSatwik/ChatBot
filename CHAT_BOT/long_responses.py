import random

r_eating = "Maybe RAM because I am a bot."
r_advice = "The internet is the best place for advices."
r_anime = "Naruto is the best anime."
def unknown():
    response = ["Could you please re-phrase that?",
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response