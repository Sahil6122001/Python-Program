import instaloader
ig = instaloader.instaloader()
dp = input("enter user name")

ig.download_profile(dp, profile_pic_only=True)