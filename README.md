# dadata_testing  
## Testing API dadata.ru  
### Install GUIDE  

* `pipenv shell`
* `pipenv sync`
* Print command `pytest --html=report.html --self-contained-html`
* You'll see new report.html file. That is testing result.

### 
=============================================================================== short test summary info ===============================================================================
FAILED test_simple.py::test_response_200 - AssertionError: assert 'Unsupported Media Type' == 200
FAILED dadata_testing/test_dadata.py::test_response_200 - AssertionError: assert 'Unsupported Media Type' == 200
===================================================================== 2 failed, 22 passed, 16 warnings in 11.48s ======================================================================  
