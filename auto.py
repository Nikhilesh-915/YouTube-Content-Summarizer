import os
import streamlit as st
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import hashlib
import functools
from transformers import pipeline
import base64

# Set up API credentials from environment variables
youtube_api_key = os.getenv("YOUTUBE_API_KEY")

# Initialize YouTube API
youtube = None
if youtube_api_key:
    youtube = build("youtube", "v3", developerKey=youtube_api_key)
else:
    st.error(
        "YouTube API key not found. Please set the YOUTUBE_API_KEY environment variable."
    )

# Predefined content sources
youtube_channel_ids = ["UCoch_d78Aosmp14ey1HgGSQ", "UCPGrgwfbkjTIgPoOh2q1BAg"]

# Initialize the summarization model from transformers
summarizer = pipeline("summarization", model="t5-small", device=-1)


# Cache for YouTube summaries to avoid redundant API calls and summarization
@functools.lru_cache(maxsize=32)
def generate_summary(text):
    # Limit the text to a reasonable length to avoid long processing times
    text = text[:2000]
    try:
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0][
            "summary_text"
        ]
        return summary
    except Exception as e:
        return f"Failed to generate summary: {str(e)}"


# Fetch latest videos from YouTube
def fetch_youtube_videos():
    if not youtube_api_key:
        return []
    summaries = []
    for channel_id in youtube_channel_ids:
        try:
            request = youtube.search().list(
                part="snippet",
                channelId=channel_id,
                maxResults=1,  # Reduce the number of videos to fetch to speed up processing
                order="date",
            )
            response = request.execute()
            for item in response["items"]:
                video_title = item["snippet"]["title"]
                video_id = item["id"]["videoId"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"

                try:
                    transcript = YouTubeTranscriptApi.get_transcript(video_id)
                    transcript_text = " ".join([entry["text"] for entry in transcript])
                    cache_key = hashlib.md5(transcript_text.encode()).hexdigest()
                    summary = generate_summary(transcript_text)
                    summaries.append(
                        {"title": video_title, "summary": summary, "url": video_url}
                    )
                except Exception as e:
                    summaries.append(
                        {
                            "title": video_title,
                            "summary": f"Failed to retrieve transcript: {str(e)}",
                            "url": video_url,
                        }
                    )
        except Exception as e:
            summaries.append(
                {"title": "Error fetching data", "summary": str(e), "url": "#"}
            )
    return summaries


# Streamlit app
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpg;base64,{base64.b64encode(open('backgrounds.jpg', 'rb').read()).decode()}');
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("✨ YouTube Content Summarizer")
st.write(
    "This application fetches and summarizes the latest posts from predefined YouTube channels."
)

# Display YouTube summaries
st.header("YouTube Summaries")
youtube_summaries = fetch_youtube_videos()
for video in youtube_summaries:
    st.subheader(video["title"])
    st.write(video["summary"])
    st.markdown(f"[Watch video]({video['url']})")

# Custom animation for footer
with st.spinner("Fetching the latest summaries..."):
    st.success("Summaries loaded successfully!")
