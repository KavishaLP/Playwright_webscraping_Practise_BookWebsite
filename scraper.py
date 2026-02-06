import asyncio
import json
from playwright.async_api import async_playwright

# Base URL for the book scraping website with a placeholder for page number
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

async def scrape_books():
    """
    Scrapes book data from books.toscrape.com using Playwright.
    Iterates through all pages until a 404 is encountered.
    
    Returns:
        list: A list of dictionaries, each containing book details.
    """
    books_data = []

    async with async_playwright() as p:
        # Launch browser in headless mode (no UI visible)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        page_number = 1

        while True:
            url = BASE_URL.format(page_number)
            print(f"Scraping page {page_number}: {url}")

            # Navigate to the page
            response = await page.goto(url)
            
            # Stop if the page doesn't exist (e.g., 404 error at the end of pagination)
            if response.status != 200:
                break

            # Wait for book elements to load to ensure content is ready
            await page.wait_for_selector(".product_pod")

            # Locate all book items on the current page
            books = page.locator(".product_pod")
            count = await books.count()

            # Iterate through each book on the page
            for i in range(count):
                book = books.nth(i)

                # Extract details using CSS selectors
                title = await book.locator("h3 a").get_attribute("title")
                price = await book.locator(".price_color").inner_text()
                availability = await book.locator(".availability").inner_text()
                
                # Extract rating (class name contains the rating, e.g., "star-rating Three")
                rating_class = await book.locator("p.star-rating").get_attribute("class")
                rating = rating_class.split()[-1] # Get the last part: "Three"

                books_data.append({
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "availability": availability.strip(),
                    "page": page_number
                })

            # Move to the next page
            page_number += 1

        await browser.close()

    return books_data


async def main():
    """
    Main function to run the scraper and save the output to a JSON file.
    """
    data = await scrape_books()

    # Save the scraped data to a JSON file
    output_file = "output/books.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Scraping complete. Total books scraped: {len(data)}")
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    asyncio.run(main())