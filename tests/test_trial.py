import requests

# Define the API endpoint and the file path
# url = "http://127.0.0.1:8000/api/"
# url = "https://b6fe-49-36-103-228.ngrok-free.app"
# url = "http://4.186.56.117:8000"
url = "https://tds-p2-endpoint.vercel.app/api/"


def printlines():
    print(" " * 80)
    print("=" * 80)
    print(" " * 80)


def ga1q1():
    printlines()
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


def ga1q5():
    printlines()
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


def main():
    ga1q1()
    # ga1q2()
    ga1q3()
    # ga1q5()
    # ga1_some_q()


def httpie_test():
    url = "https://httpbin.org/get?email=23f2005138@ds.study.iitm.ac.in"
    pass


if __name__ == "__main__":
    main()
