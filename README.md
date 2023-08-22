# GIS-Dev-Interview
This repo contains technical questions for interviewing GIS developer candidates

## Instructions

## Python Questions
1.	Find all the Map Services at our USFS public facing EDW ArcGIS REST API
    - Use Python (> 3.0) to get a dictionary of all the Map services available here: [https://apps.fs.usda.gov/arcx/rest/services/EDW/](https://apps.fs.usda.gov/arcx/rest/services/EDW/)
    - The structure of the dictionary returned should be `{‘service name': {'type': service type, 'layers': [info from layer attribute]}}`
2.	From the service located here: [https://apps.fs.usda.gov/arcx/rest/services/EDW/EDW_ForestSystemBoundaries_01/MapServer/0](https://apps.fs.usda.gov/arcx/rest/services/EDW/EDW_ForestSystemBoundaries_01/MapServer/0) use Python to
    - Get an array of all the National Forests whose name starts with the letter `S`.
    - Get the count, as an integer, of all the National forests greater than 100,000 acres.
    
## JS/HTML/CSS - Use the sample starter in this project repo
1.  Write a CSS selector to find all divs whose CSS class is `container`.
2.	Modify above selector to find all divs whose CSS class is `container` that is also a child of a div with CSS class `header`.
3.	Modify above selector to find all the same divs that also have CSS class `enabled`.
4.  Assume you have a JS array of objects (structured as shown below). Add code in the `script.js` file to returns an array of people whose age is less than 50 and is not null. Log the resulting names to the console.
`const people = [{'name': 'Derek', 'age':38}, {'name': 'Erich', 'age':59},{'name': 'Kim', 'age':38},{'name': 'Sean', 'age': null}];`
5.	In the same `script.js` file, add code to iterate over each of those divs and output their ID properties to the console.


---
## Running Solutions

### Python Questions


**Run `gis_dev_interview.py`:**

```
▶ python starter-project/gis_dev_interview.py
```

- Question 1 will output to json file
- Question 2 will output to terminal

### JS/HTML/CSS Questions

- **Open Index.html in browser**
- **Console Logs available in browser Dev Tools**
