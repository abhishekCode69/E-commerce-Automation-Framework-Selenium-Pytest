def test_home_page_title(driver):
    driver.get("https://automationexercise.com/")
    assert "Automation Exercise" in driver.title 
        