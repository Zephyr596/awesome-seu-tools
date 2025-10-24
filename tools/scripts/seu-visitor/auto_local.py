"""Automate the SEU visitor appointment form using local profile data.

The upstream project relies on a MySQL database to store personal
information.  In many scenarios maintaining a dedicated database is
overkill, so this adapter reads visitor profiles from a local JSON file
and reuses the Selenium automation steps from the original project.

Example usage::

    python auto_local.py --profiles user_info.json

The JSON file should follow the structure documented in
``user_info_template.json``.  Each profile entry will be submitted once.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from selenium import webdriver
from selenium.webdriver.common.by import By


DEFAULT_FORM_URL = (
    "https://infoplus.seu.edu.cn/infoplus/form/XWJXSQ/start?"
    "sig=bd12f0a41c7a9b8a2a2d0cbd48b138dc&ts=1767024000"
    "&uid=0f1fb840-aa02-11ea-b752-005056bd7aba&lxfs=18351939811"
)


@dataclass
class UserInfo:
    """Container for a single visitor profile."""

    name: str
    phone: str
    id_number: str
    car_number: str
    phone_teacher: str
    id_department: str
    department: str
    id_teacher: str
    name_teacher: str
    dormitory: str
    card: str


def load_profiles(path: Path) -> List[UserInfo]:
    """Load visitor profiles from ``path``.

    Parameters
    ----------
    path:
        Path to the JSON file.  The file must contain either a list of
        objects or an object with a top-level ``profiles`` array.
    """

    with path.open("r", encoding="utf-8") as fp:
        payload = json.load(fp)

    if isinstance(payload, dict) and "profiles" in payload:
        payload = payload["profiles"]

    if not isinstance(payload, list):
        raise ValueError("Profile file must contain a JSON array")

    profiles: List[UserInfo] = []
    for entry in payload:
        profiles.append(
            UserInfo(
                name=entry["name"],
                phone=entry["phone"],
                id_number=entry["id_number"],
                car_number=entry["car_number"],
                phone_teacher=entry["phone_teacher"],
                id_department=entry["id_department"],
                department=entry["department"],
                id_teacher=entry["id_teacher"],
                name_teacher=entry["name_teacher"],
                dormitory=entry["dormitory"],
                card=entry["card"],
            )
        )

    return profiles


def build_browser(headless: bool = True) -> webdriver.Chrome:
    """Create a Chrome WebDriver instance."""

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    return webdriver.Chrome(options=options)


def apply_car(user: UserInfo, browser: webdriver.Chrome, form_url: str) -> None:
    """Submit the visitor appointment form for ``user``."""

    browser.get(form_url)
    browser.implicitly_wait(15)

    browser.find_element(By.XPATH, '//input[@type="checkbox"]').click()
    browser.find_element(By.XPATH, '//a[@id="preview_start_button"]').click()

    print("Login finished, the process starts now for:", user.name)

    browser.find_element(By.XPATH, '//tr[15]//input[@id="V1_CTRL390"]').click()

    phone_number = browser.find_element(By.XPATH, '//tr[20]//div//input[@name = "fieldLXFS"]')
    phone_number.clear()
    time.sleep(1)
    phone_number.send_keys(user.phone)

    name_student = browser.find_element(By.XPATH, '//*[@id="V1_CTRL177"]')
    name_student.clear()
    browser.execute_script("arguments[0].value = arguments[1];", name_student, user.name)

    name_university = browser.find_element(By.XPATH, '//*[@id="V1_CTRL178"]')
    name_university.clear()
    browser.execute_script(
        "arguments[0].value = '东南大学';",
        name_university,
    )

    id_student = browser.find_element(By.XPATH, '//*[@id="V1_CTRL180"]')
    id_student.clear()
    browser.execute_script("arguments[0].value = arguments[1];", id_student, user.id_number)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    for element in browser.find_elements(By.XPATH, '//tr//input[@id="V1_CTRL267"]'):
        browser.execute_script("arguments[0].click();", element)

    for element in browser.find_elements(By.XPATH, '//tr[33]//td[4]//input[@id  = "V1_CTRL274"]'):
        browser.execute_script("arguments[0].click();", element)

    drive_or_not = browser.find_element(By.XPATH, '//tr[35]//input[@value="1"]')
    browser.execute_script("arguments[0].click();", drive_or_not)

    license_car = browser.find_element(By.XPATH, '//*[@id="V1_CTRL217"]')
    browser.execute_script("arguments[0].value = arguments[1];", license_car, user.car_number)

    phone_number_teacher = browser.find_element(By.XPATH, '//*[@id="V1_CTRL379"]')
    browser.execute_script(
        "arguments[0].value = arguments[1];",
        phone_number_teacher,
        user.phone_teacher,
    )

    department_stu = browser.find_element(By.XPATH, '//*[@id="V1_CTRL377"]')
    browser.execute_script(
        """
        var option = new Option(arguments[1], arguments[0]);
        arguments[2].appendChild(option);
        arguments[2].value = arguments[0];
        """,
        user.id_department,
        user.department,
        department_stu,
    )

    teacher_name = browser.find_element(By.XPATH, '//*[@id="V1_CTRL378"]')
    browser.execute_script(
        """
        var option = new Option(arguments[1], arguments[0]);
        arguments[2].appendChild(option);
        arguments[2].value = arguments[0];
        """,
        user.id_teacher,
        user.name_teacher,
        teacher_name,
    )

    dorm_location = browser.find_element(By.XPATH, '//textarea[@id="V1_CTRL376"]')
    browser.execute_script("arguments[0].value = arguments[1];", dorm_location, user.dormitory)

    reason_for_enter = browser.find_element(By.XPATH, '//textarea[@id="V1_CTRL380"]')
    reason_text = f"开车入校，{user.name}，{user.card}"
    browser.execute_script("arguments[0].value = arguments[1];", reason_for_enter, reason_text)

    apply_button = browser.find_element(
        By.XPATH, '//div[@class="commandC"]//a[@class="command_button_content"]//nobr'
    )
    browser.execute_script("arguments[0].click();", apply_button)
    print("The appointment is done for:", user.name)
    time.sleep(5)


def run_batch(users: Iterable[UserInfo], headless: bool, form_url: str) -> None:
    """Submit appointments for each user in ``users``."""

    browser = build_browser(headless=headless)
    try:
        for user in users:
            apply_car(user, browser, form_url)
    finally:
        browser.quit()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="SEU visitor appointment automation")
    parser.add_argument(
        "--profiles",
        type=Path,
        default=Path(__file__).with_name("user_info.json"),
        help="Path to the JSON file that stores visitor profiles.",
    )
    parser.add_argument(
        "--form-url",
        default=DEFAULT_FORM_URL,
        help="Target form URL.  Defaults to the URL used by the upstream script.",
    )
    parser.add_argument(
        "--no-headless",
        action="store_false",
        dest="headless",
        help="Disable headless mode for Chrome.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    profiles = load_profiles(args.profiles)
    if not profiles:
        raise SystemExit("No visitor profiles loaded – please check the JSON file.")

    run_batch(profiles, headless=args.headless, form_url=args.form_url)
    print("Successfully processed", len(profiles), "profiles.")


if __name__ == "__main__":
    main()
