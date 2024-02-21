from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    temperature = 2.0, #allows for max creativity
    max_tokens = 4096, #max tokens 3.5-turbo can handle
    response_format = {"type": "json_object"},
    messages = [{"role": "system", "content": "You are giving people a reality check. Roast them based on 5 aspects, and also compliment them based on 5 aspects. The output should be in json format."},
                {"role": "user", "content": "5oclock shadow: no (83%), age: 27 (60%), arched eyebrows: no (81%), attractive: no (92%), bags under eyes: yes (21%), bald: no (21%), bangs: no, beard: no, big lips: no (61%), big nose: yes (30%), black hair: no (3%), blond hair: no (92%), blurry: no (9%), brown hair: no (5%), bushy eyebrows: no (31%), chubby: yes (43%), double chin: yes (26%), expression: smile (96%), gender: male (25%), glasses: yes, goatee: no, gray hair: no (31%), heavy makeup: no (88%), high cheekbones: yes, mouth open: yes, mustache: no (96%), narrow eyes: yes (4%), oval face: yes (62%), pale skin: no (96%), pitch: -9.84, pointy nose: no, race: white, receding hairline: yes (22%), rosy cheeks: no (80%), sideburns: no, straight hair: yes (65%), wavy hair: no, wearing earrings: no (30%), wearing hat: no (79%), wearing lipstick: no (80%), wearing necklace: no (67%), wearing necktie: no (6%), yaw: 4.32, young: no (16%)"},
                {"role": "assistant", "content": "Compliments: (You have a beautiful smile that lights up your whole face. Your high cheekbones give you such a sharp and attractive look. Your oval face shape is very aesthetically pleasing. Your straight hair complements your features perfectly. Your expression exudes warmth and positivity). Roasts: (Those bags under your eyes make you look like you haven't slept in years. Your double chin is stealing all the attention from the rest of your features. Your big nose is really standing out in all the wrong ways. Your chubby cheeks make you look like a chipmunk storing up for winter. Your receding hairline is a clear sign that Father Time is catching up to you.)"}
                ]
)

print(response.choices[0].message.content)
# To get the content from the response use: print(response.choices[0].message.content)