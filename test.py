from datetime import datetime, timedelta
import yaml

with open('_data/emoji.yaml') as f:
	data = yaml.load(f, Loader=yaml.FullLoader)
available_dates = set(data.keys())

starting_date = '2024-01-01'
ending_date = '2024-12-31'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def generate_dates(year):
    current_date = datetime(year, 1, 1)
    while current_date != datetime(year, 12, 31):
        d1 = current_date.strftime("%Y-%m-%d")
        d2 = current_date.strftime("%m-%d")
        current_date += timedelta(days=1)
        yield d1,d2

count = 0
month = "01"
for d1,d2 in generate_dates(datetime.now().year):
    if month != d2.split("-")[0]:
        month = d2.split("-")[0]
        print()
    date = d2.split("-")[1]
    if d1 in available_dates or d2 in available_dates:
        print(f"{bcolors.ENDC}{date}{bcolors.ENDC}",end=' ')
        count+=1
    else:
        print(f"{bcolors.FAIL}{date}{bcolors.ENDC}",end=' ')

print(f"\n{count}/365 days covered")

assert(count>=160)