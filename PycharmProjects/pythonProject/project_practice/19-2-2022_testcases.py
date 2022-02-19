

# def read_conval_file():
#     with open(r"C:\Users\Avinash\PycharmProjects\pythonProject\project_practice\log_data","r") as f:
#         print(f.read())
# read_conval_file()


# def read_conval_file(path):
#     with open(path,"r") as f:
#         print(f.read())
# path=r"C:\Users\Avinash\PycharmProjects\pythonProject\project_practice\log_data"
# read_conval_file(path)
import re


def get_product_string():
    data_string= r"C:\Users\Avinash\PycharmProjects\pythonProject\project_practice\log_data"
    with open(data_string,"r") as f:
        data= f.read()
        print(data)
        match =re.compile("language")
        pattern=match.search(data)






