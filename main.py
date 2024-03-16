from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error retrieving transcript: {e}")
        return None

def save_transcript(transcript, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            for segment in transcript:
                text = segment['text']
                f.write(text + '\n')
        print(f"Transcript saved to {file_name}")
    except Exception as e:
        print(f"Error saving transcript: {e}")

if __name__ == "__main__":
    video_id = "9j1dZwFEJ-c"
    transcript = get_youtube_transcript(video_id)
    if transcript:
        save_transcript(transcript, f"{video_id}_transcript.txt")
