# InstagramTools
Python Scripts that automates Following/Unfollowing Instagram accounts from a given username list.
# Requirements
Selenium library was used to control a web browser into accessing Instagram.
it can be installed by:

`pip install selenium`

# Usage
After installing Selenium and your browser driver, you have to log in to your Instagram account by running the Instagram login script and pass your username and password as string arguments as following:

`python login_instagram.py "your_username" "your_password"`

## Usage
To unfollow a list of accounts, run the unfollow script by passing the usernames list directory as an argument, as follows:

`python unfollow.py "directory_of_usernames"`

Instagram gives a timeout after certain number of unfollows to prevent spamming, so the code will stop execution and saves the remaining usernames in the same given file for further use.
