import instaloader
from tqdm import tqdm


L = instaloader.Instaloader()

try:
    L.load_session_from_file(" insert account name")
except FileNotFoundError:

    print("Session file not found. Please log in interactivly")
    L.interactive_login("insert account name")

profile = instaloader.Profile.from_username(L.context, 'insert account name')


followers = set(follower.username for follower in profile.get_followers())
following = set(followee.username for followee in profile.get_followees())


not_following_back = following - followers

print("Users not following back")
for username in tqdm (not_following_back, desc="Finding users"):
    print(username)
