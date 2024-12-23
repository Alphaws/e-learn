import openai

openai.api_key = "your_openai_api_key"  # Az OpenAI kulcsod

def generate_description(title, language="en"):
    prompt = f"Write a detailed description for a roadmap stage titled '{title}' in {language}."
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # vagy más modell
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating description: {e}")
        return "Description generation failed."
