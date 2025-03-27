# Web Scraping Project - Books from "Books to Scrape"

This project demonstrates web scraping using Python, Flask, and BeautifulSoup. The goal of this project is to scrape book data from an e-commerce website "Books to Scrape" and display it on a modern, user-friendly web interface. Users can view the list of books, download the book data as a CSV file, and interact with the application in a simple way.

## Features

- **Web Scraping**: Scrape book data such as title, price, and availability from the website [Books to Scrape](https://books.toscrape.com/).
- **Flask Web Application**: The data is presented through a Flask web application.
- **CSV Download**: Users can download the scraped book data as a CSV file for further use.

## Installation

### Prerequisites

Ensure that you have Python 3.x and pip installed on your machine.

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/` to view the application.

### Download CSV

- Once the page is loaded, you can click the "Download CSV" button to get the scraped data as a CSV file.

## Technologies Used

- **Python**: Programming language used for scraping and backend logic.
- **Flask**: Web framework to display the data.
- **BeautifulSoup**: Python library used for parsing HTML and scraping the data.
- **Pandas**: Python library for managing and exporting the scraped data to CSV.
- **HTML/CSS**: For building the user interface.

## Dependencies

You can find all the dependencies in the `requirements.txt` file:

- Flask
- BeautifulSoup4
- Requests
- Pandas

## License

This project is open-source and available under the [MIT License](LICENSE).
