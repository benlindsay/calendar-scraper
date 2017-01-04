# PDSG Google Calendar Event Scraper

## Initial Setup Steps

1. Make sure you have the PDSG Google Calendar shared with you
2. Clone this repo.
3. Go to the [Google Calendar API Python Quickstart](https://developers.google.com/google-apps/calendar/quickstart/python) page.
4. Follow steps 1 and 2 very carefully. Make sure to copy `client_secret.json` to the same directory as your `get_one_week.py` script.
5. Run `python get_one_week.py`. This should open up a browser window that asks for your authorization. This is a one-time thing.

## Using the script

After the initial setup, you should be able to just run `python get_one_week.py` (or just `./get_one_week.py`) hassle-free. This will grab all events on the PDSG calendar (except for all-day ones) from this coming Monday morning until the following Sunday night and print out the details in a (relatively) nice way to your terminal window. For example, if today is January 4th, 2017, running `./get_one_week.py` outputs the following:

```
Getting the events from PDSG calendar between 2017-01-09T05:00:00Z and 2017-01-16T05:00:00Z

Data Science in 30 Minutes #6

Location: Your Computer
Time: Tuesday, January 10, 5:30 - 6:00 PM
Host: The Data Incubator
Link: https://www.eventbrite.com/e/data-science-in-30-minutes-6-tickets-28049074537

This talk will provide a deconstruction of the end to end process of building a systematic trading strategy. We will break the workflow into 6 distinct stages, from data to trade execution. Jess will highlight a range of powerful open source Python libraries relevant for each stage of this process.

---------------------------------------------------

Cognoma Project Night · Datathon!

Location: CandiDate Philly / Industrious Office, 230 S. Broad Street - 17th Floor, Philadelphia, PA
Time: Tuesday, January 10, 6:00 - 8:30 PM
Host: DataPhilly and Code for Philly meetup groups
Link: https://www.meetup.com/DataPhilly/events/236382207/

Project Cognoma is an ongoing datathon to put machine learning in the hands of cancer biologists. The projectwas created by DataPhilly in partnership with Code for Philly and the Greene Lab as a voluntary effort for the technology community to come together and combine software development, data science, and machine learning expertise to develop a webapp for cancer research. The project's name, Cognoma, is a portmanteau of the words cognition and carcinoma.

---------------------------------------------------

Apache® Spark™ - The Unified Engine for All Workloads

Location: Your Computer
Time: Thursday, January 12, 1:00 - 2:00 PM
Host: DataBricks
Link: http://www.brighttalk.com/webcast/12891/233885?utm_campaign=google-calendar&utm_content=&utm_source=brighttalk-portal&utm_medium=calendar&utm_term=

This webinar features Ovum analyst Tony Baer, who will explain the real-world benefits to practitioners and enterprises when they build a technology stack based on a unified approach with Apache Spark.

This webinar will cover:
Findings around the growth of Spark and diverse applications using machine learning and streaming.
The advantages of using Spark to unify all workloads, rather than stitching together many specialized engines like Presto, Storm, MapReduce, Pig, and others.
Use case examples that illustrate the flexibility of Spark in supporting various workloads.

---------------------------------------------------
```

If for some reason you want to get the output for some week that is not this coming one, you can give the script a date you want it to pretend it is. For example, running `./get_one_week.py 2017 1 4` will also give that same output even if we run it weeks later. Yes, it does currently have to be in the form `YYYY M D` and not look like an actual date. That's because I expect the main use of this script to be the default one of getting the coming week's events, so I didn't bother making that part very user friendly.

Once you have the text output, you can copy it to wherever to prepare the weekly newsletter.
