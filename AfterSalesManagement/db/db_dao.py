from db.common_dao import CommonDao

class DBDao:
    def __init__(self):
        self.com_db = CommonDao()

    def get_iphone_type(self):
        try:
            sql = "SELECT iphone_type FROM db_purchase.iphone_type;"
            iphone_type = CommonDao.search_option(self, sql)
            if isinstance(iphone_type, list):
                return iphone_type
            else:
                iphone_type = self.com_db.get_local_data("iphonetype")
                return iphone_type
        except:
            iphone_type = self.com_db.get_local_data("iphonetype")
            return iphone_type

    def get_iphone_storage(self):
        try:
            sql = "SELECT iphone_storage FROM db_purchase.iphone_storage;"
            iphone_storage = CommonDao.search_option(self, sql)
            if isinstance(iphone_storage, list):
                return iphone_storage
            else:
                iphone_storage = self.com_db.get_local_data("iphonestorage")
                return iphone_storage
        except:
            iphone_storage = self.com_db.get_local_data("iphonestorage")
            return iphone_storage

    # def get_iphone_storage(self):
    #     try:
    #         sql = "SELECT iphone_storage FROM db_purchase.iphone_storage;"
    #         iphone_storage = CommonDao.search_option(self, sql)
    #         if isinstance(iphone_storage, list):
    #             return iphone_storage
    #         else:
    #             iphone_storage = self.com_db.get_local_data("iphonestorage")
    #             return iphone_storage
    #     except:
    #         iphone_storage = self.com_db.get_local_data("iphonestorage")
    #         return iphone_storage

    # def get_iphone_grade(self):
    #     try:
    #         sql = "SELECT iphone_grade FROM db_purchase.iphone_grade;"
    #         iphone_grade = CommonDao.search_option(self, sql)
    #         if isinstance(iphone_grade, list):
    #             return iphone_grade
    #         else:
    #             iphone_grade = self.com_db.get_local_data("iphonegrade")
    #             return iphone_grade
    #     except:
    #         iphone_grade = self.com_db.get_local_data("iphonegrade")
    #         return iphone_grade

    def get_case_status(self):
        try:
            sql = "SELECT status FROM db_purchase.case_status;"
            case_status = CommonDao.search_option(self, sql)
            if isinstance(case_status, list):
                return case_status
            else:
                case_status = self.com_db.get_local_data("casestatus")
                return case_status
        except:
            case_status = self.com_db.get_local_data("casestatus")
            return case_status

    def get_supply_company(self):
        try:
            sql = "SELECT supply_company FROM db_purchase.supply_company;"
            supply_company = CommonDao.search_option(self, sql)
            if isinstance(supply_company, list):
                return supply_company
            else:
                supply_company = self.com_db.get_local_data("incompany")
                return supply_company
        except:
            supply_company = self.com_db.get_local_data("incompany")
            return supply_company

    def get_problems(self):
        try:
            sql = "SELECT problem FROM db_purchase.problem;"
            problems = CommonDao.search_option(self, sql)
            if isinstance(problems, list):
                return problems
            else:
                problems = self.com_db.get_local_data("problems")
                return problems
        except:
            problems = self.com_db.get_local_data("problems")
            return problems

    def get_lot_nums(self):
        try:
            sql = "SELECT distinct lot_num FROM db_purchase.receipts_table;"
            lot_nums = CommonDao.search_option(self, sql)
            if isinstance(lot_nums, list):
                return lot_nums
            else:
                pass
        except:
            pass

    # 创建case
    def create_case(self, case_id, create_time, lot_num, bad_count, bad_rate, status, responsible):
        try:
            sql = f"INSERT INTO db_purchase.cases_table (case_id, create_time, lot_num, bad_count, bad_rate, status, responsible)  VALUES ('{case_id}', '{create_time}', '{lot_num}', '{bad_count}', '{bad_rate}', '{status}', '{responsible}');"
            print(sql)
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    # 检查case_num是否存在
    def check_case_num(self, case_num):
        try:
            sql = f"SELECT * FROM db_purchase.cases_table WHERE case_id='{case_num}';"
            amount = CommonDao.search_option(self, sql)
            if isinstance(amount, list):
                return amount
            else:
                pass
        except:
            pass

    def check_bad_count(self, case_num):
        try:
            sql = f"SELECT COUNT(*) FROM db_purchase.cases_table WHERE case_id='{case_num}';"
            amount = CommonDao.search_option(self, sql)
            if isinstance(amount, list):
                return amount
            else:
                pass
        except:
            pass

    def create_receipt(self, case_num, lot_num, responsible):
        try:
            sql = f"INSERT INTO db_purchase.cases_table (case_id, create_time, lot_num, responsible)  VALUES ('{case_num}',CURRENT_TIMESTAMP,'{lot_num}','{responsible}');"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    def check_item(self, value):
        try:
            for table, value in value.items():
                sql = f"SELECT COUNT(*) FROM db_purchase.{table} WHERE {table}='{value}';"
                amount = CommonDao.search_option(self, sql)
                if isinstance(amount, list):
                    if list(amount[0])[0] == 0:
                        sql = f"INSERT INTO db_purchase.{table} ({table})  VALUES ('{value}');"
                        results = CommonDao.change_option(self, sql)
                    else:
                        pass
                else:
                    pass
        except:
            pass

    def create_receipt_table(self, lot_num, in_time, supply_company, credit_num, iphone_type, amount,iphone_storage):
        try:
            sql = f"INSERT INTO db_purchase.receipts_table (lot_num, in_time, supply_company, credit_num, iphone_type, amount,iphone_storage) VALUES ('{lot_num}', '{in_time}', '{supply_company}', '{credit_num}', '{iphone_type}', '{amount}', '{iphone_storage}');"
            results = CommonDao.change_option(self, sql)
            return results
        except:
            pass

    def check_receipt(self, lot_num, iphone_type,iphone_storage):
        try:
            sql = f"SELECT * FROM db_purchase.receipts_table WHERE lot_num='{lot_num}' AND iphone_type='{iphone_type}' AND iphone_storage='{iphone_storage}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def get_receipts(self):
        try:
            sql = "SELECT * FROM db_purchase.receipts_table;"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def get_receipt(self,):
        try:
            sql = "SELECT * FROM db_purchase.receipts_table ;"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def update_receipt(self, case_num, lot_num, responsible):
        try:
            sql = f"INSERT INTO db_purchase.cases_table (case_id, create_time, lot_num, responsible)  VALUES ('{case_num}',CURRENT_TIMESTAMP,'{lot_num}','{responsible}');"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    def update_case(self, case_id, create_time, lot_num, bad_count, bad_rate, status, responsible):
        try:
            sql = f"UPDATE db_purchase.cases_table SET create_time='{create_time}',lot_num='{lot_num}',bad_count='{bad_count}',bad_rate='{bad_rate},status='{status}',responsible='{responsible}'  WHERE case_id='{case_id}';"
            print(sql)
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    def update_receipt_table(self, lot_num, in_time, supply_company, credits_num, iphone_type, amount,
                                                 iphone_storage):
        try:
            sql = f"UPDATE db_purchase.receipts_table SET in_time='{in_time}',supply_company='{supply_company}',credit_num='{credits_num}',amount='{amount}  WHERE lot_num='{lot_num}' AND iphone_type='{iphone_type}' AND iphone_storage='{iphone_storage}';"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    def delete_receipt_table(self, lot_num):
        try:
            sql = f"DELETE FROM db_purchase.receipts_table WHERE lot_num='{lot_num}';"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    def delete_case_table(self, case_id):
        try:
            sql = f"DELETE FROM db_purchase.cases_table WHERE case_id='{case_id}';"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    def delete_iphone_info(self, case_id):
        try:
            sql = f"DELETE FROM db_purchase.case_info WHERE case_id='{case_id}';"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass


    def get_cases(self):
        try:
            sql = "SELECT * FROM db_purchase.cases_table;"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def get_iphone_info_table(self,case_id):
        try:
            sql = f"SELECT IEMI,iphone_type,iphone_storage,problem,operation,feedback,change_time,apply_price, approve_price,remark FROM db_purchase.case_info WHERE case_id='{case_id}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def get_receipt_info(self, lot_num):
        try:
            sql = f"SELECT in_time,supply_company,credit_num FROM db_purchase.receipts_table WHERE lot_num='{lot_num}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def get_receipt_all_info(self, lot_num):
        try:
            sql = f"SELECT supply_company,credit_num,in_time,iphone_type,iphone_storage,amount FROM db_purchase.receipts_table WHERE lot_num='{lot_num}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def get_case_id(self, lot_num):
        try:
            sql = f"SELECT case_id,responsible FROM db_purchase.cases_table WHERE lot_num='{lot_num}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def get_case_id_by_IEMI(self, IEMI):
        try:
            sql = f"SELECT case_id FROM db_purchase.case_info WHERE IEMI='{IEMI}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass


    def add_iphone_info(self, IEMI,case_id,lot_num,iphone_type,problem,create_time,operation, iphone_storage,apply_price,remark):
        try:
            sql = f"INSERT INTO db_purchase.case_info (IEMI,case_id,lot_num,iphone_type,problem,change_time,operation,iphone_storage,apply_price,remark) VALUES ('{IEMI}','{case_id}','{lot_num}','{iphone_type}','{problem}','{create_time}','{operation}','{iphone_storage}','{apply_price}','{remark}');"
            results = CommonDao.change_option(self, sql)
            return results
        except Exception as e:
            return e

    def get_actual_count(self, lot_num):
        try:
            sql = f"SELECT actual_amount FROM db_purchase.receipts_table WHERE lot_num='{lot_num}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def update_cases_table(self,bad_count,bad_rate,status, case_id):
        print("genxing")
        try:
            sql = f"UPDATE db_purchase.cases_table SET bad_count='{bad_count}',bad_rate='{bad_rate}',status='{status}' WHERE case_id='{case_id}';"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass


    def get_iphone_list(self, case_id, lot_num, status):
        try:
            sql = f"SELECT IEMI,iphone_type,problem,feedback,change_time FROM db_purchase.open_case_info WHERE case_id='{case_id}' AND lot_num='{lot_num}';"

            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except Exception as e:
            print(e)
            pass

    def get_iphone_single_storage(self, lot_num, iphone_type):
        try:
            sql = f"SELECT iphone_storage FROM db_purchase.receipts_table WHERE lot_num='{lot_num}' AND iphone_type='{iphone_type}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except Exception as e:
            print(e)
            pass

    def get_lot_num_iphone_type(self, lot_num):
        """
        获取同一lot num下对应的机型
        :param lot_num:
        :return:
        """
        try:
            sql = f"SELECT iphone_type FROM db_purchase.receipts_table WHERE lot_num='{lot_num}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except Exception as e:
            print(e)
            pass

    def get_lot_num_iphone_storage(self, lot_num, iphone_type):
        """
        获取同一lot num下对应的内存
        :param lot_num:
        :return:
        """
        try:
            sql = f"SELECT iphone_storage FROM db_purchase.receipts_table WHERE lot_num='{lot_num}' AND iphone_type='{iphone_type}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except Exception as e:
            print(e)
            pass

    def get_added_iphone(self, case_id):
        try:
            sql = f"SELECT count(*) FROM db_purchase.open_case_info WHERE case_id='{case_id}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except Exception as e:
            print(e)
            pass

    def get_lot_type(self, IEMI):
        try:
            sql = f"SELECT iphone_type,problem FROM db_purchase.case_info WHERE IEMI='{IEMI}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except Exception as e:
            print(e)
            pass

    def update_case_table(self,RMA_num,tracking_num,status, case_id):
        try:
            sql = f"UPDATE db_purchase.cases_table SET RMA_num='{RMA_num}',tracking_num='{tracking_num}',status='{status}' WHERE case_id='{case_id}';"
            results = CommonDao.change_option(self, sql)
            print(results)
            return results
        except:
            pass

    def update_iphone_info(self,operation,change_time,feedback,approve_price,remark,IEMI):
        try:
            sql = f"UPDATE db_purchase.case_info SET operation='{operation}',change_time='{change_time}',feedback='{feedback}',approve_price='{approve_price}',remark='{remark}' WHERE IEMI='{IEMI}';"
            results = CommonDao.change_option(self, sql)
            return results
        except Exception as e:
            print(e)
            return e

    def get_operation(self):
        try:
            sql = "SELECT case_operations FROM db_purchase.case_operations;"
            lot_nums = CommonDao.search_option(self, sql)
            if isinstance(lot_nums, list):
                return lot_nums
            else:
                pass
        except:
            pass

    def get_responsible(self):
        try:
            sql = "SELECT responsible FROM db_purchase.responsible;"
            responsible = CommonDao.search_option(self, sql)
            if isinstance(responsible, list):
                return responsible
            else:
                pass
        except:
            pass

    def get_receipt_amount(self, lot_num):
        try:
            sql = f"SELECT amount,credit_num FROM db_purchase.receipts_table WHERE lot_num='{lot_num}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    def check_receipt_use(self, lot_num):
        try:
            sql = f"SELECT COUNT(*) FROM db_purchase.cases_table WHERE lot_num='{lot_num}';"
            results = CommonDao.search_option(self, sql)
            if isinstance(results, list):
                return results
            else:
                pass
        except:
            pass

    # def get_credit_num(self, lot_num):
    #     try:
    #         sql = f"SELECT credit_num FROM db_purchase.receipts_table WHERE lot_num='{lot_num}';"
    #         results = CommonDao.search_option(self, sql)
    #         if isinstance(results, list):
    #             return results
    #         else:
    #             pass
    #     except:
    #         pass

