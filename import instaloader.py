import instaloader
from tqdm import tqdm


L = instaloader.Instaloader()

try:
    L.load_session_from_file("kobi_simmons")
except FileNotFoundError:

    print("Session file not found. Please log in interactivly")
    L.interactive_login("kobi_simmons")

profile = instaloader.Profile.from_username(L.context, 'kobi_simmons')


followers = set(follower.username for follower in profile.get_followers())
following = set(followee.username for followee in profile.get_followees())


not_following_back = following - followers

print("Users not following back")
for username in tqdm (not_following_back, desc="Finding users"):
    print(username)
