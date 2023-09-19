import requests


def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded and saved as {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the URL of the file you want to download: ")
    save_path = input("Enter the path where you want to save the file: ")

    download_file(url, save_path)
