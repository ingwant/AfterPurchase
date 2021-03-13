# coding: UTF-8
import time
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QDialog, QHeaderView, QDesktopWidget
from PyQt5 import QtCore, QtWidgets, QtGui
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTreeWidgetItem

from UI.saleV3 import Ui_MainWindow as main_ui
from ComFunction import ComFunction
from db.db_dao import DBDao
from SignalSlot import eventMonitor
from CaseInfo import CaseInfo
from UpdateCase import UpdateCase


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_ui = main_ui()
        self.main_ui.setupUi(self)

        self.row_count = 1
        self.amount = 0
        self.bad_amount = 0
        self.bad_rate_str = ''

        # 实例化导入的包
        self.db = DBDao()
        self.com_fun = ComFunction()
        self.monitorObj = eventMonitor()
        self.monitorObj_2 = eventMonitor()

        # 主界面窗口参数
        self.stackedWidget = self.main_ui.stackedWidget

        self.create_case_pushbutton = self.main_ui.CheckCountPB
        self.search_case_pushbutton = self.main_ui.ProductSearchPB
        self.search_receipt_pushbutton = self.main_ui.ProductSearchPB_2

        self.search_case_pushbutton.setChecked(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/add-list-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_case_pushbutton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/search-3-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_case_pushbutton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/search-5-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_receipt_pushbutton.setIcon(icon)

        self.create_case_pushbutton.clicked.connect(lambda: self.on_clicked(self.create_case_pushbutton))
        self.search_case_pushbutton.clicked.connect(lambda: self.on_clicked(self.search_case_pushbutton))
        self.search_receipt_pushbutton.clicked.connect(lambda: self.on_clicked(self.search_receipt_pushbutton))

        self.receipt_info = self.main_ui.tableWidget_1_1
        # 创建统计单页面参数
        self.in_time_dateEdit_0 = self.main_ui.in_dateEdit_1_0
        self.lot_num_lineEdit_0 = self.main_ui.lot_num_lineEdit_1_0
        self.supply_company_comboBox_0 = self.main_ui.supply_comboBox_1_0
        self.credit_num_lineEdit_0 = self.main_ui.credit_lineEdit_1_0
        self.iphone_type_comboBox_0_1 = self.main_ui.type_comboBox_1_0
        self.amount_spinBox_0 = self.main_ui.actual_count_spinBox_1_0
        self.add_iphone_type_pushButton_0 = self.main_ui.pushButton
        self.type_tableWidget_0 = self.main_ui.tableWidget
        self.create_time_dateEdit_0 = self.main_ui.dateEdit_5
        self.responsible_lineEdit_0 = self.main_ui.type_comboBox_1_3
        self.case_id_lineEdit_0 = self.main_ui.credit_lineEdit_1_1
        self.create_case_id_pushButton_0 = self.main_ui.pushButton_2
        self.operations_comboBox_0 = self.main_ui.type_comboBox_1_1
        self.problems_comboBox_0 = self.main_ui.comboBox_2
        self.iphone_type_comboBox_0_2 = self.main_ui.comboBox_4
        self.get_iphone_type_pushButton_0 = self.main_ui.pushButton_3
        self.iphone_info_tableWidget_0 = self.main_ui.tableWidget_2
        self.clear_pushButton_0 = self.main_ui.pushButton_6
        self.import_data_pushButton = self.main_ui.pushButton_7

        self.iphone_storage_comboBox_0_1 = self.main_ui.type_comboBox_1_2
        self.iphone_storage_comboBox_0_2 = self.main_ui.comboBox_3
        self.apply_price_lineEdit_0 = self.main_ui.credit_lineEdit_1_4
        self.remark_lineEdit_0 = self.main_ui.credit_lineEdit_1_5
        self.amount_lineEdit_0 = self.main_ui.credit_lineEdit_1_3
        self.file_name_lineEdit_0 = self.main_ui.credit_lineEdit_1_2

        # 设置IEMI复制粘贴输入框
        self.plainTextEdit = self.main_ui.plainTextEdit
        self.in_amount_lineEdit = self.main_ui.lineEdit
        self.add_IEMI_pushButton = self.main_ui.pushButton_8
        self.clear_IEMI_pushButton = self.main_ui.pushButton_9

        self.plainTextEdit.textChanged.connect(
            lambda: self.com_fun.set_IEMI_input_amount(self.plainTextEdit, self.in_amount_lineEdit))
        self.add_IEMI_pushButton.clicked.connect(self.set_data_by_input)

        self.iphone_info_tableWidget_0.setRowCount(999)
        self.type_tableWidget_0.setRowCount(1)

        self.create_case_pushButton_0_1 = self.main_ui.pushButton_5
        self.create_case_pushButton_0_2 = self.main_ui.pushButton_4

        # 设置时间选择框格式及显示当前时间
        self.in_time_dateEdit_0.setDisplayFormat("yyyy-MM-dd")
        self.in_time_dateEdit_0.setDate(QtCore.QDate.currentDate())
        self.create_time_dateEdit_0.setDisplayFormat("yyyy-MM-dd")
        self.create_time_dateEdit_0.setDate(QtCore.QDate.currentDate())

        # 设置下拉选择框参数
        iphone_type = self.com_fun.get_iphone_type()
        iphone_storage = self.com_fun.get_iphone_storage()
        self.com_fun.set_supply_company(self.supply_company_comboBox_0)
        self.com_fun.set_iphone_type(self.iphone_type_comboBox_0_1, iphone_type)
        self.com_fun.set_iphone_storage(self.iphone_storage_comboBox_0_1, iphone_storage)
        self.com_fun.set_operation(self.operations_comboBox_0)
        self.com_fun.set_problems(self.problems_comboBox_0)
        self.com_fun.set_responsible(self.responsible_lineEdit_0)

        self.clear_pushButton_0.clicked.connect(self.clear_tableWidget)
        self.add_iphone_type_pushButton_0.clicked.connect(self.create_iphone_type_list)
        self.add_iphone_type_pushButton_0.clicked.connect(self.check_item)
        self.get_iphone_type_pushButton_0.clicked.connect(self.get_type_list_item)
        self.clear_IEMI_pushButton.clicked.connect(lambda: self.com_fun.clear_plainTextEdit(self.plainTextEdit))

        # 设置lot num 默认参数
        default_lot_num = time.strftime("%Y%m%d-", time.localtime())[2:]
        self.lot_num_lineEdit_0.setText(default_lot_num)

        self.lot_num_lineEdit_0.setPlaceholderText("格式 年月日:210101-lot num")

        self.monitorObj.EnterKeyPressed.connect(self.enterKeyPressed)  # 连接自定义信号和槽
        self.iphone_info_tableWidget_0.installEventFilter(self.monitorObj)  # 对tableWidget安装事件监控

        # 创建信号槽，查询入库单信息
        self.monitorObj_2.EnterKeyPressed.connect(self.check_receipt_info)
        self.lot_num_lineEdit_0.installEventFilter(self.monitorObj_2)

        self.create_case_pushButton_0_1.clicked.connect(self.create_case_page_info)
        self.create_case_pushButton_0_2.clicked.connect(self.create_case_page_info)
        self.create_case_id_pushButton_0.clicked.connect(self.show_case_id)
        self.import_data_pushButton.clicked.connect(self.open_file)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/check-mark-3-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_case_pushButton_0_1.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/check-mark-3-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_case_pushButton_0_2.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/database-5-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.get_iphone_type_pushButton_0.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/add-row-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_iphone_type_pushButton_0.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/warning-38-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_pushButton_0.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/sinchronize-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_case_id_pushButton_0.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/excel-3-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_data_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/arrow-96-48.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_IEMI_pushButton.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/x-mark-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_IEMI_pushButton.setIcon(icon)

        # 查询统计单页面参数
        self.create_time_checkBox_1 = self.main_ui.checkBox_2
        self.create_time_dateEdit_1 = self.main_ui.create_dateEdit_0_1
        self.supply_company_comboBox_1 = self.main_ui.supply_comboBox_0_1
        self.lot_num_comboBox_1 = self.main_ui.lot_num_comboBox_0_1
        self.status_comboBox_1 = self.main_ui.status_comboBox_0_1
        self.again_pushButton_1 = self.main_ui.again_pushButton_0_1
        self.search_pushButton_1 = self.main_ui.search_pushButton_0_1
        self.refresh_pushButton_1 = self.main_ui.refresh_pushButton_0_1
        self.amount_lineEdit_1 = self.main_ui.count_lineEdit_0_1
        self.case_info_tableWidget_1 = self.main_ui.tableWidget_0_1
        self.search_IEMI_comboBox_1 = self.main_ui.supply_comboBox_0_2
        self.search_credit_lineEdit = self.main_ui.credit_lineEdit_1_6

        self.create_time_dateEdit_1.setDisplayFormat("yyyy-MM-dd")
        self.create_time_dateEdit_1.setDate(QtCore.QDate.currentDate())

        self.com_fun.set_supply_company(self.supply_company_comboBox_1)
        self.com_fun.set_case_status(self.status_comboBox_1)

        self.search_pushButton_1.clicked.connect(self.show_search_cases_table)
        self.again_pushButton_1.clicked.connect(self.again_case)
        # self.case_info_tableWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.case_info_tableWidget_1.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.refresh_pushButton_1.clicked.connect(self.show_cases_table)

        self.show_cases_table()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/sinchronize-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_pushButton_1.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/search-5-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_pushButton_1.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/redo-2-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.again_pushButton_1.setIcon(icon)

        # 查询入库单页面参数
        self.in_time_checkBox_2 = self.main_ui.checkBox
        self.in_time_dateEdit_2 = self.main_ui.in_dateEdit_1_1
        self.lot_num_comboBox_2 = self.main_ui.lot_num_comboBox_1_1
        self.supply_company_comboBox_2 = self.main_ui.supply_comboBox_1_1
        self.again_pushButton_2 = self.main_ui.again_pushButton_1_1
        self.search_receipt_pushbutton_2 = self.main_ui.search_pushButton_1_1
        self.refresh_pushButton_2 = self.main_ui.refresh_pushButton_1_1
        self.amount_lineEdit_2 = self.main_ui.count_lineEdit_1_1
        self.receipt_info = self.main_ui.tableWidget_1_1

        self.in_time_dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.in_time_dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.again_pushButton_2.clicked.connect(self.again_receipt)
        self.search_receipt_pushbutton_2.clicked.connect(self.search_case)

        self.com_fun.set_supply_company(self.supply_company_comboBox_2)

        self.refresh_pushButton_2.clicked.connect(self.show_receipt_table)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/sinchronize-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_pushButton_2.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/search-5-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_receipt_pushbutton_2.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/redo-2-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.again_pushButton_2.setIcon(icon)

    def center(self):  # 定义一个函数使得窗口居中显示
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop) - 30)

    # 定义方法用于切换窗口
    def on_clicked(self, pushbutton):
        # 获取按钮文本(去除两边空格)
        text = pushbutton.text().strip()
        if text == "创建统计单":
            self.on_pushButton1_clicked()
        elif text == "查询统计单":
            self.on_pushButton2_clicked()
        elif text == "查询入库单":
            self.on_pushButton3_clicked()

    # 创建面板显示
    # 按钮一：打开第一个面板
    def on_pushButton1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    # 按钮二：打开第二个面板
    def on_pushButton2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.show_cases_table()

    # 按钮三：打开第三个面板
    def on_pushButton3_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.show_receipt_table()

    # 设置显示iphone type
    def set_iphone_type(self):
        iphone_type_list = self.com_fun.get_iphone_type()
        self.iphone_type_comboBox_0_1.clear()

        for i in range(len(iphone_type_list)):
            self.iphone_type_comboBox_0_1.addItem(iphone_type_list[i])

    def create_iphone_type_list(self):
        """
        创建生成机型列表
        :return:
        """
        iphone_type = self.iphone_type_comboBox_0_1.currentText()
        iphone_storage = self.iphone_storage_comboBox_0_1.currentText()
        value_dict = {
            "手机型号": iphone_type,
            "手机内存": iphone_storage,
        }

        result = self.check_item_input(value_dict)
        if result == 1024:
            return
        else:
            iphone_type = self.iphone_type_comboBox_0_1.currentText()
            iphone_storage = self.iphone_storage_comboBox_0_1.currentText()
            amount = self.amount_spinBox_0.text()

            value_list = [iphone_type, iphone_storage, amount]
            self.show_table_widget(value_list, self.type_tableWidget_0)

    def show_table_widget(self, value_list, table_widget):
        """
        展示机型列表方法
        :param iphone_type:
        :param amount:
        :return:
        """
        # 判断添加的参数是否已经存在，若存在则修改对应参数
        row_count = table_widget.rowCount()
        for row in range(row_count - 1):
            if value_list[0] == table_widget.item(row, 0).text():
                if value_list[1] == table_widget.item(row, 1).text():
                    value = QTableWidgetItem(str(value_list[2]))
                    table_widget.setItem(row, 2, value)
                    return
                else:
                    continue
            else:
                continue

        # 不存在则新建
        # 判断是否存在值

        if table_widget.item(row_count, 0) == None:
            for column, item in enumerate(value_list):
                value = QTableWidgetItem(str(item))
                table_widget.setItem(row_count - 1, column, value)

            row_count += 1
            table_widget.setRowCount(row_count)

    def clear_tableWidget(self):
        self.type_tableWidget_0.clearContents()
        self.type_tableWidget_0.setRowCount(1)

        self.iphone_info_tableWidget_0.clearContents()
        self.iphone_info_tableWidget_0.setRowCount(1000)
        self.iphone_storage_comboBox_0_2.clear()
        self.iphone_type_comboBox_0_2.clear()
        self.case_id_lineEdit_0.clear()
        self.row_count = 1

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

    def get_type_list_item(self):
        result = self.get_table_widget_item(self.type_tableWidget_0)
        iphone_type_list = []
        iphone_storage_list = []
        amount_list = []
        for value_list in result:
            iphone_type_list.append(value_list[0])
            iphone_storage_list.append(value_list[1])
            amount_list.append(int(value_list[2]))

        self.amount = sum(amount_list)
        print(self.amount)
        self.com_fun.set_iphone_type(self.iphone_type_comboBox_0_2, list(set(iphone_type_list)))
        self.com_fun.set_iphone_storage(self.iphone_storage_comboBox_0_2, list(set(iphone_storage_list)))

    def get_iphone_info_list_item(self):

        self.get_table_widget_item(self.iphone_info_tableWidget_0)

    def check_item(self):
        """
        创建方法判断输入信息是否存在
        :return:
        """
        supply_company = self.supply_company_comboBox_0.currentText()
        iphone_type = self.iphone_type_comboBox_0_1.currentText()
        problem = self.problems_comboBox_0.currentText()
        operation = self.operations_comboBox_0.currentText()
        responsible = self.responsible_lineEdit_0.currentText()
        iphone_storage = self.iphone_storage_comboBox_0_1.currentText()

        self.com_fun.check_item(supply_company, iphone_type, problem, operation, responsible, iphone_storage)

    def enterKeyPressed(self):  # 回车键按键响应槽函数

        operation = self.operations_comboBox_0.currentText()
        problem = self.problems_comboBox_0.currentText()
        iphone_type = self.iphone_type_comboBox_0_2.currentText()
        iphone_storage = self.iphone_storage_comboBox_0_2.currentText()
        apply_price = self.apply_price_lineEdit_0.text()
        remark = self.remark_lineEdit_0.text()

        info_list = [iphone_type, iphone_storage, problem, operation, apply_price, remark]

        self.check_item()

        value_dict = {
            "处理方式": operation,
            "不良项": problem,
            "手机型号": iphone_type,
            "手机内存": iphone_storage,

        }

        result = self.check_item_input(value_dict)
        if result == 1024:
            return
        else:
            try:
                currentRow = self.iphone_info_tableWidget_0.currentRow()
                # self.iphone_info_tableWidget_0.setRowCount(currentRow + 1)
                for i, item in enumerate(info_list):
                    item = QTableWidgetItem(str(item))
                    self.iphone_info_tableWidget_0.setItem(currentRow, i + 1, item)

                self.iphone_info_tableWidget_0.setCurrentCell(currentRow + 1, 0)
                bad_amount = self.get_table_widget_item(self.iphone_info_tableWidget_0)
                self.amount_lineEdit_0.setText(str(len(bad_amount)))
            except:
                pass

    def check_receipt_info(self):
        self.clear_tableWidget()
        lot_num = self.lot_num_lineEdit_0.text()
        result = self.db.get_receipt_all_info(lot_num)
        print(result)

        if result:
            supply_company = list(result[0])[0]
            self.supply_company_comboBox_0.setCurrentText(supply_company)

            credit_num = list(result[0])[1]
            self.credit_num_lineEdit_0.setText(credit_num)

            in_time = list(result[0])[2]
            self.in_time_dateEdit_0.setDate(in_time)

            row_count = len(result)
            self.type_tableWidget_0.setRowCount(row_count + 1)
            for row, iphone_info in enumerate(result):
                iphone_info_list = list(iphone_info)
                del iphone_info_list[0]
                del iphone_info_list[0]
                del iphone_info_list[0]
                for column, item in enumerate(iphone_info_list):
                    value = QTableWidgetItem(str(item))
                    self.type_tableWidget_0.setItem(row, column, value)
            # 获取case num

            result = self.db.get_case_id(lot_num)
            if result:
                case_id = list(result[0])[0]
                responsible = list(result[0])[1]
                self.case_id_lineEdit_0.setText(case_id)
                self.responsible_lineEdit_0.setCurrentText(responsible)
        else:
            pass

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

    def get_bad_count_item(self, case_id):
        search_bad_count = 0
        search_bad_count_result = self.db.check_bad_count(case_id)
        if search_bad_count_result:
            search_bad_count = len(search_bad_count_result)

        result = self.get_table_widget_item(self.iphone_info_tableWidget_0)

        bad_amount = len(result) + search_bad_count - 1
        bad_rate = (bad_amount / self.amount) * 100
        bad_rate_str = str(round(bad_rate, 2)) + "%"

        return bad_amount, bad_rate_str

    def create_case_num(self):
        self.now = int(round(time.time() * 1000))
        case_num = time.strftime('%Y%m%d%H%M%S', time.localtime(self.now / 1000))

        return case_num

    def show_case_id(self):
        case_id = self.create_case_num()
        self.case_id_lineEdit_0.setText(case_id)

    def create_case_page_info(self):
        in_time = self.in_time_dateEdit_0.text()
        lot_num = self.lot_num_lineEdit_0.text()
        supply_company = self.supply_company_comboBox_0.currentText()
        credits_num = self.credit_num_lineEdit_0.text()

        create_time = self.create_time_dateEdit_0.text()
        responsible = self.responsible_lineEdit_0.currentText()
        case_id = self.case_id_lineEdit_0.text()

        status = '打开'

        type_list = self.get_table_widget_item(self.type_tableWidget_0)
        info_list = self.get_table_widget_item(self.iphone_info_tableWidget_0)

        value_dict = {
            "lot num": lot_num,
            "供应商": supply_company,
            "发票号": credits_num,
            "责任人": responsible,
            "Case Num": case_id,
        }

        result = self.check_item_input(value_dict)
        if result == 1024:
            return
        else:
            try:
                for item in type_list:
                    iphone_type = item[0]
                    amount = item[2]
                    iphone_storage = item[1]
                    check_receipt_result = self.db.check_receipt(lot_num, iphone_type, iphone_storage)
                    print(check_receipt_result)
                    if check_receipt_result:
                        result = self.db.update_receipt_table(lot_num, in_time, supply_company, credits_num,
                                                              iphone_type, amount, iphone_storage)
                        if result:
                            QMessageBox.information(self, '提示', "更新入库单失败。", QMessageBox.Ok)
                            return
                    else:
                        result = self.db.create_receipt_table(lot_num, in_time, supply_company, credits_num,
                                                              iphone_type, amount,
                                                              iphone_storage)
                        if result:
                            QMessageBox.information(self, '提示', "创建入库单失败。", QMessageBox.Ok)
                            return
            except:
                QMessageBox.information(self, '提示', "创建或更新入库单失败。", QMessageBox.Ok)
                return
            try:
                result = self.get_bad_count_item(case_id)
                print(result)
                bad_count = list(result)[0]
                bad_rate = list(result)[1]
                check_case_result = self.db.check_case_num(case_id)
                print(check_case_result)
                if check_case_result:
                    result = self.db.update_case(case_id, create_time, lot_num, bad_count, bad_rate, status,
                                                 responsible)
                    if result:
                        QMessageBox.information(self, '提示', "更新统计单失败。", QMessageBox.Ok)
                        return
                else:
                    result = self.db.create_case(case_id, create_time, lot_num, bad_count, bad_rate, status,
                                                 responsible)
                    if result:
                        QMessageBox.information(self, '提示', "创建统计单失败。", QMessageBox.Ok)
                        return
            except:
                QMessageBox.information(self, '提示', "创建或更新统计单失败。", QMessageBox.Ok)
                return
            try:
                for item in info_list:
                    IEMI = item[0]
                    iphone_type = item[1]
                    iphone_storage = item[2]
                    problem = item[3]
                    operation = item[4]
                    apply_price = item[5]
                    remark = item[6]

                    result = self.db.add_iphone_info(IEMI, case_id, lot_num, iphone_type, problem, create_time,
                                                     operation,
                                                     iphone_storage, apply_price, remark)
                    if result:
                        QMessageBox.information(self, '提示', f"手机信息录入失败\n重复IEMI:{IEMI}。", QMessageBox.Ok)
                        delete_info_table = self.db.delete_iphone_info(case_id)
                        if delete_info_table:
                            QMessageBox.information(self, '提示', f"删除新新录入手机信息失败\nCase Num:{case_id}。", QMessageBox.Ok)
                            return
                        delete_case_result = self.db.delete_case_table(case_id)
                        if delete_case_result:
                            QMessageBox.information(self, '提示', f"删除新建统计单失败\nCase Num:{case_id}。", QMessageBox.Ok)
                            return

                        delete_receipt_result = self.db.delete_receipt_table(lot_num)
                        if delete_receipt_result:
                            QMessageBox.information(self, '提示', f"删除新建入库单失败\nCase Num:{lot_num}。", QMessageBox.Ok)
                            return
                        return

                QMessageBox.information(self, '提示', "创建成功。", QMessageBox.Ok)
                self.clear_tableWidget()
                # self.lot_num_lineEdit_0.clear()
                # self.credit_num_lineEdit_0.clear()
                self.case_id_lineEdit_0.clear()
                self.iphone_type_comboBox_0_2.clear()
                self.iphone_storage_comboBox_0_2.clear()
                self.amount_lineEdit_0.clear()
                self.amount_spinBox_0.clear()
                self.apply_price_lineEdit_0.clear()
                self.remark_lineEdit_0.clear()
                self.file_name_lineEdit_0.clear()

            except Exception as e:
                QMessageBox.information(self, '提示', "手机信息录入失败。", QMessageBox.Ok)
                # print(e)
                # self.clear_tableWidget()
                return

    def show_cases_table(self):
        results = self.db.get_cases()
        row_count = len(results)

        self.amount_lineEdit_1.setText(str(row_count))
        self.case_info_tableWidget_1.setRowCount(row_count)

        for row, item in enumerate(results):
            receipt = list(item)
            del receipt[0]
            lot_num = receipt[2]
            receipt_table_info = self.db.get_receipt_info(lot_num)
            in_time = list(receipt_table_info[0])[0]
            supply_company = list(receipt_table_info[0])[1]
            credit_num = list(receipt_table_info[0])[2]

            receipt.insert(1, str(in_time))
            receipt.insert(4, str(supply_company))
            receipt.insert(5, str(credit_num))

            for column, value in enumerate(receipt):
                value = QTableWidgetItem(str(value))
                self.case_info_tableWidget_1.setItem(row, column, value)

            self.set_option_detail(row_count, self.case_info_tableWidget_1, self.case_info_tableWidget_1.columnCount())

    def show_search_cases_table(self):
        self.case_info_tableWidget_1.clearContents()
        self.case_info_tableWidget_1.setRowCount(0)
        self.amount_lineEdit_1.clear()

        search_list = []
        search_result_list = []
        results = self.db.get_cases()

        state = self.create_time_checkBox_1.checkState()
        print(state)

        create_time = self.create_time_dateEdit_1.text().strip()
        lot_num = self.lot_num_comboBox_1.currentText().strip()
        supply_company = self.supply_company_comboBox_1.currentText().strip()
        status = self.status_comboBox_1.currentText().strip()
        IEMI = self.search_IEMI_comboBox_1.currentText().strip()
        credit_num = self.search_credit_lineEdit.text().strip()


        if state:
            search_list.append(create_time)
        if lot_num:
            search_list.append(lot_num)
        if supply_company:
            search_list.append(supply_company)
        if status:
            search_list.append(status)
        if IEMI:
            case_num = self.db.get_case_id_by_IEMI(IEMI)
            if case_num:
                case_num = list(case_num[0])[0]
                search_list.append(case_num)
        if credit_num:
            search_list.append(credit_num)

        if search_list == []:
            return
        else:
            for row, item in enumerate(results):
                receipt = list(item)
                del receipt[0]
                lot_num = receipt[2]
                receipt_table_info = self.db.get_receipt_info(lot_num)
                in_time = list(receipt_table_info[0])[0]
                supply_company = list(receipt_table_info[0])[1]
                credit_num = list(receipt_table_info[0])[2]

                receipt.insert(1, str(in_time))
                receipt.insert(4, str(supply_company))
                receipt.insert(5, str(credit_num))

                receipt[2] = str(receipt[2])

                print(receipt)
                if set(search_list).issubset(set(receipt)):
                    search_result_list.append(receipt)
                else:
                    continue

            row_count = len(search_result_list)
            print(row_count)
            print(search_list)
            if row_count == 0:
                pass
            else:
                self.amount_lineEdit_1.setText(str(row_count))
                self.case_info_tableWidget_1.setRowCount(row_count)
                for row, search_result in enumerate(search_result_list):
                    for column, value in enumerate(search_result):
                        value = QTableWidgetItem(str(value))
                        self.case_info_tableWidget_1.setItem(row, column, value)

                    self.set_option_detail(row_count, self.case_info_tableWidget_1, self.case_info_tableWidget_1.columnCount())

    def set_option_detail(self, row_count, tableWidget, column):
        if tableWidget == self.case_info_tableWidget_1:
            for i in range(row_count):
                tableWidget.setCellWidget(i, column - 1, self.detail_buttonForRow())
        if tableWidget == self.receipt_info:
            for i in range(row_count):
                tableWidget.setCellWidget(i, column - 1, self.receipt_buttonForRow())

    def detail_buttonForRow(self):
        widget = QtWidgets.QWidget()
        # 详情
        detail_style = """
            QPushButton {
                border-radius:5px;
                border-width:1px;
                background-color:#83aa7a;   
                height : 25px;
                max-width: 70px;
                min-width: 50px;
                font : 12px;
                font-family: "黑体";
            }

            QPushButton:pressed
            {
                padding-left:15px;
                border-radius:5px;
            }

        """

        detail_icon = QtGui.QIcon()
        detail_icon.addPixmap(QtGui.QPixmap("./static/img/purchase-order-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.detailBtn = QtWidgets.QPushButton('详情')
        self.detailBtn.setStyleSheet(detail_style)
        self.detailBtn.setIcon(detail_icon)

        self.detailBtn.clicked.connect(self.case_detail)

        update_style = """
            QPushButton {
                border-radius:5px;
                border-width:1px;
                background-color:#55aaff;   
                height : 25px;
                max-width: 70px;
                min-width: 50px;
                font : 12px;
                font-family: "黑体";
            }

            QPushButton:pressed
            {
                padding-left:15px;
                border-radius:5px;
            }

        """

        update_icon = QtGui.QIcon()
        update_icon.addPixmap(QtGui.QPixmap("./static/img/edit-property-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.updateBtn = QtWidgets.QPushButton('修改')
        self.updateBtn.setStyleSheet(update_style)
        self.updateBtn.setIcon(update_icon)

        self.updateBtn.clicked.connect(self.update_case)

        # 删除
        delete_style = """
            QPushButton {
                border-radius:5px;
                border-width:1px;
                background-color:#ff557f;   
                height : 25px;
                max-width: 70px;
                min-width: 50px;
                font : 12px;
                font-family: "黑体";
            }

            QPushButton:pressed
            {
                padding-left:15px;
                border-radius:5px;
            }

        """

        delete_icon = QtGui.QIcon()
        delete_icon.addPixmap(QtGui.QPixmap("./static/img/warning-38-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(delete_style)
        self.deleteBtn.setIcon(delete_icon)
        self.deleteBtn.clicked.connect(self.delete_case)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.detailBtn)
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def receipt_buttonForRow(self):
        widget = QtWidgets.QWidget()

        # 删除
        delete_style = """
            QPushButton {
                border-radius:5px;
                border-width:1px;
                background-color:#ff557f;   
                height : 25px;
                max-width: 70px;
                min-width: 50px;
                font : 12px;
                font-family: "黑体";
            }

            QPushButton:pressed
            {
                padding-left:15px;
                border-radius:5px;
            }

        """

        delete_icon = QtGui.QIcon()
        delete_icon.addPixmap(QtGui.QPixmap("./static/img/warning-38-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(delete_style)
        self.deleteBtn.setIcon(delete_icon)
        self.deleteBtn.clicked.connect(self.delete_receipt)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def find_location(self):
        self.value_list = []
        button = self.sender()
        if button:
            try:
                tableWidget = self.case_info_tableWidget_1
                row = tableWidget.indexAt(button.parent().pos()).row()
                return row, tableWidget
            except:
                pass

    def find_location_receipt_table(self):
        self.value_list = []
        button = self.sender()
        if button:
            try:
                tableWidget = self.receipt_info
                row = tableWidget.indexAt(button.parent().pos()).row()
                return row, tableWidget
            except:
                pass

    def delete_case(self):
        row, tableWidget = self.find_location()

        case_id = tableWidget.item(row, 0).text()
        lot_num = tableWidget.item(row, 3).text()

        check_box = QMessageBox.information(self, '提示', "确认删除？", QMessageBox.Ok | QMessageBox.Cancel)
        try:
            if check_box == QMessageBox.Ok:
                result = self.db.delete_case_table(case_id)
                if result == None:
                    result = self.db.delete_iphone_info(case_id)
                    if result == None:
                        QMessageBox.information(self, '提示', "删除成功。", QMessageBox.Ok)
                    else:
                        QMessageBox.information(self, '提示', "删除详情表失败。", QMessageBox.Ok)
                else:
                    QMessageBox.information(self, '提示', "删除统计单失败。", QMessageBox.Ok)

                self.show_cases_table()
            if check_box == QMessageBox.Cancel:
                self.show_cases_table()
        except:
            self.show_cases_table()

    def delete_receipt(self):
        row, tableWidget = self.find_location_receipt_table()

        # case_id = tableWidget.item(row, 0).text()
        lot_num = tableWidget.item(row, 0).text()

        check_box = QMessageBox.information(self, '提示', "确认删除？", QMessageBox.Ok | QMessageBox.Cancel)
        try:
            if check_box == QMessageBox.Ok:
                # 查询入库单是否在使用中，如果在使用中禁止删除
                count = self.db.check_receipt_use(lot_num)
                if list(count[0])[0] == 0:
                    result = self.db.delete_receipt_table(lot_num)
                    if result == None:
                        QMessageBox.information(self, '提示', "删除入库单成功。", QMessageBox.Ok)
                    else:
                        QMessageBox.information(self, '提示', "删除入库单失败。", QMessageBox.Ok)
                    self.show_receipt_table()
                else:
                    QMessageBox.information(self, '提示', "入库单使用中，禁止删除。", QMessageBox.Ok)
                    self.show_receipt_table()
            if check_box == QMessageBox.Cancel:
                self.show_receipt_table()
        except:
            self.show_receipt_table()

    def update_case(self):
        row, tableWidget = self.find_location()
        for i in range(tableWidget.columnCount() - 1):
            if tableWidget.item(row, i) == None:
                value = ""
                self.value_list.append(value)
            else:
                value = tableWidget.item(row, i).text()
                self.value_list.append(value)
        print(self.value_list)

        self.change_table = UpdateCase(self.value_list)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/available-updates-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_table.setWindowIcon(icon)

        self.change_table.show()

    def case_detail(self):
        row, tableWidget = self.find_location()
        for i in range(tableWidget.columnCount() - 1):
            if tableWidget.item(row, i) == None:
                value = ""
                self.value_list.append(value)
            else:
                value = tableWidget.item(row, i).text()
                self.value_list.append(value)
        print(self.value_list)

        self.case_detail_window = CaseInfo(self.value_list)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/view-details-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.case_detail_window.setWindowIcon(icon)

        self.case_detail_window.show()

    def show_receipt_table(self):
        result = self.db.get_receipts()
        row_count = len(result)
        self.amount_lineEdit_2.setText(str(row_count))
        self.receipt_info.setRowCount(row_count)
        if result:
            for row, value in enumerate(result):
                value_list = list(value)
                del value_list[0]
                for column, item in enumerate(value_list):
                    item = QTableWidgetItem(str(item))
                    self.receipt_info.setItem(row, column, item)

                self.set_option_detail(row_count, self.receipt_info, self.receipt_info.columnCount())

    def search_case(self):
        self.com_fun.search_function()

    def search_receipt(self):
        self.com_fun.search_function()

    def again_case(self):
        self.create_time_checkBox_1.setChecked(False)
        self.lot_num_comboBox_1.clearEditText()
        self.supply_company_comboBox_1.clearEditText()
        self.status_comboBox_1.clearEditText()
        self.search_IEMI_comboBox_1.clearEditText()
        self.search_credit_lineEdit.clear()

    def again_receipt(self):
        self.in_time_checkBox_2.setChecked(False)
        self.lot_num_comboBox_2.clearEditText()
        self.supply_company_comboBox_2.clearEditText()

    def open_file(self):

        path_openfile_name, IEMI_list = self.com_fun.open_file()
        print(path_openfile_name)
        print(IEMI_list)
        if path_openfile_name:
            file_name = path_openfile_name.split("/")[-1]
            print(file_name)
            self.file_name_lineEdit_0.setText(file_name)
            if IEMI_list:
                IEMI_list = list(set(IEMI_list))
                self.amount_lineEdit_0.setText(str(len(IEMI_list)))

                self.import_set_data(IEMI_list)

    def import_set_data(self, IEMI_list):  # 回车键按键响应槽函数

        operation = self.operations_comboBox_0.currentText()
        problem = self.problems_comboBox_0.currentText()
        iphone_type = self.iphone_type_comboBox_0_2.currentText()
        iphone_storage = self.iphone_storage_comboBox_0_2.currentText()
        apply_price = self.apply_price_lineEdit_0.text()
        remark = self.remark_lineEdit_0.text()

        info_list = [iphone_type, iphone_storage, problem, operation, apply_price, remark]

        self.check_item()

        value_dict = {
            "处理方式": operation,
            "不良项": problem,
            "手机型号": iphone_type,
            "手机内存": iphone_storage,

        }

        result = self.check_item_input(value_dict)
        if result == 1024:
            return
        else:
            try:
                start_row = self.get_start_row()
                print(start_row)
                for row, IEMI in enumerate(IEMI_list):
                    info_list.insert(0, IEMI)
                    for column, item in enumerate(info_list):
                        item = QTableWidgetItem(str(item))
                        self.iphone_info_tableWidget_0.setItem(row + start_row, column, item)
                    info_list.remove(IEMI)

                bad_amount = self.get_table_widget_item(self.iphone_info_tableWidget_0)
                self.amount_lineEdit_0.setText(str(len(bad_amount)))
            except Exception as e:
                print(e)
                pass

    def set_data_by_input(self):
        IEMI_list = self.com_fun.get_IEMI_list(self.plainTextEdit)
        self.import_set_data(IEMI_list)

    def get_start_row(self):
        row_count = self.iphone_info_tableWidget_0.rowCount()
        for row in range(row_count):
            item = self.iphone_info_tableWidget_0.item(row, 0)
            print(item)
            if item is not None:
                continue
            else:
                return row


if __name__ == "__main__":
    import sys
    import os

    if hasattr(sys, '_MEIPASS'):
        # PyInstaller会创建临时文件夹temp
        # 并把路径存储在_MEIPASS中
        appPath = os.path.dirname(os.path.realpath(sys.executable))
    else:
        appPath, filename = os.path.split(os.path.abspath(__file__))

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.center()
    window_icon = QtGui.QIcon()
    window_icon.addPixmap(QtGui.QPixmap("./static/img/cow-2-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    MainWindow.setWindowIcon(window_icon)
    MainWindow.show()

    sys.exit(app.exec_())
