import json
from pathlib import Path


class ProfileLoader:

    @staticmethod
    def load_profile(profile_name):

        allowed_profiles = ["campus", "metro", "wan"]

        if profile_name not in allowed_profiles:
            raise ValueError("Invalid network profile")

        project_folder = Path(__file__).resolve().parent.parent

        file_path = project_folder / "presets" / f"{profile_name}.json"

        with open(file_path, "r") as file:
            profile_data = json.load(file)

        return profile_data