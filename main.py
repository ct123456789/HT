# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pytest

if __name__ == '__main__':
    pytest.main(["./", "--alluredir=./report/result"])
    os.system(f"allure generate report/result -o report/allure_html --clean")
