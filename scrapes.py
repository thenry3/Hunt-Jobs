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
    idCache = []
    # return dictionary with jobs
    foundJobs = {}
    # glassdoor website to query jobs
    JOB_URL = "https://www.glassdoor.com/Job/jobs.htm"
    JobQueryHeaders = {
        "referer": "https://www.glassdoor.com/",
        "upgrade-insecure-requests": "1",
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    }
    # url to queyr location IDs
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
            "maxLocationsToReturn": 50
        }
        locationResponse = requests.post(
            LOCATION_URL, headers=LocationQueryHeaders, data=locationQuery)
        # iterate through each location response
        for locationData in locationResponse.json():
            jobQuery = {'clickSource': 'searchBtn', "sc.keyword": " " if keywords is None else " ".join(keywords), "locT": locationData["locationType"],
                        "locId": locationData["locationId"], "jobType": jobtype}
            jobResponse = requests.post(
                JOB_URL, headers=JobQueryHeaders, data=jobQuery)

            soup = BeautifulSoup(jobResponse.text, "html.parser")
            for jobposting in soup.find_all("li", class_="jl"):
                # for each posting, retrieve data
                company = jobposting.find(
                    "div", class_="jobHeader").get_text().strip()
                title = jobposting.find(class_="jobContainer").find(
                    "a", recursive=False).get_text().strip()
                city = jobposting.select("div.empLoc > span.loc")[
                    0].get_text().strip()
                date = jobposting.find(
                    "span", class_="jobLabel").get_text().strip()
                try:
                    salary = jobposting.find(
                        "span", class_="jobSalaryRange").get_text().strip()
                except:
                    salary = None

                # find link to job
                halfLink = re.findall(
                    '/partner.*?jobListingId=\d*', str(jobposting.find(class_="jobContainer")))[0]
                jobLink = "https://www.glassdoor.com" + halfLink

                # find job id number to keep as history
                idNum = re.findall('\d*$', halfLink)[0]

                # create JSON post
                posting = {"job": title, "link": jobLink,
                           "location": city, "posted": date, "meta": salary}

                # add posting to found jobs
                try:
                    if idNum not in idCache:
                        foundJobs[company].append(posting)
                        idCache.append(idNum)
                except:
                    foundJobs[company] = [posting]
                    idCache.append(idNum)

    return foundJobs
