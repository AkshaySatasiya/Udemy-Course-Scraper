import os
import requests
import json
from urllib.parse import urlparse, parse_qs

# Create a directory to store the data
directory = "All Courses"
os.makedirs(directory, exist_ok=True)

# Read course URLs from the file and associate them with course names
course_data = []
with open("course_urls.txt", "r") as file:
    lines = file.readlines()
    course_name = None
    for line in lines:
        if line.startswith("# "):
            # Extract the course name from the comment line
            course_name = line.strip("# ").strip()
        elif line.strip():  # Check if the line is not empty
            # Store the course name and URL as a tuple
            course_data.append((course_name, line.strip()))

# Create a dictionary to store course data in the desired format
all_courses_data = {}

# Iterate through the course data
for course_name, course_url in course_data:
    base_url = course_url
    page = 1

    # Create a dictionary for each course
    course_info = {}

    while True:
        url = f"{base_url}&p={page}"

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON content from the response
            course_data = response.json()

            # Extracting relevant sections and modifying URLs
            unit = course_data.get("unit", {})
            course_items = unit.get("items", [])

            for course in course_items:
                course_title = course.get("title", "")
                course_url = course.get("url", "")
                if course_url.startswith("/"):
                    course_url = "https://www.udemy.com" + course_url  # Adding full Udemy URL to relative course URLs
                course_is_paid = course.get("is_paid", False)
                course_description = course.get("headline", "")
                subscribers = course.get("num_subscribers", 0)
                average_rating = course.get("avg_rating", 0)
                num_reviews = course.get("num_reviews", 0)
                num_lectures = course.get("num_published_lectures", 0)
                content_length = course.get("content_info", "")
                last_update = course.get("last_update_date", "")
                badges = [badge.get("badge_text", "") for badge in course.get("badges", [])]


                # Fetching the primary language used in the course from the 'locale' section
                course_language = course.get("locale", {}).get("title", "")

                # Instructional level of the course
                instructional_level = course.get("instructional_level", "")

                # Extracting author information
                authors = course.get("visible_instructors", [])
                author_names = [author.get("display_name", "") for author in authors]

                # Scraping the course image URL
                image_url = course.get("image_125_H")

                # Add course details to the dictionary
                course_info[course_title] = {
                    "Description": course_description,
                    "Is Paid": course_is_paid,
                    "Subscribers": subscribers,
                    "Average Rating": average_rating,
                    "Number of Reviews": num_reviews,
                    "Number of Lectures": num_lectures,
                    "Content Length": content_length,
                    "Last Update": last_update,
                    "Badges": badges,
                    "Course Language": course_language,
                    "Instructional Level": instructional_level,
                    "Authors": author_names,
                    "Course URL": course_url,
                    "Image URL": image_url,
                }

            # Increment the page number for the next iteration
            page += 1
        else:
            print(f"Failed to fetch data for page {page}. Status code:", response.status_code)
            break

    # Save the course data in a JSON file based on course name
    course_json_file = os.path.join(directory, f"{course_name}.json")
    with open(course_json_file, "w", encoding="utf-8") as json_file:
        json.dump(course_info, json_file, ensure_ascii=False, indent=4)

print("All course data saved successfully!")
