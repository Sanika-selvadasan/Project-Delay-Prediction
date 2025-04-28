# Project Delay Prediction and Mitigation Assistant

Tired of project deadlines slipping through your fingers like sand?
Meet your new AI sidekick: Project Delay Prediction and Mitigation Assistant! 🦸‍♂️

This app doesn't just predict whether your project tasks will fall behind  it also suggests clever strategies to keep everything on track.
Powered by a Random Forest classifier and the mighty LLaMA 3 via the Groq API, it combines machine learning prediction with LLM-driven actionable advice.
All wrapped in a slick and simple Streamlit UI!


## Merits:
Accurate Delay Predictions: Uses a trained Random Forest model to predict overdue tasks based on risk, priority, hours, delay, and root cause.

Smart Mitigation Suggestions: Integrates an LLM to generate practical and understandable strategies to address potential delays.

User-Friendly: Built with Streamlit  making it easy for non-technical users to interact with.

Real-time Analysis: Instant predictions and advice after user input  no waiting around!

Customizable: Easy to plug in new models or update the LLM prompt for different use cases.

## Demerits:
Model Simplicity: Random Forest may not capture complex sequential or temporal project dynamics like time-series models would.

Static Encoders: LabelEncoders are trained on initial data  new unseen categories at runtime could cause errors unless handled.

Limited Root Cause Analysis: Root cause input is text-based and manually entered, which might lead to inconsistencies if not standardized.

Dependency on API Key: Requires a valid Groq API key to fetch mitigation strategies; otherwise, suggestions won't work.



