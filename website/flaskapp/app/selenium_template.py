#Author: Brendan Schweichler
#Template for Selenium testing
#Not tested as of right now
#Ran into docker run error
#Error: key error appears to be related to the browserleftoverscleanup process continually exiting unexpectedly and eventually leading to a FATAL state because it's trying to start too many times too quickly
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Update this URL to your Gitpod Selenium Grid UI URL but replace `/ui/#` with `/wd/hub`
grid_url = 'https://4444-seleniumhq-dockerseleni-onszkh4fhdg.ws-us110.gitpod.io/wd/hub'
# Actual url in case of /wd/hub path failure gitpod url: https://4444-seleniumhq-dockerseleni-onszkh4fhdg.ws-us110.gitpod.io/ui/#

# Your web application's Gitpod URL
app_url = 'https://4444-seleniumhq-dockerseleni-onszkh4fhdg.ws-us110.gitpod.io'
# Actual gitpod workstation url: https://4444-seleniumhq-dockerseleni-onszkh4fhdg.ws-us110.gitpod.io/ui/#

# Initialize the remote WebDriver using Selenium Grid
driver = webdriver.Remote(
    command_executor="https://7900-seleniumhq-dockerseleni-onszkh4fhdg.ws-us110.gitpod.io/?autoconnect=1&resize=scale&password=secret",
    desired_capabilities=DesiredCapabilities.FIREFOX,
)

try:
  # Your test code goes here. Example:
  driver.get(app_url)
  print(driver.title)
  # Assume there's a test to verify the app's title
  assert "ExpectedTitle" in driver.title

  # Add more actions as needed

finally:
  driver.quit()
