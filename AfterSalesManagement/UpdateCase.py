# coding: UTF-8
import time
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QDialog
from PyQt5 import QtCore, QtWidgets, QtGui
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTreeWidgetItem

from db.db_dao import DBDao

from UI.update_case import Ui_Dialog as update_case
from ComFunction import ComFunction
from SignalSlot import eventMonitor


class UpdateCase(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateCase, self).__init__()
        self.update_case = update_case()
        self.update_case.setupUi(self)

        # 导入包实例化
        self.db = DBDao()
        self.com_function = ComFunction()
        self.monitorObj = eventMonitor()

        # 定义参数
        self.change_time = self.update_case.in_dateEdit_1_0
        self.case_num = self.update_case.credit_lineEdit_1_1
        self.lot_num = self.update_case.lot_num_lineEdit_1_0
        self.status = self.update_case.status_comboBox_0_2
        self.RMA_num = self.update_case.RMA_num_lineEdit_0_2
        self.tracking_number = self.update_case.return_lineEdit_0_2
        self.operation = self.update_case.type_comboBox_1_1
        self.feedback = self.update_case.credit_lineEdit_1_7
        self.tableWidget = self.update_case.tableWidget
        self.approve_price = self.update_case.credit_lineEdit_1_4
        self.IEMI = self.update_case.credit_lineEdit_1_5
        self.file_name = self.update_case.credit_lineEdit_1_2
        self.checkBox = self.update_case.checkBox
        self.amount = self.update_case.credit_lineEdit_1_3
        self.selected_amount = self.update_case.credit_lineEdit_1_8
        self.remark = self.update_case.credit_lineEdit_1_6
        self.update_pushButton = self.update_case.change_pushButton_0_2
        self.again_pushButton = self.update_case.again_pushButton_0_2
        self.import_data_pushButton = self.update_case.pushButton_7
        self.change_parameter_pushButton = self.update_case.pushButton
        self.refresh_pushButton = self.update_case.refresh_pushButton_0_1


        self.plainTextEdit = self.update_case.plainTextEdit
        self.in_amount_lineEdit = self.update_case.lineEdit
        self.add_IEMI_pushButton = self.update_case.pushButton_8
        self.clear_IEMI_pushButton = self.update_case.pushButton_9

        # 设置tableWidget的行数
        # self.tableWidget.setRowCount(999)

        # pushButton事件关联，更新数据
        self.update_pushButton.clicked.connect(self.update_info)
        # 重置数据按钮关联事件
        self.again_pushButton.clicked.connect(self.clear_items)
        # 设置导入文件按钮事件
        self.import_data_pushButton.clicked.connect(self.open_file)
        # 设置checkBox 的关联信号
        self.checkBox.stateChanged.connect(self.all_bool_checked)
        # 修改参数
        self.change_parameter_pushButton.clicked.connect(self.change_parameter)

        self.tableWidget.cellChanged.connect(self.get_selected_amount)

        self.refresh_pushButton.clicked.connect(self.show_iphone_list_table)

        self.clear_IEMI_pushButton.clicked.connect(lambda: self.com_function.clear_plainTextEdit(self.plainTextEdit))

        self.plainTextEdit.textChanged.connect(lambda :self.com_function.set_IEMI_input_amount(self.plainTextEdit,self.in_amount_lineEdit))

        self.add_IEMI_pushButton.clicked.connect(self.checked_import_data_by_input)


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/sinchronize-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/redo-2-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.again_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/excel-3-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_data_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/parallel-tasks-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_parameter_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/sinchronize-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/arrow-96-48.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_IEMI_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/x-mark-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_IEMI_pushButton.setIcon(icon)

        # 设置字体
        # font = QtGui.QFont()
        # font.setFamily("黑体")
        # font.setPointSize(10)
        # self.feedback.setFont(font)

        self.monitorObj.EnterKeyPressed.connect(self.set_row_selected_by_IEMI)  # 连接自定义信号和槽
        self.monitorObj.EnterKeyPressed.connect(self.get_selected_amount)  # 连接自定义信号和槽
        self.IEMI.installEventFilter(self.monitorObj)  # 对tableWidget安装事件监控

        value_list = list(args)[0]

        self.change_time.setDisplayFormat("yyyy-MM-dd")
        self.change_time.setDate(QtCore.QDate.currentDate())

        self.com_function.set_case_status(self.status)
        self.com_function.set_operation(self.operation)

        self.status.setCurrentText(value_list[10])
        self.case_num.setText(value_list[0])
        self.lot_num.setText(value_list[3])
        self.RMA_num.setText(value_list[8])
        self.tracking_number.setText(value_list[9])

        self.show_iphone_list_table()

    # def enterKeyPressed(self):  # 回车键按键响应槽函数
    #     status = self.status.currentText()
    #     operation = self.operation.currentText()
    #     feedback = self.feedback.text()
    #     change_time = self.change_time.text()
    #     remark = self.remark.text()
    #     approve_price = self.approve_price.text()
    #
    #     info_list = [operation,feedback,change_time,approve_price,remark]
    #     self.check_item()
    #
    #     value_dict = {
    #         "状态": status,
    #         "处理方式": operation,
    #     }
    #
    #     result = self.check_item_input(value_dict)
    #     if result == 1024:
    #         return
    #     else:
    #         try:
    #
    #             for i, item in enumerate(info_list):
    #                 column = i
    #                 item = QTableWidgetItem(str(item))
    #                 if i == 0 or i == 1 or i == 2:
    #                     self.tableWidget.setItem(currentRow, column + 4, item)
    #                 else:
    #                     self.tableWidget.setItem(currentRow, column + 5, item)
    #             self.set_row_selected_by_IEMI()
    #
    #         except:
    #             pass

    def check_item_input(self, value_dict):
        """
        检出各个输入项是否为空
        :param value_dict:
        :return:
        """
        for key, value in value_dict.items():
            if value == "":
                self.check_box = QMessageBox.information(self, '提示', f"请输入{key}", QMessageBox.Ok)
                return self.check_box

    def check_item(self):
        """
        创建方法判断输入信息是否存在
        :return:
        """
        supply_company = ''
        iphone_type = ''
        problem = ''
        responsible = ''
        iphone_storage = ''
        operation = self.operation.currentText()

        self.com_function.check_item(supply_company, iphone_type, problem, operation, responsible, iphone_storage)

    def get_current_text(self):
        try:
            currentRow = self.tableWidget.currentRow()
            current_text = self.tableWidget.item(currentRow - 1, 0).text()
            print(current_text)

            # 获取对应的iphone type 和 lot num
            result = self.db.get_lot_type(current_text)
            print(result)
            iphone_type = list(result[0])[0]
            problem = list(result[0])[1]

            info = [iphone_type, problem]
            for i, item in enumerate(info):
                item = QTableWidgetItem(str(item))
                self.tableWidget.setItem(currentRow - 1, i + 1, item)
        except:
            pass

    def update_info(self):
        case_id = self.case_num.text()
        lot_num = self.lot_num.text()
        status = self.status.currentText()
        RMA_num = self.RMA_num.text()
        tracking_num = self.tracking_number.text()

        try:
            # 更新case表
            self.db.update_case_table(RMA_num, tracking_num, status, case_id)
        except:
            QMessageBox.information(self, '提示', "更新统计单失败。", QMessageBox.Ok)
            return
        try:
            # 更新info table
            table_widget_item_list = []

            row_count = self.tableWidget.rowCount()
            column_count = self.tableWidget.columnCount()
            for row in range(row_count):
                value_list = []
                state = self.check_row_state(row)
                if state == QtCore.Qt.Checked:
                    for column in range(column_count):
                        value = self.tableWidget.item(row, column).text()
                        value_list.append(value)

                    table_widget_item_list.append(value_list)
                else:
                    continue
            if table_widget_item_list:
                for item in table_widget_item_list:
                    IEMI = item[0]
                    operation = item[4]
                    feedback = item[5]
                    change_time = item[6]
                    approve_price = item[8]
                    remark = item[9]
                    result = self.db.update_iphone_info(operation, change_time, feedback, approve_price, remark, IEMI)
                    if result:
                        QMessageBox.information(self, '提示', "更新失败。", QMessageBox.Ok)
                        # self.show_iphone_list_table()
                        return
                    else:
                        continue
                check_box = QMessageBox.information(self, '提示', "更新成功。", QMessageBox.Ok)
                if check_box == QMessageBox.Ok:
                    self.show_iphone_list_table()
            else:
                QMessageBox.information(self, '提示', "信息更新前请先进行选择。", QMessageBox.Ok)
                return
        except:
            QMessageBox.information(self, '提示', "更新失败。", QMessageBox.Ok)
            return

    def close_window(self):
        self.close()

    def clear_items(self):
        self.operation.clearEditText()
        self.feedback.clear()
        self.remark.clear()
        self.approve_price.clear()
        self.IEMI.clear()
        self.file_name.clear()

    def open_file(self):
        self.show_iphone_list_table()
        path_openfile_name, IEMI_list = self.com_function.open_file()
        if path_openfile_name:
            file_name = path_openfile_name.split("/")[-1]

            self.file_name.setText(file_name)
            if IEMI_list:
                IEMI_list = list(set(IEMI_list))
                self.selected_amount.setText(str(len(IEMI_list)))

                self.checked_import_data(IEMI_list)

    def checked_import_data(self, IEMI_list):

        tableWidget_IEMI_list = []

        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            tableWidget_IEMI = self.tableWidget.item(row, 0).text()
            tableWidget_IEMI_list.append(tableWidget_IEMI)

        # 不存在数据库中的信息
        no_find_IEMI_list = list(set(IEMI_list).difference(set(tableWidget_IEMI_list)))
        print(IEMI_list)
        print(tableWidget_IEMI_list)
        print("no_find_IEMI_list",no_find_IEMI_list)

        # 需要选择的信息列表

        select_IEMI_lit = list(set(IEMI_list).intersection(set(tableWidget_IEMI_list)))
        if select_IEMI_lit:
            for IEMI in select_IEMI_lit:
                row_count = self.tableWidget.rowCount()
                for row in range(row_count):
                    tableWidget_IEMI = self.tableWidget.item(row, 0).text()
                    if IEMI == tableWidget_IEMI:
                        self.checked_table_row(row)
                    else:
                        continue

        if no_find_IEMI_list:
            QMessageBox.information(self, "提示", f"未录入IEMI列表:\n{no_find_IEMI_list}", QMessageBox.Ok)

        # self.change_parameter()

    def checked_import_data_by_input(self):
        IEMI_list = self.com_function.get_IEMI_list(self.plainTextEdit)
        self.checked_import_data(IEMI_list)


    def show_iphone_list_table(self):
        # 显示table widget
        self.checkBox.setChecked(False)
        case_num = self.case_num.text()
        results = self.db.get_iphone_info_table(case_num)
        if results:
            row_count = len(results)
            self.amount.setText(str(row_count))
            self.tableWidget.setRowCount(row_count)

            for row, item in enumerate(results):
                for column, value in enumerate(list(item)):
                    value = QTableWidgetItem(str(value))
                    if column == 0:
                        value.setCheckState(False)
                        self.tableWidget.setItem(row, column, value)
                    else:
                        self.tableWidget.setItem(row, column, value)

    def all_bool_checked(self, state):
        self.checkBox = self.sender()
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            if state == QtCore.Qt.Unchecked:
                self.uncheck_table_row(row)
            elif state == QtCore.Qt.Checked:
                self.checked_table_row(row)
        self.get_selected_amount()

    def single_bool_checked(self, row):
        self.check_row_state(row)

    def uncheck_table_row(self, row):
        # 显示table widget 不选择
        self.tableWidget.item(row, 0).setCheckState(QtCore.Qt.Unchecked)

    def checked_table_row(self, row):
        # 显示table widget 选中
        self.tableWidget.item(row, 0).setCheckState(QtCore.Qt.Checked)

    def check_row_state(self, row):
        try:
            state = self.tableWidget.item(row, 0).checkState()
            return state
        except:
            pass

    def set_row_selected_by_IEMI(self):
        input_IEMI = self.IEMI.text().strip()
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            tableWidget_IEMI = self.tableWidget.item(row, 0).text()
            if input_IEMI == tableWidget_IEMI:
                self.checked_table_row(row)
            else:
                continue

    def get_selected_amount(self):
        selected_amount = 0
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            state = self.check_row_state(row)
            if state == QtCore.Qt.Unchecked:
                continue
            elif state == QtCore.Qt.Checked:
                selected_amount += 1
        self.selected_amount.setText(str(selected_amount))

    def change_parameter(self):
        status = self.status.currentText()
        operation = self.operation.currentText()
        feedback = self.feedback.text()
        change_time = self.change_time.text()
        remark = self.remark.text()
        approve_price = self.approve_price.text()

        info_list = [operation, feedback, change_time, approve_price, remark]
        self.check_item()

        value_dict = {
            "状态": status,
        }

        result = self.check_item_input(value_dict)
        if result == 1024:
            return
        else:
            try:
                row_count = self.tableWidget.rowCount()

                for currentRow in range(row_count):
                    state = self.check_row_state(currentRow)
                    if state == QtCore.Qt.Checked:
                        for i, item in enumerate(info_list):
                            column = i
                            if item == "":
                                continue
                            else:
                                item = QTableWidgetItem(str(item))
                                if i == 0 or i == 1 or i == 2:
                                    self.tableWidget.setItem(currentRow, column + 4, item)
                                else:
                                    self.tableWidget.setItem(currentRow, column + 5, item)
                    elif state == QtCore.Qt.Unchecked:
                        continue
            except:
                pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UpdateCase()
    ui.show()
    sys.exit(app.exec_())
