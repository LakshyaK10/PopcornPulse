# import os
# import google.generativeai as genai
# import re

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_API_KEY:
#     raise ValueError("GEMINI_API_KEY is missing. Set it using: setx GEMINI_API_KEY your_api_key_here")

# genai.configure(api_key=GEMINI_API_KEY)

# model = genai.GenerativeModel("gemini-1.5-flash")

# def get_movie_recommendation(user_message: str) -> str:
#     """
#     Generates movie recommendations or motivational advice based on user input.
#     """
#     # Keywords for mood & recommendation detection
#     mood_keywords = ["sad", "depressed", "not feeling good", "anxious", "stress", "cheer up", "feeling low", "motivate me"]
#     recommendation_keywords = ["recommend", "suggest", "movie", "film", "watch", "see"]

#     user_message_lower = user_message.lower()
#     mood_related = any(word in user_message_lower for word in mood_keywords)
#     wants_movies = any(word in user_message_lower for word in recommendation_keywords)

#     print("Mood related:", mood_related)
#     print("Wants movies:", wants_movies)

#     # If user is sad but didn't ask for movies → motivational advice
#     if mood_related and not wants_movies:
#         prompt = f"""
#         The user is feeling sad or low: "{user_message}".
#         Give 3-4 positive, motivating, and supportive suggestions.
#         Do NOT recommend movies here.
#         """
#     else:
#         prompt = f"""
#         The user asked: "{user_message}".
#         Recommend 3-5 movies based on their mood.
#         Respond strictly in this format:
#         - Title (Genre) - IMDb: Rating : Short description
#         Example:
#         - Inception (Sci-Fi) - IMDb: 8.8 : A mind-bending thriller about dream invasion.
#         Also give 1-2 motivational lines if the mood is low.
#         """

#     try:
#         # ✅ Generate response from Gemini
#         response = model.generate_content(prompt)
#         response_text = response.text.strip()
#         print("Final response:", response_text)
#         return response_text
#     except Exception as e:
#         print(f"Error in Gemini API: {e}")
#         return "Sorry, something went wrong while fetching recommendations."

# def parse_response(response_text):
#     """
#     Parses Gemini's response and extracts structured movie data.
#     """
#     movies = []
#     lines = response_text.strip().split('\n')
#     for line in lines:
#         match = re.match(r"-\s*(.*?)\s*\((.*?)\)\s*-\s*IMDb:\s*(\d+\.?\d*)\s*:\s*(.*)", line)
#         if match:
#             title, genre, rating, description = match.groups()
#             movies.append({
#                 "title": title.strip(),
#                 "genre": genre.strip(),
#                 "rating": rating.strip(),
#                 "description": description.strip()
#             })
#     return movies

# def get_movie_details(movie_title: str) -> str:
#     """
#     Fetches static movie details (replace later with OMDB API).
#     """
#     movie_details = {
#         "Inception": "Inception (2010): Directed by Christopher Nolan, Inception is a mind-bending sci-fi thriller that explores the concept of shared dreams. IMDb: 8.8",
#         "The Matrix": "The Matrix (1999): A groundbreaking sci-fi movie exploring simulated reality. IMDb: 8.7"
#     }
#     return movie_details.get(movie_title, "Sorry, I don't have more details on that movie.")


