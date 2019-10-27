from selenium import webdriver

subject = "algorithms"
endRange = 4350
endNumber = 146
driver = webdriver.Chrome()
questionsReferences = []
try:
    driver.get("https://google.com")
    baseUrl = "https://gateoverflow.in/questions/" + subject + "?start="
    for index in range(0, endRange, 30):
        if index != 0:
            print("\nProgress ---> ", ((index / 30) / endNumber) * 100)
            print("\n Length", len(questionsReferences))
        try:
            driver.get(baseUrl + str(index))
            questionList = driver.find_element_by_class_name("qa-q-list")
            questionElement = questionList.find_elements_by_class_name("qa-q-list-item")
            for element in questionElement:
                questionsReferences.append(element.get_attribute("id"))
        except Exception as e:
            print(index, e, "IN LOOP")
            break
except Exception as e:
    print(e)
finally:
    # driver.quit()
    pass

import json

json.dump(questionsReferences, open(subject + ".json", "w"))

print(questionsReferences)
