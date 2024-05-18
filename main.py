import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_URL = "https://devapi.beyondchats.com/api/get_message_with_sources"

def fetch_data(api_url):
    page = 1
    data = []
    while True:
        response = requests.get(api_url, params={'page': page})
        response_data = response.json()
        if not response_data:
            break
        data.extend(response_data)
        page += 1
    return data

def find_citations(data):
    all_citations = []
    for item in data:
        response_text = item.get('response')
        sources = item.get('sources', [])
        citations = []
        for source in sources:
            if source['context'] in response_text:
                citation = {'id': source['id']}
                if 'link' in source and source['link']:
                    citation['link'] = source['link']
                citations.append(citation)
        all_citations.append(citations)
    return all_citations

@app.route('/get_citations', methods=['GET'])
def get_citations():
    data = fetch_data(API_URL)
    citations = find_citations(data)
    return jsonify(citations)

if __name__ == '__main__':
    app.run(debug=True)
