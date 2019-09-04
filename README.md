# For the lazy unemployed ;)

## Introduction

Well, I realized something. I was too lazy to find my own internships and built my own tool for that. I was also looking for a personal project. So, why not help EVERYONE find a job or internship?! Lowkey this is useless because legit not THAT many people know how to use terminal and I mean there's Indeed or Glassdoor, but this is like a summary; you can view many job postings faster. I'm currently working on a Graphical User Interface so that it can be used like an app! Great idea, am I right???!!!

Man, I got way too bored this summer lmao

## Installation and Usage

\*\*\***NOTE**\*\*\*
This is a command line tool. This will be run on a mac's Terminal or windows' Command Prompt

### Installation

- [macOS Download](https://github.com/thenry3/Hunt-Jobs/releases/download/v1.02/HuntJobs-mac.zip)
- [Windows Download](https://github.com/thenry3/Hunt-Jobs/releases/download/v1.02/HuntJobs.exe)

### Usage and Examples

**This command must have a location parameter in order to work.**
Navigate to the directory that containts the script executable in terminal(macOS)/Command Prompt(windows)

The -h or --help flag brings up a help menu

```
macOS:  ./HuntJobs -h
windows:  HuntJobs -h
```

Simple example

```
macOS:  ./HuntJobs California
windows:  HuntJobs California
```

Search in two locations

```
macOS: ./HuntJobs California Boston
windows:  HuntJobs California Boston
```

Search in a location which has a multi-word name

```
macOS: ./HuntJobs New+York
windows:  HuntJobs New+York
```

The -k or --keywords flag allows a search with keywords

```
macOS: ./HuntJobs San+Jose Florida -k data scientist
windows:  HuntJobs San+Jose Florida -k data scientist
```

Search for only internships or only full-time positions using the -i(or --internship) and -f(--fulltime) flag respectively

```
macOS: ./HuntJobs Boston Texas -i
windows:  HuntJobs Boston Texas -f
```

**NOTE: DO NOT USE BOTH -i and -f FLAGS AT THE SAME TIME**

Print output in table format to console using -v or --verbose

```
macOS: ./HuntJobs Nevada -v
windows:  HuntJobs Nevada -v
```

Parse data into csv file by specifying path name using -c or --csv; be sure to include the .csv file extension

```
macOS: ./HuntJobs Salt+Lake+City -c foobar.csv
windows:  HuntJobs Salt+Lake+City -c foobar.csv
```

Parse data into excel file by specifying path name using -e or --excel; be sure to include the .xlsx file extension

```
macOS: ./HuntJobs Maine -e ../foobar.xlsx
windows:  HuntJobs -e ../foobar.xlsx
```

Parse data into text file by specifying path name using -t or --text

```
macOS: ./HuntJobs Colorado -t test.txt
windows:  HuntJobs Colorado -t test.txt
```

Using everything, we can do search in California, New York, and Dallas for full-time designer positions, having the output be printed on terminal, and parsed into a csv, excel, and text file.

```
macOS: ./HuntJobs California New+York -f -k designer -v -c foobar.csv -e foobar.xlsx -t foobar.txt
windows:  HuntJobs California New+York -f -k designer -v -c foobar.csv -e foobar.xlsx -t foobar.txt
```

Enjoy!

## IN DEVELOPMENT

- Email results

- User Graphical Interface/Website
