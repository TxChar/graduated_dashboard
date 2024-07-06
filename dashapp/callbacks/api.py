import httpx
import pandas
import plotly.graph_objects as go
import plotly.express as px


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


def provinces_location():
    df_graduated = (graduated_api()).drop(["pp3year", "level"], axis=1)
    df_locations = pandas.read_csv("dashapp/ThailandProvincesLocation.csv")
    df_merge_locations = pandas.merge(df_graduated, df_locations, on="schools_province")
    return df_merge_locations
