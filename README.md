<b><H1>Analysis of the socio-demographic composition of people in images in job advertisements using computer vision tools.</H1></b>
<b><H2>All documents, codes, analysis related to the project - "Analysis of the socio-demographic composition of people in images in job advertisements using computer vision tools." are stored in this repository.</H2></b>

<b><H3>Project Overview:</H3></b>

<b><H3>Project description</H3></b>
In a research project, we are investigating technologies in the field of HR to determine whether they promote discrimination risks, especially in hiring processes for trainees. Within the scope of this project, an image analysis of job advertisements is to be carried out. Using state of the art computer vision algorithms, the socio-demographic composition of persons on images in job advertisements is to be analyzed. 

<b><H3>Project tasks</H3></b>
For this purpose, first a survey of currently available tools is required, such as Amazon Recognition. It should be evaluated, what features are inferred by the software (e.g. gender, skin tone, facial expression, age etc.), and under what conditions the software can be used (license, cost, APIs, etc.).

Second, the selected tools should be assessed regarding their potential biases, e.g. a performance loss on certain population subgroups. For this purpose, research shall first be conducted to find out what experiences have been made in the use of the software with regard to bias. If necessary, the bias potential shall be estimated on the basis of a selected data set that needs to be composed using real-world images for exactly this purpose. 

In a third step, a Python script is needed that:

1. Crawls the platform Ausbildung.de and stores the text information, preserving as much of the structural information as possible. By structural information we mean the assignment of text to the sections / paragraphs of the text (see the images attached). 

2. In a second step, the crawler should be extended so that it extracts information from the images in near-time, without storing the image material.

3. The script should be run to crawl all jobs listed on the website (approx. 10,000). We can provide access to the AWS cloud for this purpose. The data can be stored in a CSVfile since the amount of data is expected to be rather small (up to 15,000). Existing Python code can be provided for this purpose.

<b><H3>Skills and technologies required or learned</H3></b>

Data Science; Machine Learning; Programming (Python); Web Scraping

<b><H3>Facial Recognition Software: Azure Face API</H3></b>
<b><H3>Azure Face API attributes documentation: https://docs.microsoft.com/en-us/azure/cognitive-services/face/concepts/face-detection</H3></b>
