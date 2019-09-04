# For the lazy unemployed ;)

## Introduction

Well, I realized something. I was too lazy to find my own internships and built my own tool for that. I was also looking for a personal project. So, why not help EVERYONE find a job or internship?! Lowkey this is useless because legit not THAT many people know how to use terminal and I mean there's Indeed or Glassdoor, but this is like a summary; you can view many job postings faster. I'm currently working on a Graphical User Interface so that it can be used like an app! Great idea, am I right???!!!

Man, I got way too bored this summer lmao

## Installation and Usage

**NOTE**
As of 9/3/2019, this script is Unix-based -- only macOS may run this.

### Installation

1. [Click to Download!](https://github.com/thenry3/Hunt-Jobs/releases/download/v1.0/HuntJobs)
   Or go to this [link](https://github.com/thenry3/Hunt-Jobs/releases) or click on the "releases" tab above and download the file there.

2. Click and download the executable named `HuntJobs`

3. In terminal, enter the command `chmod +x FILE_PATH_NAME`

### Usage

This command must have a location parameter in order to work.

The -h or --help flag brings up a help menu

```
./HuntJobs.dms -h
```

Simple example

```
./HuntJobs.dms California
```

Search in two locations

```
./HuntJobs.dms California Boston
```

Search in a location which has a multi-word name

```
./HuntJobs.dms New+York
```

The -k or --keywords flag allows a search with keywords

```
./HuntJobs.dms San+Jose Florida -k data scientist
./HuntJobs.dms Seattle -k Microsoft software engineer
```

Search for only internships or only full-time positions using the -i(or --internship) and -f(--fulltime) flag respectively

```
./HuntJobs.dms Los+Angeles -i
./HuntJobs.dms Boston Texas -f -k financial analyst \n
./HuntJobs.dms Dallas -i
```

**NOTE: DO NOT USE BOTH -i and -f FLAGS AT THE SAME TIME**

Print output in table format to console using -v or --verbose

```
./HuntJobs.dms Nevada -v
```

Parse data into csv file by specifying path name using -c or --csv; be sure to include the .csv file extension

```
./HuntJobs.dms Salt+Lake+City -c foobar.csv
```

Parse data into excel file by specifying path name using -e or --excel; be sure to include the .xlsx file extension

```
./HuntJobs.dms Maine -e ../foobar.xlsx
```

Parse data into text file by specifying path name using -t or --text

```
./HuntJobs.dms Colorado -t test.txt
```

Using everything, we can do search in California, New York, and Dallas for full-time designer positions, having the output be printed on terminal, and parsed into a csv, excel, and text file.

```
./HuntJobs.dms California New+York -f -k designer --verbose -c foobar.csv -e ../foobar.xlsx -t ~/Documents/foobar.txt
```

Enjoy!

## IN DEVELOPMENT

- Email results

- User Graphical Interface/Website
