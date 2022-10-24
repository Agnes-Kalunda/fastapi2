

# import urllib.request,json

# api_key = None
# base_url = None

# def configure_request(app)
#     global api_key, base_url
#     api_key = app.config['api_key']
#     base_url = app.config['NEWS_API_BASE_URL']


# def get_source():
#     source_base_url = "https://api.stlouisfed.org/fred/series/observations"+\
#                        "?series_id={seriesID}&api_key={api_key}&file_type=json"+\
#                         "&observation_start={start}&observation_end{end}&units={units}"

#     with urllib.request.urlopen(source_base_url) as url:
#         get_source_data = url.read()
#         get_source_response = json.loads(get_source_data)

#         source_results = None

#         if get_source_response['sources']:
#             source_results_list = get_source_response['sources']
#             source_results = produce_results(source_results_list)

#             return source_results

# #seriesID request
# def get_seriesID():
#     get_seriesID_url = source_base_url
#     with urllib.request.urlopen(get_seriesID_url) as url:
#         get_seriesID_data = url.read()
#         get_seriesID_response = json.loads(get_seriesID_data)

#         seriesID_results = None

#         if get_seriesID_response['seriesID']
#             seriesID_list = get_seriesID_response['seriesID']
#             seriesID_results = process_results(seriesID_results_list)

#             return seriesID_results


