import sys, os
from skillshare import Skillshare, splash


# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    phpsessid = sys.argv[1]
    dl = Skillshare("PHPSESSID="+phpsessid)
    course_url = sys.argv[2]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
