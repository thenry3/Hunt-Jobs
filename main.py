import argparse
import scrapes
from enum import Enum

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

    args = parser.parse_args()

    JobType = "internship" if args.internship else "fulltime" if args.fulltime else ""
    indeedJobs = scrapes.indeed(args.locations, args.keywords, JobType)
    print(len(indeedJobs))
