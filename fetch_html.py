import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# This is the first file, meant to retrieve and store the links into HTML format that can be parsed using beautiful soup!

# Generic function so we can just fetch and save any html's we might want for the project
def fetch_and_save_html(url, file_name, headers):

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Save the response content to a file
        with open(file_name, 'w', encoding='utf-8') as file:
            print("WRITING")
            file.write(response.text)
        # print(f"The HTML content has been saved to {file_name}")
    else:
        print(f"Failed to retrieve the page from {url}, status code: {response.status_code}")

# The closest thing to a main function, so far just gets the resume and tournament links, 
# and puts all of the stuff into an actual html file.
def crawl_websites():
    # Headers to simulate a request from a web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_74; rv:12.0) Gecko/20100101 Firefox/12.0"
    }

    # driver = webdriver.Chrome()

    # URLs for the tournament and resume websites
    tournament_url_asc = "https://www.espn.com/mens-college-basketball/bpi/_/view/tournament/group/100/sort/tournament.projectedtournamentseedactual/dir/asc"
    tournament_url_desc = "https://www.espn.com/mens-college-basketball/bpi/_/view/tournament/group/100/sort/tournament.projectedtournamentseedactual/dir/desc"
    resume_url_asc = "https://www.espn.com/mens-college-basketball/bpi/_/view/resume/group/100/sort/resume.projectedtournamentseed/dir/asc"
    resume_url_desc = "https://www.espn.com/mens-college-basketball/bpi/_/view/resume/group/100/sort/resume.sorrank/dir/desc"
   
    # driver.get(tournament_url)
    # #driver.get(resume_url)
    # print("TEST1")
    # # Find and click the "Show More" link
    # show_more_link = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'loadMore__link'))
    # )
    # show_more_link.click()
    # print("AFTER SHOW MORE")
    # Wait for the content to load
    #WebDriverWait(driver, 10).until(
    #    EC.visibility_of_element_located((By.CLASS_NAME, "AnchorLink loadMore__link"))
    #)
    # print("AFTER WEB DRIVER")
    # <div class="tc mv5 loadMore"><a class="AnchorLink loadMore__link" tabindex="0" href="#">Show More</a></div>
    # Get the page source after clicking "Show More"
    # page_source = driver.page_source
    # print("AFTER PAGE SOURCE")
    # Parse the page source using BeautifulSoup
    #soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the desired information from the parsed HTML
    # For example:
    # content = soup.find_all('div', class_='class_of_content_you_want_to_scrape')

    # Close the WebDriver
    # driver.quit()

    # File names for saving the HTML content
    tournament_file_asc = "tournament_asc.html"
    tournament_file_desc = "tournament_desc.html"
    resume_file_asc = "resume_asc.html"
    resume_file_desc = "resume_desc.html"

    # Fetch and save HTML content for both URLs
    fetch_and_save_html(tournament_url_asc, tournament_file_asc, headers)
    fetch_and_save_html(tournament_url_desc, tournament_file_desc, headers)
    fetch_and_save_html(resume_url_asc, resume_file_asc, headers)
    fetch_and_save_html(resume_url_desc, resume_file_desc, headers)

# Main!
if __name__ == '__main__':
    print("Starting the crawl...")
    crawl_websites()