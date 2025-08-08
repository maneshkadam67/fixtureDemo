import pytest
import requests
from selenium import webdriver

URL='''https://firebaseremoteconfig.googleapis.com/v1/projects/castify-storage
    /namespaces/firebase:fetch?key=AIzaSyDraAcnfh7TewzYJS9yt8Togm6_VzB_RJE'''

@pytest.fixture(scope="session", autouse=True)
def health_check():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            pytest.skip(f"Health check failed with status {response.status_code}, skipping tests.")
    except Exception as e:
        pytest.skip(f"Health check failed: {e}")


@pytest.fixture(scope="session")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}  # 1 = allow
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()

