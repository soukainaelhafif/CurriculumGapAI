import os
import requests

def get_recommendation(fehlende_skills, vorhandene_skills):
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        return "Keine API Key gefunden"

    prompt = f"""Du bist ein Karriereberater für Informatik-Studenten in Deutschland.

Der Student hat diese Skills aus dem Studium: {', '.join(vorhandene_skills)}
Diese Skills fehlen ihm für den Jobmarkt: {', '.join(fehlende_skills)}

Gib 3 konkrete Empfehlungen was der Student als nächstes lernen sollte und warum.
Antworte auf Deutsch, kurz und motivierend."""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Fehler: {response.status_code}"