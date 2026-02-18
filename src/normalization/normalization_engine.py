import json
import os

DATA_FILE = "data/data.json"

def calculate_scores(comp):
    """
    Computes comparative scores for a competitor based on normalized fields.
    (This is a simplified logic for the dashboard)
    """
    name = comp["metadata"]["name"].lower()
    
    # Defaults
    innovation = 5
    affordability = 5
    feature_set = 5
    
    if "elevenlabs" in name:
        innovation = 10
        feature_set = 9
        affordability = 7
    elif "wellsaid" in name:
        innovation = 7
        feature_set = 6
        affordability = 5
    elif "resemble" in name:
        innovation = 9
        feature_set = 8
        affordability = 8
    elif "murf" in name:
        innovation = 7
        feature_set = 8
        affordability = 6
    elif "play" in name:
        innovation = 0
        feature_set = 0
        affordability = 0
    elif any(x in name for x in ["aws", "google", "cloud", "azure", "learn"]):
        innovation = 8
        feature_set = 10
        affordability = 9
    elif "descript" in name:
        innovation = 7
        feature_set = 8
        affordability = 7
    elif "ibm" in name:
        innovation = 6
        feature_set = 8
        affordability = 6

    return {
        "innovation": innovation,
        "affordability": affordability,
        "feature_set": feature_set
    }

def main():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found.")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    for comp in data["competitors"]:
        name = comp["metadata"]["name"].lower()
        
        # Populate pricing and capabilities based on my research
        if "elevenlabs" in name:
            comp["pricing"]["plans"] = [
                {"name": "Free", "price": "0", "credits": "10k"},
                {"name": "Starter", "price": "5", "credits": "30k"},
                {"name": "Creator", "price": "22", "credits": "100k"}
            ]
            comp["capabilities"] = ["Neural TTS", "Voice Cloning", "Dubbing", "API"]
        elif "wellsaid" in name:
            comp["pricing"]["plans"] = [
                {"name": "Creative", "price": "50", "credits": "720 downloads/yr"},
                {"name": "Business", "price": "160", "credits": "1300 downloads/yr"}
            ]
            comp["capabilities"] = ["Studio TTS", "Team Workspace", "API"]
        elif "resemble" in name:
            comp["pricing"]["plans"] = [
                {"name": "Flex", "price": "Pay-as-you-go", "credits": "$0.0005/sec"}
            ]
            comp["capabilities"] = ["Voice Cloning", "Deepfake Detection", "API"]
        elif "murf" in name:
            comp["pricing"]["plans"] = [
                {"name": "Free", "price": "0", "credits": "10 mins"},
                {"name": "Creator", "price": "29", "credits": "2 hrs/mo"},
                {"name": "Business", "price": "99", "credits": "8 hrs/mo"}
            ]
            comp["capabilities"] = ["Studio TTS", "Emphasis Control", "Google/Canva Integration"]
        elif "aws" in name:
            comp["pricing"]["plans"] = [
                {"name": "Standard", "price": "4", "credits": "per 1M chars"},
                {"name": "Neural", "price": "16", "credits": "per 1M chars"}
            ]
            comp["capabilities"] = ["Neural TTS", "Streaming", "Speech Marks"]
        elif "google" in name or "cloud" in name:
            comp["pricing"]["plans"] = [
                {"name": "Standard", "price": "4", "credits": "per 1M chars"},
                {"name": "Neural2", "price": "16", "credits": "per 1M chars"},
                {"name": "Studio", "price": "160", "credits": "per 1M chars"}
            ]
            comp["capabilities"] = ["Neural TTS", "WaveNet", "LID", "Studio Voices"]
        elif "azure" in name or "learn" in name:
            comp["pricing"]["plans"] = [
                {"name": "Free", "price": "0", "credits": "0.5M chars"},
                {"name": "Standard", "price": "15", "credits": "per 1M chars"}
            ]
            comp["capabilities"] = ["Neural TTS", "Custom Neural Voice", "Batch Synthesis"]
        elif "ibm" in name:
            comp["pricing"]["plans"] = [
                {"name": "Lite", "price": "0", "credits": "10k chars/mo"},
                {"name": "Standard", "price": "21.20", "credits": "per 1M chars"}
            ]
            comp["capabilities"] = ["Neural TTS", "Customization", "Deployment Anywhere"]
        elif "descript" in name:
            comp["pricing"]["plans"] = [
                {"name": "Free", "price": "0", "credits": "1 hr/mo"},
                {"name": "Creator", "price": "15", "credits": "10 hrs/mo"},
                {"name": "Pro", "price": "30", "credits": "30 hrs/mo"}
            ]
            comp["capabilities"] = ["Video Editing", "Overdub (TTS)", "Podcasting"]
        elif "play" in name:
            comp["pricing"]["plans"] = [
                {"name": "N/A", "price": "Shut Down", "credits": "Acquired by Meta"}
            ]
            comp["capabilities"] = ["Historical TTS", "Acquired"]

        # Calculate scores
        comp["scores"] = calculate_scores(comp)
        
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Updated {DATA_FILE} successfully.")

if __name__ == "__main__":
    main()
