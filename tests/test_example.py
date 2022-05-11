
def test_first(driver):
    driver.get("http://192.168.1.190:8081/")
    assert "Your Store" == driver.title
    driver.save_screenshot("test.png")
