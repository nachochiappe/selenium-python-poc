"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver

CONFIG_FILE_LOCATION = 'config/config.json'

@pytest.fixture
def config(scope='session'):

    # Read the file
    with open(CONFIG_FILE_LOCATION) as config_file:
        config = json.load(config_file)
  
    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    # Set up options for both Chrome and Headless Chrome
    chrome_options = selenium.webdriver.ChromeOptions()
    chrome_options.add_argument('ignore-certificate-errors')

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        profile = selenium.webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        b = selenium.webdriver.Firefox(firefox_profile=profile)
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome(options=chrome_options)
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        chrome_options.add_argument('headless')
        b = selenium.webdriver.Chrome(options=chrome_options)
    elif config['browser'] == 'Internet Explorer':
        capabilities = selenium.webdriver.DesiredCapabilities().INTERNETEXPLORER
        capabilities['acceptSslCerts'] = True
        b = selenium.webdriver.Ie(capabilities=capabilities)
    elif config['browser'] == 'Edge':
        b = selenium.webdriver.Edge()    
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()