import subprocess
import json
import os

competitors = [
    "https://www.wellsaid.io",
    "https://www.descript.com",
    "https://www.resemble.ai",
    "https://play.ht",
    "https://elevenlabs.io",
    "https://murf.ai",
    "https://cloud.google.com/text-to-speech",
    "https://aws.amazon.com/polly",
    "https://learn.microsoft.com/azure/ai-services/speech",
    "https://www.ibm.com/cloud/watson-text-to-speech"
]

results = []
data_file = "data/data.json"

for url in competitors:
    print(f"Processing {url}...")
    try:
        # Run discovery_engine.py for each URL
        proc = subprocess.run(
            ["python3", "src/discovery/discovery_engine.py", url],
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout per competitor
        )
        if proc.returncode == 0:
            # The script prints some logs to stderr, so we only parse stdout
            output = proc.stdout.strip()
            # Find the JSON start
            json_start = output.find('{')
            if json_start != -1:
                competitor_data = json.loads(output[json_start:])
                results.append(competitor_data)
            else:
                print(f"No JSON found for {url}")
        else:
            print(f"Failed to process {url}: {proc.stderr}")
    except subprocess.TimeoutExpired:
        print(f"Timeout processing {url}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

# Load existing or create new data structure
final_data = {"competitors": results}

with open(data_file, "w") as f:
    json.dump(final_data, f, indent=2)

print(f"Discovery complete. Processed {len(results)} competitors into {data_file}")
