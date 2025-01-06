# Selenium Pytest Automation

## Project Setup

1. Clone the repository:

   git clone https://github.com/Crashtest/OrangeTest.git
2. cd OrangeHRMLiveTest
3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```
3. Once that is done, simply run the following command to install the required dependencies:

   ```sh
   pytest ./tests/test_login.py
   ```
   
This was a difficult task for me. If I had been involved in the creation of this web project, I would have requested that the developers add <tag>'s to elements on the page to make them easier to identify.

I ended up using the `xpath` method to identify elements on the page. This is not the best way to do this, but it was the only way I could find to identify the elements on the page.

I also had to use the `time.sleep()` method to wait for the page to load before I could interact with it. This is not the best way to do this either, but it was the only way I could find to make the test work.


