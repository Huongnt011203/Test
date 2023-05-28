import pandas as pd

def get_list_test_case_login(path_data_test_login):
    df = pd.read_csv(path_data_test_login, sep=",", header=0)
    # df = pd.read_csv(path_data_test_login, sep=",", names=['No','Username','Password','Desired Result','Message'])
    data =[]
    for idx, row in df.iterrows():
        username = row['Username']
        password = row['Password']
        desired_result = row['Desired Result']
        message = row['Message']

        print(f"Username: {username}, Password: {password}, Desired Result: {desired_result}, Message: {message}")
        data.append(df.values.tolist())
        return data
    for row in data:
        # Sử dụng dữ liệu từ mỗi hàng
        value1 = row[0]
        value2 = row[1]
        value3 = row[2]
        value4 = row[3]
        value5 = row[4]

        print(row[0])
        return row


if __name__ == '__main__':
    path_data_test_login = r'D:\PycharmProjects\Login\dataTest\testok.csv'
    get_list_test_case_login(path_data_test_login)