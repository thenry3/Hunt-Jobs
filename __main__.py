import argparse
import scrapes
from enum import Enum
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search multiple job sites for jobs/internships")

    jobtype = parser.add_mutually_exclusive_group()
    jobtype.add_argument("-i", "--internship", action="store_true",
                         help="search only for internships")
    jobtype.add_argument("-f", "--fulltime", action="store_true",
                         help="search only for full time positions")

    parser.add_argument("locations", metavar="L", nargs="+",
                        help="location(s) to search for a job -- use '+' as a space between multiword locations")
    parser.add_argument("-k", "--keywords", nargs="+", dest='keywords',
                        help="search for jobs with keywords")

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="print results of query into terminal/console")
    parser.add_argument("-c", "--csv", dest='csv_dest',
                        help="specify file path to create a csv file")
    parser.add_argument("-e", "--excel", dest='excel_dest',
                        help="specfiy file path to create an excel file")
    parser.add_argument("-t", "--text", dest="text_dest",
                        help="specify file path to create a text file")

    args = parser.parse_args()
    df = pd.DataFrame(columns=["Company", "Job Title",
                               "Link", "Location", "Posted", "Notes"])
    JobType = "internship" if args.internship else "fulltime" if args.fulltime else ""
    keywords = args.keywords if args.keywords is not None else [""]

    # run through glassdoor and indeed
    glassdoorJobs = scrapes.glassdoor(args.locations, args.keywords, JobType)
    indeedJobs = scrapes.indeed(args.locations, args.keywords, JobType)

    index = 0
    for company in indeedJobs:
        for post in indeedJobs[company]:
            df.loc[index] = [company, post["job"], post["link"],
                             post["location"], post["posted"], post["meta"]]
            index += 1

    for company in glassdoorJobs:
        for post in glassdoorJobs[company]:
            df.loc[index] = [company, post["job"], post["link"],
                             post["location"], post["posted"], post["meta"]]
            index += 1

    if args.csv_dest:
        df.to_csv(args.csv_dest, index=False)

    if args.excel_dest:
        df.to_excel(args.excel_dest, index=False)

    if args.text_dest:
        print(df.to_string(index=False), file=open(args.text_dest, "w"))

    if args.verbose:
        print(df.to_string(index=False))
