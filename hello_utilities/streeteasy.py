from selenium import webdriver

from hello_models.models import Room
from hello_utilities.log_helper import _log


def get_list_of_building_links():
    building_links = []
    return building_links


def get_list_of_floorplan_links_from_building(building_link):
    floorplan_links = []
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get("https://duckduckgo.com/")
    driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
    driver.find_element_by_id("search_button_homepage").click()
    print driver.current_url
    driver.quit()
    return floorplan_links


def save_room(building_link, floorplan_image_link, db_session):
    room = Room(
        building_link=building_link,
        floorplan_image_link=floorplan_image_link
    )
    db_session.add(room)
    db_session.commit()


def scrape_rooms(db_session):
    building_links = get_list_of_building_links()
    for b_link in building_links:
        _log('++ getting floorplans from {}'.format(b_link))
        floorplan_links = get_list_of_floorplan_links_from_building(building_link=b_link)
        for f_link in floorplan_links:
            save_room(
                building_link=b_link,
                floorplan_image_link=f_link,
                db_session=db_session
            )

if __name__ == '__main__':
    # from hello_models.database import db_session
    # scrape_rooms(db_session=db_session)
    get_list_of_building_links()