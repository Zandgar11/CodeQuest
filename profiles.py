import json
import os

PROFILE_DIR = 'data/profiles/'

def ensure_profile_dir_exists():
    if not os.path.exists(PROFILE_DIR):
        os.makedirs(PROFILE_DIR)

def load_profile(player_name):
    ensure_profile_dir_exists()
    profile_path = os.path.join(PROFILE_DIR, f"{player_name}.json")
    if os.path.exists(profile_path):
        with open(profile_path, 'r') as f:
            return json.load(f)
    else:
        return create_profile(player_name)

def save_profile(profile):
    ensure_profile_dir_exists()
    profile_path = os.path.join(PROFILE_DIR, f"{profile['name']}.json")
    with open(profile_path, 'w') as f:
        json.dump(profile, f)

def create_profile(player_name):
    profile = {
        'name': player_name,
        'progress': 0,
        'score': 0
    }
    save_profile(profile)
    return profile
