from Subscription import Subscription


class Account:
    def __init__(self, username: str, password: str, subscription: Subscription):
        self.username = username
        self.password = password
        self.subscription = subscription
        self.profiles = {}

    def create_profile(self, profile_name: str):
        if profile_name not in self.profiles:
            self.profiles[profile_name] = {"watched_movies": []}
            print(f"Profile '{profile_name}' has been created.")
        else:
            print(f"Profile '{profile_name}' already exists.")

    def delete_profile(self, profile_name: str):
        if profile_name in self.profiles:
            del self.profiles[profile_name]
            print(f"Profile '{profile_name}' has been deleted.")
        else:
            print(f"Profile '{profile_name}' does not exist.")

    def list_profiles(self):
        if self.profiles:
            print("List of profiles:")
            for profile_name in self.profiles:
                print(f"- {profile_name}")
        else:
            print("No profiles found for this account.")

    def watch_movie(self, profile_name: str, movie_title: str):
        if profile_name in self.profiles:
            self.profiles[profile_name]["watched_movies"].append(movie_title)
            print(f"{movie_title} has been added to {profile_name}'s watched movies.")
        else:
            print(f"Profile '{profile_name}' does not exist.")

    def get_watched_movies(self, profile_name: str):
        if profile_name in self.profiles:
            return self.profiles[profile_name]["watched_movies"]
        else:
            print(f"Profile '{profile_name}' does not exist.")
