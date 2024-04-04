import requests

# This is the first file, meant to retrieve and store the links into HTML format that can be parsed using beautiful soup!

# Generic function so we can just fetch and save any html's we might want for the project
def fetch_and_save_html(url, file_name, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Save the response content to a file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"The HTML content has been saved to {file_name}")
    else:
        print(f"Failed to retrieve the page from {url}, status code: {response.status_code}")

# The closest thing to a main function, so far just gets the resume and tournament links, 
# and puts all of the stuff into an actual html file.
def crawl_websites():
    # Headers to simulate a request from a web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_74; rv:12.0) Gecko/20100101 Firefox/12.0"
    }

    # URLs for the tournament and resume websites
    tournament_url = "https://www.espn.com/mens-college-basketball/bpi/_/view/tournament/group/100/sort/tournament.projectedtournamentseedactual/dir/asc"
    resume_url = "https://www.espn.com/mens-college-basketball/bpi/_/view/resume/group/100/sort/resume.projectedtournamentseed/dir/asc"
    
    # File names for saving the HTML content
    tournament_file = "tournament.html"
    resume_file = "resume.html"

    # Fetch and save HTML content for both URLs
    fetch_and_save_html(tournament_url, tournament_file, headers)
    fetch_and_save_html(resume_url, resume_file, headers)

# Main!
if __name__ == '__main__':
    print("Starting the crawl...")
    crawl_websites()