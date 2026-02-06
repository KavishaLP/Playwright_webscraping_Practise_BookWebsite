# 📚 Playwright Books Scraper

A robust web scraping and data visualization project that extracts book details from [Books to Scrape](https://books.toscrape.com/) and provides an interactive dashboard to explore the data.

## 🚀 Features

- **Automated Scraping**: Uses [Playwright](https://playwright.dev/) for reliable, high-speed asynchronous scraping.
- **Data Visualization**: Includes a Jupyter Notebook (`visualize_books.ipynb`) with an interactive UI.
- **Search & Filter**:
  - 🔍 **Search by Title**
  - ⭐ **Filter by Rating** (Minimum or Exact match)
  - 💰 **Filter by Price Range**
  - 🔄 **Reset Filters** button for easy exploration

## 📂 Project Structure

```bash
playwright-books-scraper/
│
├── scraper.py               # Main Python script to scrape data
├── visualize_books.ipynb    # Interactive notebook for data exploration
├── requirements.txt         # List of Python dependencies
├── README.md                # Project documentation
│
└── output/
    └── books.json           # Scraped data saved in JSON format
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KavishaLP/Playwright_webscraping_Practise_BookWebsite.git
   cd Playwright_webscraping_Practise_BookWebsite
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright Browsers**:
   ```bash
   playwright install chromium
   ```

## 🏃 Usage

### 1. Run the Scraper
Execute the script to scrape book data. This will save the results to `output/books.json`.

```bash
python scraper.py
```
> **Note**: The scraper runs in headless mode by default. You will see progress logs in the terminal.

### 2. Explore Data (Interactive Dashboard)
Open the Jupyter Notebook to visualize and search through the scraped books.

```bash
jupyter notebook visualize_books.ipynb
```
- Run all cells in the notebook.
- Use the **Search Title**, **Rating**, and **Price Range** widgets to filter the book list.

## 📊 Data Output
The scraped data is stored in `output/books.json` with the following fields:
- `title`: Title of the book
- `price`: Price (e.g., £51.77)
- `rating`: Star rating (One to Five)
- `availability`: Stock status
- `page`: Page number where it was found
- <img width="994" height="498" alt="image" src="https://github.com/user-attachments/assets/8ca2e756-1a25-43a8-a380-ed79d7078380" />-INTERFACE


## 🤝 Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.
