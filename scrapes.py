import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def indeed(locations, keywords, jobtype):
    def divNoClassNoID(tag):
        return not tag.has_attr('class') and not tag.has_attr('id') and tag.name == 'div'
    foundJobs = {}
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

                # parse data for job title, company, location, and date posting
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


def glassdoor(locations, keywords, jobtype):
    foundJobs = {}
    JOB_URL = "https://www.glassdoor.com/Job/jobs.htm"
    JobQueryHeaders = {
        "referer": "https://www.glassdoor.com/",
        "upgrade-insecure-requests": "1",
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    }
    LOCATION_URL = "https://www.glassdoor.co.in/findPopularLocationAjax.htm?"
    LocationQueryHeaders = {
        "referer": "https://www.glassdoor.com/",
        "upgrade-insecure-requests": "1",
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
        "Cache-Control": "no-cache",
        "Conncection": "keep-alive"
    }
    for location in locations:
        locationQuery = {
            "term": location.replace("+", " "),
            "maxLocationsToReturn": 10
        }
        locationResponse = requests.post(
            LOCATION_URL, headers=LocationQueryHeaders, data=locationQuery)
        for locationData in locationResponse.json():
            jobQuery = {'clickSource': 'searchBtn', "sc.keyword": " " if keywords is None else " ".join(keywords), "locT": locationData["locationType"],
                        "locID": locationData["locationId"], "jobType": ""}
            jobResponse = requests.post(
                JOB_URL, headers=JobQueryHeaders, data=jobQuery)
            soup = BeautifulSoup(jobResponse.text, "html.parser")
            print(soup.prettify())

    return 0
