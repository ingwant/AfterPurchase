# coding: UTF-8
import time
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QDialog
from PyQt5 import QtCore, QtWidgets, QtGui
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTreeWidgetItem

from db.db_dao import DBDao
from UI.case_info import Ui_Dialog as case_info


class CaseInfo(QDialog):
    def __init__(self, *args, **kwargs):
        super(CaseInfo, self).__init__()
        self.case_info = case_info()
        self.case_info.setupUi(self)

        self.db = DBDao()

        print(args)

        self.value_list = list(args)[0]
        self.case_num = self.case_info.credit_lineEdit_1_1
        self.lot_num = self.case_info.lot_num_lineEdit_1_0
        self.in_time = self.case_info.credit_lineEdit_1_2
        self.supply_company = self.case_info.lot_num_lineEdit_1_1
        self.credit_num = self.case_info.lot_num_lineEdit_1_2
        self.amount = self.case_info.lot_num_lineEdit_1_3
        self.status = self.case_info.lineEdit_14
        self.responsible = self.case_info.lineEdit_13
        self.create_time = self.case_info.credit_lineEdit_1_3
        self.bad_count = self.case_info.count_lineEdit_0_1
        self.bad_rate = self.case_info.count_lineEdit_0_2
        self.tableWidget = self.case_info.tableWidget

        self.set_date()
        self.show_iphone_list_table()

    def get_amount(self):
        lot_num = self.value_list[3]
        result = self.db.get_receipt_amount(lot_num)

        amount_list = []
        for amount in result:
            amount_list.append(int(list(amount)[0]))
        amount = sum(amount_list)
        credit_num = list(result[0])[1]

        return amount, credit_num

    def set_date(self):
        amount, credit_num = self.get_amount()
        self.case_num.setText(self.value_list[0])
        self.lot_num.setText(self.value_list[3])
        self.in_time.setText(self.value_list[1])
        self.supply_company.setText(self.value_list[4])
        self.credit_num.setText(credit_num)
        self.amount.setText(str(amount))
        self.status.setText(self.value_list[9])
        self.responsible.setText(self.value_list[10])
        self.create_time.setText(self.value_list[2])
        self.bad_count.setText(self.value_list[5])
        self.bad_rate.setText(self.value_list[6])

        # self.iphone_info_list = self.case_info.tableWidget

    def show_iphone_list_table(self):
        case_num = self.value_list[0]
        results = self.db.get_iphone_info_table(case_num)
        if results:
            row_count = len(results)
            self.tableWidget.setRowCount(row_count)

            for row, item in enumerate(results):
                for column, value in enumerate(list(item)):
                    value = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, column, value)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CaseInfo()
    ui.show()
    sys.exit(app.exec_())
