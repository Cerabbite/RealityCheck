# OpenAI Prompt
OpenAI will be used to process the tags produced by [betafaceapi](https://www.betafaceapi.com/demo.html)
To do this, the `gpt-3.5-turbo` model will be used.

`OpenAI-Prompt.py` uses demo-persona.json as mock data. Betafaceapi provides the same structure data.

### System Prompt
The following system prompt is used to assure correct format.
```
You will only be given tags about someones face with a yes or no value.
Based on these values, give 5 compliments and 5 roasts, format these in 2 lists, not markdown.
Do not add extra text.
The roasts must be mean and the compliments must be nice.
```

### User Prompt
The provided data by [betafaceapi](https://www.betafaceapi.com/demo.html) is in json format. This must be converted to a single string.
Example:
```yaml
5oclock shadow: no (83%), age: 27 (60%), arched eyebrows: no (81%), attractive: no (92%), bags under eyes: yes (21%), bald: no (21%), bangs: no, beard: no, big lips: no (61%), big nose: yes (30%), black hair: no (3%), blond hair: no (92%), blurry: no (9%), brown hair: no (5%), bushy eyebrows: no (31%), chubby: yes (43%), double chin: yes (26%), expression: smile (96%), gender: male (25%), glasses: yes, goatee: no, gray hair: no (31%), heavy makeup: no (88%), high cheekbones: yes, mouth open: yes, mustache: no (96%), narrow eyes: yes (4%), oval face: yes (62%), pale skin: no (96%), pitch: -9.84, pointy nose: no, race: white, receding hairline: yes (22%), rosy cheeks: no (80%), sideburns: no, straight hair: yes (65%), wavy hair: no, wearing earrings: no (30%), wearing hat: no (79%), wearing lipstick: no (80%), wearing necklace: no (67%), wearing necktie: no (6%), yaw: 4.32, young: no (16%),
```

## Sample output
This is a sample output using mock data.
```md
Compliments:
1. You have a beautiful smile that lights up your whole face.
2. Your high cheekbones give you such a sharp and attractive look.
3. Your oval face shape is very aesthetically pleasing.
4. Your straight hair complements your features perfectly.
5. Your expression exudes warmth and positivity.

Roasts:
1. Those bags under your eyes make you look like you haven't slept in years.
2. Your double chin is stealing all the attention from the rest of your features.
3. Your big nose is really standing out in all the wrong ways.
4. Your chubby cheeks make you look like a chipmunk storing up for winter.
5. Your receding hairline is a clear sign that Father Time is catching up to you.
```