import xlrd

from db.db_dao import DBDao
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import numpy as np


class ComFunction(object):
    def __init__(self, *args, **kwargs):
        self.db = DBDao()

    # 创建获取信息方法
    def get_iphone_type(self):
        iphone_type_list = []
        iphone_type = self.db.get_iphone_type()
        if iphone_type:
            for item in iphone_type:
                iphone_type_list.append(list(item)[0])

        return iphone_type_list

    def get_iphone_storage(self):
        iphone_storage_list = []
        iphone_storage = self.db.get_iphone_storage()
        if iphone_storage:
            for item in iphone_storage:
                iphone_storage_list.append(list(item)[0])

        return iphone_storage_list

    def get_supply_company(self):
        supply_company_list = []
        supply_company = self.db.get_supply_company()
        if supply_company:
            for item in supply_company:
                supply_company_list.append(list(item)[0])

        return supply_company_list

    def get_case_status(self):
        case_status_list = []
        case_status = self.db.get_case_status()
        if case_status:
            for item in case_status:
                case_status_list.append(list(item)[0])

        return case_status_list

    def get_problems(self):
        problems_list = []
        problem = self.db.get_problems()
        if problem:
            for item in problem:
                problems_list.append(list(item)[0])

        return problems_list

    def get_lot_num(self):
        lot_num_list = []
        lot_num = self.db.get_lot_nums()
        if lot_num:
            for item in lot_num:
                lot_num_list.append(list(item)[0])

        return lot_num_list

    def get_operation(self):
        operation_list = []
        operation = self.db.get_operation()
        if operation:
            for item in operation:
                operation_list.append(list(item)[0])

        return operation_list

    def get_responsible(self):
        responsible_list = []
        responsible = self.db.get_responsible()
        if responsible:
            for item in responsible:
                responsible_list.append(list(item)[0])

        return responsible_list

    def set_iphone_type(self, comboBox, iphone_type_list):
        # iphone_type_list = self.get_iphone_type()
        comboBox.clear()
        if iphone_type_list:
            for i in range(len(iphone_type_list)):
                comboBox.addItem(iphone_type_list[i])

    def set_iphone_storage(self, comboBox, iphone_storage_list):
        # iphone_type_list = self.get_iphone_type()
        comboBox.clear()
        if iphone_storage_list:
            for i in range(len(iphone_storage_list)):
                comboBox.addItem(iphone_storage_list[i])

    def set_supply_company(self, comboBox):
        supply_company_list = self.get_supply_company()
        comboBox.clear()
        if supply_company_list:
            for i in range(len(supply_company_list)):
                comboBox.addItem(supply_company_list[i])

    def set_case_status(self, comboBox):
        case_status_list = self.get_case_status()
        comboBox.clear()
        if case_status_list:
            for i in range(len(case_status_list)):
                comboBox.addItem(case_status_list[i])

    def set_problems(self, comboBox):
        problems_list = self.get_problems()
        comboBox.clear()
        if problems_list:
            for i in range(len(problems_list)):
                comboBox.addItem(problems_list[i])

    def set_lot_num(self, comboBox):
        lot_num_list = self.get_lot_num()
        comboBox.clear()
        if lot_num_list:
            for i in range(len(lot_num_list)):
                comboBox.addItem(lot_num_list[i])

    def set_operation(self, comboBox):
        operation_list = self.get_operation()
        comboBox.clear()
        if operation_list:
            for i in range(len(operation_list)):
                comboBox.addItem(operation_list[i])

    def set_responsible(self, comboBox):
        responsible_list = self.get_responsible()
        comboBox.clear()
        if responsible_list:
            for i in range(len(responsible_list)):
                comboBox.addItem(responsible_list[i])

    def check_item(self, supply_company, iphone_type, problem, operation, responsible, iphone_storage):
        """
        # 创建方法查询输入信息是否存在数据库中，若不存在则添加
        :return:
        """
        item_dict = {
            "supply_company": supply_company,
            "iphone_type": iphone_type,
            "problem": problem,
            "case_operations": operation,
            "responsible": responsible,
            "iphone_storage": iphone_storage,
        }
        self.db.check_item(item_dict)

    def get_table_widget_item(self, table_widget):
        """
        获取table widget中的信息
        :return:
        """
        table_widget_item_list = []

        row_count = table_widget.rowCount()
        column_count = table_widget.columnCount()
        for row in range(row_count):
            value_list = []
            if table_widget.item(row, 0):
                for column in range(column_count):
                    value = table_widget.item(row, column).text()
                    value_list.append(value)

                table_widget_item_list.append(value_list)

        return table_widget_item_list

    def search_function(self, *args, **kwargs):
        print("zhixing cha")


    def open_file(self):
        openfile_name = QFileDialog.getOpenFileName(caption='select file', directory='',
                                                    filter='Excel files(*.xlsx , *.xls)', initialFilter='')
        path_openfile_name = openfile_name[0]
        IEMI_list = []
        print(path_openfile_name)
        if path_openfile_name:

            wb = xlrd.open_workbook(path_openfile_name)
            sheet1 = wb.sheets()[0]
            sheet1_rows = sheet1.nrows
            print(sheet1_rows)
            for row in range(sheet1_rows):
                value = str(int(sheet1.row(row)[0].value))
                IEMI_list.append(value)
        print(IEMI_list)

        return path_openfile_name, IEMI_list


