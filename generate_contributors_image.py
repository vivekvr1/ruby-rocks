import datetime
import github
import matplotlib.pyplot as plt

# Replace with your personal access token
personal_access_token = "YOUR_PERSONAL_ACCESS_TOKEN"

# Repository information
repository_owner = "vivekvr1"
repository_name = "ruby-rocks"

# Get repository object
g = github.Github(personal_access_token)
repo = g.get_repo(f"{repository_owner}/{repository_name}")

# Get contributors for the specified period
start_date = datetime.date(2022, 11, 30)
end_date = datetime.date(2023, 10, 18)
contributors = repo.get_contributors(since=start_date, until=end_date)

# Generate a bar chart of contributors
contributor_names = [c.name for c in contributors]
contribution_counts = [c.contributions for c in contributors]

plt.figure(figsize=(10, 5))
plt.bar(contributor_names, contribution_counts)
plt.xlabel("Contributors")
plt.ylabel("Contributions")
plt.title("Contributors for 2022-11-30 to 2023-10-18")

# Save the image as 'contributors.png'
plt.savefig("contributors.png")
