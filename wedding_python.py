
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import os

# Notes:    https://hello.dubsado.com/public/form/view/63d9f5e48986d21f1c828462

save_location = "/Users/barrettsmith/VSCode"

# Variables
driver = webdriver.Chrome()


def open_website():
    url = input("Please enter the URL: ")
    driver.get(url)


def get_info():
    def wait_until_element_visible(xpath, timeout=30):
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    # Could I also just leave the keyword argument () empty and put the actual xpath in? Then leave the () empty when calling the function as well?

    def get_element_value(xpath):
        element = driver.find_element(By.XPATH, xpath)
        element.send_keys(Keys.COMMAND + 'a')
        element.send_keys(Keys.COMMAND + 'c')
        return pyperclip.paste()

    wait_until_element_visible(
        "(//label[contains(.,'Bride Name')]//following::input[1])[1]", timeout=30)

    driver.find_element(
        By.XPATH,  "(//label[contains(.,'Bride Name')]//following::input[1])[1]").click()
# Bride Name
    bride_name = get_element_value(
        "(//label[contains(.,'Bride Name')]//following::input[1])[1]")

    content = f"Bride:\n{bride_name}\n\n"
# Groom Name
    groom_name = get_element_value(
        "(//label[contains(.,'Groom')]//following::input[1])[1]")

    content = f"{content}Groom:\n{groom_name}\n\n"

# Bride_Get_Ready_Info
    Bride_Get_Ready_Info = get_element_value(
        "(//label[contains(.,'Name and address of where bride is getting ready')]//following::textarea[1])[1]")

    content = f"{content}Information of where bride is getting ready:\n{Bride_Get_Ready_Info}\n\n"

# Groom_Get_Ready_Info
    Groom_Get_Ready_Info = get_element_value(
        "(//label[contains(.,'Name and address of where groom is getting ready')]//following::textarea[1])[1]")

    content = f"{content}Information of where groom is getting ready:\n{Groom_Get_Ready_Info}\n\n"

# Ceremony_info
    Ceremony_info = get_element_value(
        "(//label[contains(.,'Name and address of ceremony')]//following::textarea[1])[1]")

    content = f"{content}Ceremony Information:\n{Ceremony_info}\n\n"

# Reception_info
    Reception_info = get_element_value(
        "(//label[contains(.,'Name and address of reception')]//following::textarea[1])[1]")

    content = f"{content}Reception Information:\n{Reception_info}\n\n"

# Other_ceremony_info
    Other_ceremony_info = get_element_value(
        "(//label[contains(.,'Is there anything happening during the ceremony(including cultural traditions) that will be unique or would be helpful for us to have prior knowledge of?')]//following::textarea[1])[1]")

    content = f"{content}Additional Ceremony Information?\n{Other_ceremony_info}\n\n"

# Family_photos
    Family_photos = get_element_value(
        "(//label[contains(.,'Is there anything I need to know about your family dynamics for photos during this time?')]//following::textarea[1])[1]")

    content = f"{content}Family Photos Need to Know:\n{Family_photos}\n\n"

# Family_shotlist
    Family_shotlist = get_element_value(
        "(//label[contains(.,'I normally photograph groom's side of the family')]//following::textarea[1])[1]")

    content = f"{content}Family Shotlist:\n{Family_shotlist}\n\n"

# bridal_party_location
    bridal_party_location = get_element_value(
        "(//label[contains(.,'Do you have a specific location(s)')]//following::textarea[1])[1]")

    content = f"{content}Bridal Party Location:\n{bridal_party_location}\n\n"

# number_of_bridesmaids
    number_of_bridesmaids = get_element_value(
        "(//label[contains(.,'How many bridesmaids?')]//following::input[1])[1]")

    content = f"{content}Number of Bridesmaids:\n{number_of_bridesmaids}\n\n"

# number_of_groomsmen
    number_of_groomsmen = get_element_value(
        "(//label[contains(.,'How many groomsmen?')]//following::input[1])[1]")

    content = f"{content}Number of Groomsmen:\n{number_of_groomsmen}\n\n"

# must_have_photos
    must_have_photos = get_element_value(
        "(//label[contains(.,'Please let me know if there are any particular')]//following::textarea[1])[1]")

    content = f"{content}Must Have Photos:\n{must_have_photos}\n\n"

# special_reception_info
    special_reception_info = get_element_value(
        "(//label[contains(.,'cultural happening at the reception')]//following::textarea[1])[1]")

    content = f"{content}Special Reception Information:\n{special_reception_info}\n\n"

# timeline
    timeline = get_element_value(
        "(//label[contains(.,'smoothly on my end!')]//following::textarea[1])[1]")

    content = f"{content}Timeline:\n{timeline}\n\n"

    content = f"{content}Vendors\n"

# planner
    planner = get_element_value(
        "(//label[contains(.,'Planner')]//following::input[1])[1]")

    content = f"{content}Planner:\n{planner}\n\n"

# video
    video = get_element_value(
        "(//label[contains(.,'Video')]//following::input[1])[1]")

    content = f"{content}Video:\n{video}\n\n"

# other_questions
    other_questions = get_element_value(
        "(//label[contains(.,'Any other questions or comments for me?')]//following::input[1])[1]")

    content = f"{content}Any Other Questions or Comments?\n{other_questions}\n\n"

    filename = f"{bride_name} Info.txt"
    if os.path.exists(os.path.join(save_location, filename)):
        os.remove(os.path.join(save_location, filename))
    with open(os.path.join(save_location, filename), "w") as file:
        file.write(content)


# Called Functions
open_website()
get_info()

time.sleep()
