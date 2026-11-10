from engine.profile_loader import ProfileLoader


def main():

    print("=" * 45)
    print("       NETARCHITECT")
    print("   NETWORK PROFILE SELECTION")
    print("=" * 45)

    print("\n1. Campus LAN")
    print("2. Metro MAN")
    print("3. Global WAN")

    choice = input("\nSelect network profile (1/2/3): ")

    profiles = {
        "1": "campus",
        "2": "metro",
        "3": "wan"
    }

    if choice not in profiles:
        print("Invalid selection. Please choose 1, 2 or 3.")
        return

    profile_name = profiles[choice]

    profile = ProfileLoader.load_profile(profile_name)

    print("\n--- SELECTED NETWORK PROFILE ---")
    print(f"Profile: {profile['profile']}")

    print("\n--- PROFILE DETAILS ---")

    for key, value in profile.items():
        print(f"{key}: {value}")

    print("\nNetwork profile loaded successfully!")


if __name__ == "__main__":
    main()