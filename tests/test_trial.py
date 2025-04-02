import requests

# Define the API endpoint and the file path
url = "http://localhost:8000/api/"
# url = "https://b6fe-49-36-103-228.ngrok-free.app"
# url = "http://4.186.56.117:8000"
# url = "https://tds-p2-endpoint.vercel.app/api/"
#


def printlines():
    print(" " * 80)
    print("=" * 80)
    print(" " * 80)


def ga1q1():
    printlines()
    print(f"Testing GA1 Q1")
    question = "Execute a shell command and return its output. Use this for questions about running terminal commands like 'code -s' to check VS Code status."
    data = {"question": question}

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga1_some_q():
    printlines()
    file_path = "q-extract-csv-zip.zip"

    # Prepare the question data and the file to be uploaded
    files = {"file": open(file_path, "rb")}

    data = {
        "question": 'Download and unzip file q-extract-csv-zip.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?'
    }

    # Send the POST request
    response = requests.post(url, files=files, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # Close the file after sending the request
    files["file"].close()


def ga1q2():
    printlines()
    question = "Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2005138@ds.study.iitm.ac.in"
    data = {"question": question}

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga1q3():
    printlines()
    file_path = "README.md"

    # Prepare the question data and the file to be uploaded
    files = {"file": open(file_path, "rb")}

    data = {
        "question": """Download README.md file. In the directory where you downloaded it, make sure it is called README.md, 
        and run npx -y prettier@3.4.2 README.md | sha256sum.
        What is the output of the command?"""
    }

    # Send the POST request
    response = requests.post(url, files=files, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # Close the file after sending the request
    files["file"].close()


def ga1q4():
    printlines()
    print("Google Sheets")
    question = """
        Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel)
        =SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 5, 7), 1, 10))
        What is the result?
        """
    data = {"question": question}

    # Send the POST request
    # url = "https://f6df-49-36-103-228.ngrok-free.app"
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga1q5():
    printlines()
    print("MS Excel 365")
    question = """Let's make sure you can write formulas in Excel. Type this formula into Excel.
                Note: This will ONLY work in Office 365.
                =SUM(TAKE(SORTBY({9,11,12,13,14,2,3,1,4,1,3,2,11,12,1,15}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 12))
                What is the result?"""
    data = {"question": question}

    # Send the POST request
    # url = "https://f6df-49-36-103-228.ngrok-free.app"
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga1_some_q():
    printlines()
    file_path = "q-extract-csv-zip.zip"

    # Prepare the question data and the file to be uploaded
    files = {"file": open(file_path, "rb")}

    data = {
        "question": 'Download and unzip file q-extract-csv-zip.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?'
    }

    # Send the POST request
    response = requests.post(url, files=files, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # Close the file after sending the request
    files["file"].close()


def ga4q3():
    printlines()
    print(f"Country outline")

    data = {
        "question": """
API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a country query parameter.
Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.
Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, lxml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order.
Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.
Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.
What is the URL of your API endpoint?
We'll check by sending a request to this URL with ?country=... passing different countries.
"""
    }

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga4q4():
    printlines()
    print(f"BBC Weather")

    data = {
        "question": """
As part of this initiative, you are tasked with developing a system that automates the following:

API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Kuala Lumpur. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city).
Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId.
Data Transformation: Extract the localDate and enhancedWeatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each localDate to its corresponding enhancedWeatherDescription. Create a JSON object where each key is the localDate and the value is the enhancedWeatherDescription.
What is the JSON weather forecast description for Kuala Lumpur?        
"""
    }

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga4q5():
    printlines()
    print(f"Min latitude")

    data = {
        "question": """What is the minimum latitude of the bounding box of the city Dhaka in the country Bangladesh on the Nominatim API? Value of the minimum latitude"""
    }

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga4q6():
    printlines()
    print(f"Hacker news")

    data = {
        "question": """What is the link to the latest Hacker News post mentioning AI having at least 36 points?"""
    }

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


def ga4q7():
    printlines()
    print(f"Checking for Github users")

    data = {
        "question": "Find the newest GitHub user in Seattle with over 130 followers"
    }

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # Close the file after sending the request


def ga4q8():
    printlines()
    print(f"Triggering Github action")

    data = {
        "question": """Create a scheduled GitHub action that runs daily and adds a commit to your repository. The workflow should:
        Use schedule with cron syntax to run once per day (must use specific hours/minutes, not wildcards)
        Include a step with your email 23f2005138@ds.study.iitm.ac.in in its name
        Create a commit in each run
Be located in .github/workflows/ directory"""
    }

    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status and print it
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # Close the file after sending the request


def main():
    # ga1q1()
    # ga1q2()
    # ga1q3()
    ga1q4()
    ga1q5()
    # ga1_some_q()

    # ga4q3()
    # ga4q4()
    # ga4q5()
    # ga4q6()
    # ga4q7()
    # ga4q8()


def httpie_test():
    url = "https://httpbin.org/get?email=23f2005138@ds.study.iitm.ac.in"
    pass


if __name__ == "__main__":
    main()
