# Credits to Pojomi for search function

from urllib.request import urlopen as req_url
import json


filename = "warframe-market-item-names.txt"
# Search API for most recent average price scrape
def search(target):

    # print("Searching for " + string.capwords(target) + "...")
    main_url = req_url(
        "https://api.warframe.market/v1/items/"
        + target.replace(" ", "_").lower()
        + "/statistics"
    )
    # time.sleep(5)

    data = main_url.read()
    # time.sleep(5)
    parsed = json.loads(data)
    parsed_data = parsed["payload"]["statistics_live"]["48hours"][-1]["min_price"]
    date_time = parsed["payload"]["statistics_live"]["48hours"][-1]["datetime"]

    return (parsed_data, date_time)


def read_list(filename):
    with open(filename, "r") as infile:
        data = infile.readlines()
        for line in data:
            price, time = search(line.strip())
            print(f"{line.strip()}: {price} Platinum")
            # -- Returning the price data along with the time at which the pricing data was recorded
            # -- (This works iteratively per individual item)
            # print(f"{line.strip()}: {price} Platinum -- [Time of evaluation: {time}]")


read_list(filename)

# -- Items without pricing data
# Artillery Battery Scene
# Ostron Chest Guard
# Meso T6 Relic
# Meso V8 Relic
# Neo A7 Relic
# Neo D6 Relic
