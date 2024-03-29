import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from betaface import get_facial_features

load_dotenv()
client = OpenAI()




def get_compliments_and_roasts(img_url):
    code, facial_features = get_facial_features(img_url)
    if code != 0:
        # Todo: Add better error handling
        print(f"Error occured with code: {code}")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1.0,
        max_tokens=4096,  # max tokens 3.5-turbo can handle
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are giving people a reality check. Roast them based on 5 aspects, and also compliment them based on 5 aspects. The output should be in json format.",
            },
            {
                "role": "user",
                "content": "5oclock shadow: no (83%), age: 27 (60%), arched eyebrows: no (81%), attractive: no (92%), bags under eyes: yes (21%), bald: no (21%), bangs: no, beard: no, big lips: no (61%), big nose: yes (30%), black hair: no (3%), blond hair: no (92%), blurry: no (9%), brown hair: no (5%), bushy eyebrows: no (31%), chubby: yes (43%), double chin: yes (26%), expression: smile (96%), gender: male (25%), glasses: yes, goatee: no, gray hair: no (31%), heavy makeup: no (88%), high cheekbones: yes, mouth open: yes, mustache: no (96%), narrow eyes: yes (4%), oval face: yes (62%), pale skin: no (96%), pitch: -9.84, pointy nose: no, race: white, receding hairline: yes (22%), rosy cheeks: no (80%), sideburns: no, straight hair: yes (65%), wavy hair: no, wearing earrings: no (30%), wearing hat: no (79%), wearing lipstick: no (80%), wearing necklace: no (67%), wearing necktie: no (6%), yaw: 4.32, young: no (16%)",
            },
            {
                "role": "assistant",
                "content": "Compliments: (You have a beautiful smile that lights up your whole face. Your high cheekbones give you such a sharp and attractive look. Your oval face shape is very aesthetically pleasing. Your straight hair complements your features perfectly. Your expression exudes warmth and positivity). Roasts: (Those bags under your eyes make you look like you haven't slept in years. Your double chin is stealing all the attention from the rest of your features. Your big nose is really standing out in all the wrong ways. Your chubby cheeks make you look like a chipmunk storing up for winter. Your receding hairline is a clear sign that Father Time is catching up to you.)",
            },
            # Line 18 is for testing, Line19 is for user input
            # {
            #    "role": "user",
            #    "content": "5oclock shadow: no (22%), age: 15 (60%), arched eyebrows: no (45%), attractive: yes (32%), bags under eyes: no (37%), bald: no (80%), bangs: no (87%), beard: no (77%), big lips: no (43%), big nose: no (17%), black hair: yes (89%), blond hair: no (99%), blurry: no, brown hair: no (92%), bushy eyebrows: yes (84%), chubby: no (47%), double chin: no (75%), expression: neutral (88%), gender: male (96%), glasses: no, goatee: no, gray hair: no, heavy makeup: no (89%), high cheekbones: no (90%), mouth open: no (97%), mustache: no (85%), narrow eyes: no, oval face: yes (63%), pale skin: yes (3%), pitch: -10.1, pointy nose: no (79%), race: white (88%), receding hairline: no (37%), rosy cheeks: no, sideburns: no, straight hair: yes (93%), wavy hair: no, wearing earrings: no (70%), wearing hat: no (84%), wearing lipstick: no (89%), wearing necklace: no, wearing necktie: yes (46%), yaw: -0.51, young: yes (94%),",
            # },
            {"role": "user", "content": facial_features}
        ],
    )

    response_content = response.choices[0].message.content

    response_data = json.loads(response_content)

    # Extract compliments and roasts
    compliments = response_data.get("Compliments", {})
    roasts = response_data.get("Roasts", {})

    both = compliments.copy()
    both.update(roasts)

    return compliments, roasts
