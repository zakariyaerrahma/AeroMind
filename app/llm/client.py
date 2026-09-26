import ollama


class LLMClient:

    def __init__(self):

        self.model = "llama3.2:3b"

    def generate_report(
        self,
        aircraft_state,
        alerts,
        knowledge
    ):

        # --------------------------------
        # Retrieved knowledge
        # --------------------------------

        knowledge_text = "\n\n".join(
            document["text"]
            for document in knowledge
        )

        # --------------------------------
        # Detected alerts
        # --------------------------------

        if alerts:

            alerts_text = "\n".join(
                f"- {alert}"
                for alert in alerts
            )

        else:

            alerts_text = "- No active alerts"

        # --------------------------------
        # Prompt
        # --------------------------------

        prompt = f"""
You are AeroMind, an AI assistant inside a
simulated aviation training environment.

Your task is to analyze a simulated aircraft situation.

IMPORTANT:
Use ONLY the information provided in:

1. Aircraft state
2. Detected alerts
3. Retrieved simulated knowledge

Do NOT use external knowledge.

Do NOT invent procedures.

Do NOT invent recommendations.

Do NOT add actions that are not supported
by the retrieved simulated knowledge.

If information is missing, explicitly write:

"Not available in the retrieved knowledge."

--------------------------------------------------
AIRCRAFT STATE
--------------------------------------------------

Aircraft ID: {aircraft_state.aircraft_id}

Altitude: {aircraft_state.altitude} ft
Speed: {aircraft_state.speed} kt
Heading: {aircraft_state.heading} degrees
Fuel: {aircraft_state.fuel} percent

Weather: {aircraft_state.weather}
Communication: {aircraft_state.communication}
Navigation: {aircraft_state.navigation}

--------------------------------------------------
DETECTED ALERTS
--------------------------------------------------

{alerts_text}

--------------------------------------------------
RETRIEVED SIMULATED KNOWLEDGE
--------------------------------------------------

{knowledge_text}

--------------------------------------------------
GENERATE THE REPORT
--------------------------------------------------

Generate a concise AI situation report using exactly
the following sections:

1. Situation Summary

Describe the current simulated aircraft state.

2. Detected Issues

List only the issues contained in the detected alerts.

3. Retrieved Simulated Procedures

Summarize only procedures that appear in the
retrieved simulated knowledge.

4. Evidence from Retrieved Knowledge

Explain which retrieved documents support the
analysis.

5. Important Limitations

Clearly state that:

- This is a simulated training environment.
- The information is not intended for real-world
  aviation operations.
- The AI must not invent procedures or recommendations.

--------------------------------------------------
STRICT RULES
--------------------------------------------------

- Do not provide real-world aviation instructions.
- Do not invent procedures.
- Do not invent recommendations.
- Do not add information that is not provided.
- Do not make assumptions about the aircraft.
- Do not prioritize one procedure over another unless
  the retrieved documents explicitly do so.
- Keep the answer grounded in the retrieved documents.
- If something is not available, say:
  "Not available in the retrieved knowledge."

This system is strictly a simulated training environment.
"""

        # --------------------------------
        # Ollama LLM
        # --------------------------------

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # --------------------------------
        # Return AI report
        # --------------------------------

        return response["message"]["content"]