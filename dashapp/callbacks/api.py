import httpx
import pandas


def graduated_api():
    # client = httpx.Client()
    # url = "https://gpa.obec.go.th/reportdata/pp3-4_2566_province.json"

    # try:
    #     response = client.get(url)
    #     json_data = response.json()
    #     df = pandas.DataFrame(json_data)
    # except:
    #     df = pandas.DataFrame()

    df = pandas.read_json("dashapp/graduated.json")
    return df
