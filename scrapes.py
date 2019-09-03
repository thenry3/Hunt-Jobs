import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def divNoClassNoID(tag):
    return not tag.has_attr('class') and not tag.has_attr('id') and tag.name == 'div'


def indeed(locations, keywords, jobtype):
    foundJobs = {}
    count = 0
    # search for each location given
    for location in locations:
        # parse keyword search string
        key = "q=" + "+".join(keywords) + "&" if keywords is not None else ""
        for page_num in range(0, 100, 10):
            # Get Page Data
            URL = "https://www.indeed.com/jobs?" + key + "l=" + \
                location + "&jt=" + jobtype + "&start=" + str(page_num)
            result = requests.get(URL)

            # parse HTML document
            soup = BeautifulSoup(result.text, "html.parser")
            # iterate through each posting on page
            for div in soup.find_all("div", class_="jobsearch-SerpJobCard"):
                sections = div.select('.jobsearch-SerpJobCard > div')

                title = div.find("div", class_="title").get_text().strip()
                company = div.find("span", class_="company").get_text().strip()
                city = div.find(class_="location").get_text().strip()
                age = div.find(class_="date").get_text().strip() if div.find(
                    class_="date") is not None else None
                linkindeed = None
                MetaData = None

                try:
                    # retrieve job link and parse HTML
                    linkindeed1 = re.findall('\?jk=.*?&', str(sections[0]))[0]
                    linkindeed = "https://www.indeed.com/viewjob" + linkindeed1 + "from=serp&vjs=3"
                except:
                    linkindeed = None
                else:
                    try:
                        glasspage = requests.get(linkindeed).text
                        jobsoup = BeautifulSoup(glasspage, "html.parser")

                        jobdiv = jobsoup.find(
                            class_="jobsearch-DesktopStickyContainer")

                        MetaData = jobdiv.find(
                            "span", class_="jobsearch-JobMetadataHeader-item").get_text()
                    except:
                        MetaData = None

                # add posting to dictionary of postings by company
                posting = {"job": title, "link": linkindeed,
                           "location": city, "posted": age, "meta": MetaData}
                try:
                    if posting not in foundJobs[company]:
                        foundJobs[company].append(posting)
                except:
                    foundJobs[company] = [posting]

    return foundJobs
