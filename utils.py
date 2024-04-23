from portkey_ai import Portkey
import streamlit as st
# Set up Portkey API key
PORTKEY_API_KEY = st.secrets["PORTKEY_API_KEY"]

teach_tel2hin = """
Teach me a new sentence in Telugu

The output should be in the below format. Use it as reference:

-----
Sentence: Nuvvu ela unnavu?
Meaning: Tum kaise ho? ## explain in Hindi
Explanation: 'Nuvvu' means tum; 'ela' means kaise; 'unnavu' means ho
Nuances: 'Nuvvu' is a singular form - 'Meeru' is a plural form
------

P.S. Don't mention Telugu Script in the output
"""

teach_tel2eng = ("""
Teach me a new sentence in Telugu

The output should be in the below format. Use it as reference:

--------
Sentence: Nuvvu ela unnavu?
Meaning: How are you?
Explanation: 'Nuvvu' means you; 'ela' means how; 'unnavu' means there
Nuances: 'Nuvvu' is a singular form - 'Meeru' is a plural form
---------

P.S. Don't mention Telugu Script in the output
""")

def explain_prompt(sentence):
    explain_prompt_template = f"""
    Teach me how to say '{sentence}' in Telugu

    The output should be in the following format. Use it as a reference:

    --------
    Sentence: Nuvvu ela unnavu?
    Meaning: How are you?
    Explanation: 'Nuvvu' means you; 'ela' means how; 'unnavu' means there
    Nuances: 'Nuvvu' is a singular form - 'Meeru' is a plural form
    ---------

    P.S. Don't mention Telugu Script in the output
    """
    return explain_prompt_template

def run_app(query=None, provider_vk = "anthropic-9e8db9", model_name = 'claude-3-sonnet-20240229' ):

    if query:
      prompt = explain_prompt(query)
    else:
      prompt = teach_tel2eng

    # Assuming PORTKEY_API_KEY is defined in your environment or passed as an argument
    portkey = Portkey(
        api_key=PORTKEY_API_KEY,
        virtual_key= provider_vk,
    )

    response = portkey.chat.completions.create(
        messages=[{"role": 'user', "content": prompt}],
        model= model_name,
        max_tokens=500,
        temperature=1.0
    )

    return response.choices[0].message.content




def format_telugu_sentence(sentence):
    lines = sentence.strip().split('\n')
    formatted_sentence = '<div class="telugu-explanation-container">'
    
    for line in lines:
        if line.startswith('Sentence:'):
            formatted_sentence += f'<div class="telugu-sentence"><div class="side-heading">Telugu Sentence:</div>{line[9:].strip()}</div>'
        elif line.startswith('Meaning:'):
            formatted_sentence += f'<div class="telugu-meaning"><div class="side-heading">Meaning:</div>{line[8:].strip()}</div>'
        elif line.startswith('Explanation:'):
            formatted_sentence += f'<div class="telugu-explanation"><div class="side-heading">Explanation:</div>{line[12:].strip()}</div>'
        elif line.startswith('Nuances:'):
            formatted_sentence += f'<div class="telugu-nuance"><div class="side-heading">Nuances:</div>{line[8:].strip()}</div>'
    
    formatted_sentence += '</div>'
    return formatted_sentence