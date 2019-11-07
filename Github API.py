import requests
import json
import pygal
from pygal.style import  LightColorizedStyle as LCS, LightStyle as LS
from github import Github
import getpass



def start():
        access = False
        while (not access):
            username = input("Please put in your username: ")
            password = getpass.getpass("Please input your password: ")
            try:
                g = Github(username, password)
                access = True
            except:
                print("Incorrect details try again")

        error = True
        while (error):
            try:
                repo_to_use = input("Please put in the git repo you wish to interrogate: ")
                repo = g.get_repo(repo_to_use)
                error = False
            except:
                print("Incorrect repo please try again")
        return repo



def getTheContributors(repo):
    repo_contributors = []
    repo_contributions = []
    contributors = repo.get_contributors()
    print("Preparing to print the contributors and each of their contributions:")
    for contributor in contributors:
            name = str(contributor.name)
            contributionTime = str(contributor.contributions)
            if name != "None":
                if contributionTime != "None":
                   print("Contributor:" + str(name)+"  Contribution:"+ str(contributionTime))
                   repo_contributors.append(contributor)
                   repo_contributions.append(contributionTime)
    # returns contributors in a list

    return repo_contributors,repo_contributions






repo=start()
(contributors,contributions) = getTheContributors(repo)
print("\nThe contributors who gives the most contribution is " +contributors[0].name+" and his/her contribution time is:"+contributions[0])


my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = contributors.name
chart.add('', contributions)
chart.render_to_file('python_repos.svg')
