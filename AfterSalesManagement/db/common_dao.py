from db.mysql_pool import pool
import json
from UI.saleV3 import Ui_MainWindow


class CommonDao:
    # 创建通用修改方法
    def __init__(self):
        self.UI = Ui_MainWindow()

    def change_option(self, sql):
        global con
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            cursor.execute(sql)
            # result = cursor.fetchall()
            con.commit()

        except Exception as e:
            # print("添加失败")
            # 操作失败
            con.rollback()
            return e
        finally:
            con.close()

    def search_option(self, sql):
        global con
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            return e
        finally:
            con.close()

    def get_local_data(self, table_name):
        # 当数据库连接不上时，读取本地数据
        message = "连接数据失败，读取本地文件。"
        # self.UI.statusbar.showMessage(message)
        info_list = []
        print("打开本地文件")
        try:
            with open(f"./static/config/{table_name}.json", "r", encoding="utf-8") as info_file:
                info = json.load(info_file)
                for value in info.values():
                    value_tuple = (value, )
                    info_list.append(value_tuple)

                return info_list
        except Exception as e:
            # 异常处理
            # print(e)
            pass


    # def get_iphone_type(self):
    #     try:
    #         sql = "SELECT iphonetype FROM trillion.iphonetype;"
    #         iphone_type = self.search_option(sql)
    #     except Exception:
    #         iphone_type = self.get_local_data("iphonetype")
    #     finally:
    #         # 获取数据库及本地文件错误，异常处理
    #         pass
    #     return iphone_type

    # def get_iphone_color(self):
    #     try:
    #         sql = "SELECT iphonecolor FROM trillion.iphoneclor;"
    #         iphone_color = self.search_option(sql)
    #         if iphone_color is list:
    #             return iphone_color
    #         else:
    #             iphone_color = self.get_local_data("iphonecolor")
    #             return iphone_color
    #     except Exception:
    #         pass
    #     finally:
    #         # 获取数据库及本地文件错误，异常处理
    #         pass