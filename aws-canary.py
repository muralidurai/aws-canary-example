import asyncio
from aws_synthetics.selenium import synthetics_webdriver as syn_webdriver
from aws_synthetics.common import synthetics_logger as logger, synthetics_configuration

TIMEOUT = 10

async def main():
    url = "https://markets.jpmorgan.com"
    browser = syn_webdriver.Chrome()


    # Set synthetics configuration
    synthetics_configuration.set_config({
       "screenshot_on_step_start" : True,
       "screenshot_on_step_success": True,
       "screenshot_on_step_failure": True
    });


    def navigate_to_page():
        browser.implicitly_wait(TIMEOUT)
        browser.get(url)

    await syn_webdriver.execute_step("navigateToUrl", navigate_to_page)

    # Execute customer steps
    def customer_actions_1():
        browser.find_element_by_xpath("//*[@id='userName1']").send_keys("CanaryTestUser")

    await syn_webdriver.execute_step('input', customer_actions_1)

    logger.info("Canary successfully executed")


async def handler(event, context):
    # user defined log statements using synthetics_logger
    logger.info("Selenium Python workflow canary")
    return await main()
