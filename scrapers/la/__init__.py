from utils import url_xpath
from openstates.scrape import State
from .events import LAEventScraper
from .bills import LABillScraper


class Louisiana(State):
    scrapers = {
        "events": LAEventScraper,
        "bills": LABillScraper,
    }
    legislative_sessions = [
        {
            "_scraped_name": "2009 Regular Session",
            "classification": "primary",
            "end_date": "2010-06-24",
            "identifier": "2009",
            "name": "2009 Regular Session",
            "start_date": "2010-04-27",
        },
        {
            "_scraped_name": "2010 Regular Session",
            "classification": "primary",
            "end_date": "2010-06-21",
            "identifier": "2010",
            "name": "2010 Regular Session",
            "start_date": "2010-03-29",
        },
        {
            "_scraped_name": "2011 Regular Session",
            "classification": "primary",
            "end_date": "2011-06-23",
            "identifier": "2011",
            "name": "2011 Regular Session",
            "start_date": "2011-04-25",
        },
        {
            "_scraped_name": "2011 First Extraordinary Session",
            "classification": "special",
            "end_date": "2011-04-13",
            "identifier": "2011 1st Extraordinary Session",
            "name": "2011, 1st Extraordinary Session",
            "start_date": "2011-03-20",
        },
        {
            "_scraped_name": "2012 Regular Session",
            "classification": "primary",
            "end_date": "2012-06-04",
            "identifier": "2012",
            "name": "2012 Regular Session",
            "start_date": "2012-03-12",
        },
        {
            "_scraped_name": "2013 Regular Session",
            "classification": "primary",
            "end_date": "2013-06-06",
            "identifier": "2013",
            "name": "2013 Regular Session",
            "start_date": "2013-04-08",
        },
        {
            "_scraped_name": "2014 Regular Session",
            "classification": "primary",
            "end_date": "2014-06-02",
            "identifier": "2014",
            "name": "2014 Regular Session",
            "start_date": "2014-03-10",
        },
        {
            "_scraped_name": "2015 Regular Session",
            "classification": "primary",
            "end_date": "2015-06-11",
            "identifier": "2015",
            "name": "2015 Regular Session",
            "start_date": "2015-04-13",
        },
        {
            "_scraped_name": "2016 Regular Session",
            "classification": "primary",
            "end_date": "2016-06-06",
            "identifier": "2016",
            "name": "2016 Regular Session",
            "start_date": "2016-03-14",
        },
        {
            "_scraped_name": "2016 First Extraordinary Session",
            "classification": "special",
            "end_date": "2016-03-09",
            "identifier": "2016 1st Extraordinary Session",
            "name": "2016, 1st Extraordinary Session",
            "start_date": "2016-02-14",
        },
        {
            "_scraped_name": "2016 Second Extraordinary Session",
            "classification": "special",
            "end_date": "2016-06-23",
            "identifier": "2016 2nd Extraordinary Session",
            "name": "2016, 2nd Extraordinary Session",
            "start_date": "2016-06-06",
        },
        {
            "_scraped_name": "2017 Regular Session",
            "classification": "primary",
            "identifier": "2017",
            "name": "2017 Regular Session",
            "start_date": "2017-04-10",
            "end_date": "2017-06-08",
        },
        {
            "_scraped_name": "2017 First Extraordinary Session",
            "classification": "special",
            "identifier": "2017 1st Extraordinary Session",
            "name": "2017, 1st Extraordinary Session",
            "start_date": "2017-02-13",
            "end_date": "2017-02-22",
        },
        {
            "_scraped_name": "2017 Second Extraordinary Session",
            "classification": "special",
            "identifier": "2017 2nd Extraordinary Session",
            "name": "2017, 2nd Extraordinary Session",
            "start_date": "2017-06-08",
            "end_date": "2017-06-16",
        },
        {
            "_scraped_name": "2018 First Extraordinary Session",
            "classification": "special",
            "identifier": "2018 1st Extraordinary Session",
            "name": "2018, 1st Extraordinary Session",
            "start_date": "2018-02-19",
            "end_date": "2018-03-05",
        },
        {
            "_scraped_name": "2018 Regular Session",
            "classification": "primary",
            "identifier": "2018",
            "name": "2018 Regular Session",
            "start_date": "2018-03-12",
            "end_date": "2018-05-18",
        },
        {
            "_scraped_name": "2018 Second Extraordinary Session",
            "classification": "special",
            "identifier": "2018 2nd Extraordinary Session",
            "name": "2018, 2nd Extraordinary Session",
            "start_date": "2018-05-22",
            "end_date": "2018-06-04",
        },
        {
            "_scraped_name": "2018 Third Extraordinary Session",
            "classification": "special",
            "identifier": "2018 3rd Extraordinary Session",
            "name": "2018, 3rd Extraordinary Session",
            "start_date": "2018-06-18",
            "end_date": "2018-06-24",
        },
        {
            "_scraped_name": "2019 Regular Session",
            "classification": "primary",
            "identifier": "2019",
            "name": "2019 Regular Session",
            "start_date": "2019-04-08",
            "end_date": "2019-06-06",
        },
        {
            "_scraped_name": "2020 Regular Session",
            "classification": "primary",
            "identifier": "2020",
            "name": "2020 Regular Session",
            "start_date": "2020-03-09",
            "end_date": "2020-06-01",
        },
        {
            "_scraped_name": "2020 First Extraordinary Session",
            "classification": "special",
            "identifier": "2020s1",
            "name": "2020 First Extraordinary Session",
            "start_date": "2020-06-01",
            "end_date": "2020-06-30",
        },
        {
            "_scraped_name": "2020 Second Extraordinary Session",
            "classification": "special",
            "identifier": "2020s2",
            "name": "2020 Second Extraordinary Session",
            "start_date": "2020-09-28",
            "end_date": "2020-10-23",
        },
        {
            "_scraped_name": "2021 Regular Session",
            "classification": "primary",
            "identifier": "2021",
            "name": "2021 Regular Session",
            "start_date": "2021-03-12",
            "end_date": "2021-06-10",
            "active": False,
        },
        {
            "_scraped_name": "2022 First Extraordinary Session",
            "classification": "special",
            "identifier": "2022s1",
            "name": "2022 First Extraordinary Session",
            "start_date": "2022-02-01",
            "end_date": "2022-02-18",
            "active": False,
        },
        {
            "_scraped_name": "2022 Regular Session",
            "classification": "primary",
            "identifier": "2022",
            "name": "2022 Regular Session",
            "start_date": "2022-03-14",
            "end_date": "2022-06-06",
            "active": False,
        },
        {
            "_scraped_name": "2022 Second Extraordinary Session",
            "classification": "special",
            "identifier": "2022s2",
            "name": "2022 Second Extraordinary Session",
            "start_date": "2022-06-15",
            "end_date": "2022-06-18",
            "active": False,
        },
        {
            "_scraped_name": "2023 Regular Session",
            "classification": "primary",
            "identifier": "2023",
            "name": "2023 Regular Session",
            "start_date": "2023-04-10",
            "end_date": "2023-06-08",
            "active": False,
        },
        {
            "_scraped_name": "2023 First Extraordinary Session",
            "classification": "primary",
            "identifier": "2023s1",
            "name": "2023 First Extraordinary Session",
            "start_date": "2023-01-30",
            "end_date": "2023-02-05",
            "active": False,
        },
        {
            "_scraped_name": "2024 First Extraordinary Session",
            "classification": "special",
            "identifier": "2024s1",
            "name": "2024 First Extraordinary Session",
            "start_date": "2024-01-15",
            "end_date": "2024-01-23",
            "active": False,
        },
        {
            "_scraped_name": "2024 Second Extraordinary Session",
            "classification": "special",
            "identifier": "2024s2",
            "name": "2024 Second Extraordinary Session",
            "start_date": "2024-02-19",
            "end_date": "2024-03-06",
            "active": False,
        },
        {
            "_scraped_name": "2024 Third Extraordinary Session",
            "classification": "special",
            "identifier": "2024s3",
            "name": "2024 Third Extraordinary Session",
            "start_date": "2024-11-01",
            "end_date": "2024-11-29",
            "active": True,
        },
        {
            "_scraped_name": "2024 Regular Session",
            "classification": "primary",
            "identifier": "2024",
            "name": "2024 Regular Session",
            "start_date": "2024-03-11",
            "end_date": "2024-06-03",
            "active": True,
        },
        {
            "_scraped_name": "2025 Regular Session",
            "classification": "primary",
            "identifier": "2025",
            "name": "2025 Regular Session",
            "start_date": "2025-04-14",
            "end_date": "2025-06-12",
            "active": False,
        },
    ]
    ignored_scraped_sessions = [
        "2024 Organizational Session",
        "2023 Veto Session",
        "2022 Veto Session",
        "2021 Veto Session",
        "2020 Organizational Session",
        "2016 Organizational Session",
        "2015 Regular Session",
        "2014 Regular Session",
        "2013 Regular Session",
        "2012 Regular Session",
        "2012 Organizational Session",
        "2011 Regular Session",
        "2011 First Extraordinary Session",
        "2010 Regular Session",
        "2009 Regular Session",
        "2008 Regular Session",
        "2008 Organizational Session",
        "2008 Second Extraordinary Session",
        "2008 First Extraordinary Session",
        "2007 Regular Session",
        "2006 Regular Session",
        "2005 Regular Session",
        "2004 Regular Session",
        "2004 First Extraordinary Session",
        "2004 1st Extraordinary Session",
        "2003 Regular Session",
        "2002 Regular Session",
        "2001 Regular Session",
        "2000 Regular Session",
        "1999 Regular Session",
        "1998 Regular Session",
        "1997 Regular Session",
        "2006 Second Extraordinary Session",
        "2006 First Extraordinary Session",
        "2005 First Extraordinary Session",
        "2002 First Extraordinary Session",
        "2001 Second Extraordinary Session",
        "2001 First Extraordinary Session",
        "2000 Second Extraordinary Session",
        "2000 First Extraordinary Session",
        "1998 First Extraordinary Session",
        "2012 Organizational Session",
        "2000 Organizational Session",
        "2004 Organizational Session",
        "Other Sessions",
        "Other Sessions",
        "Sessions",
    ]

    def get_session_list(self):
        return url_xpath(
            "https://www.legis.la.gov/Legis/SessionInfo/SessionInfo.aspx",
            '//table[@id="ctl00_ctl00_PageBody_DataListSessions"]//a[contains'
            '(text(), "Session")]/text()',
        )
