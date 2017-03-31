#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QGridLayout, QPushButton, QMessageBox,
                             QHBoxLayout, QVBoxLayout, QLineEdit,
                             QTextEdit, QLabel, QComboBox, QCalendarWidget)
from PyQt5.QtCore import QCoreApplication


class ResultPrint(QWidget):

    def __init__(self, rstr, rcount=0):
        super().__init__()

        self.rstr = rstr
        self.rcount = rcount

        self.initUI()

    def initUI(self):

        grid = QGridLayout()

        if isinstance(self.rstr, list):

            self.textbox = QTextEdit()
            self.textbox.setReadOnly(True)

            # for each_result in self.rstr:
            self.textbox.setText(str(self.rstr))

            grid.addWidget(self.textbox, 0, 0, 300, 300)
            self.setLayout(grid)
            self.setGeometry(300, 300, 300, 300)



            """
            grid.setSpacing(1)

            for each_result, iii in zip(self.rstr, range(self.rcount)):
                self.result = QLabel(each_result)
                grid.addWidget(self.result, iii+1, 0)

            self.setLayout(grid)
            self.setGeometry(300, 300, 300, 300)
            """


        else:
            grid.setSpacing(5)

            self.result = QLabel('每月还款金额为 %.2f 元' % self.rstr)
            grid.addWidget(self.result, 1, 0)
            self.setLayout(grid)


            self.setGeometry(300, 300, 100, 100)

        self.setWindowTitle('计算结果')





class MortgageCal(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        self.CommercialLoanDes = QLabel('商业贷款额')
        self.CommercialLoan = QLineEdit()
        grid.addWidget(self.CommercialLoanDes, 1, 0)
        grid.addWidget(self.CommercialLoan, 1, 1)

        self.CommercialLoanRateDes = QLabel('商贷利率')
        self.CommercialLoanRate = QLineEdit()
        self.CommercialLoanRate.setText('4.90')
        self.CommercialLoanRateUnit = QLabel('%')
        grid.addWidget(self.CommercialLoanRateDes, 1, 2)
        grid.addWidget(self.CommercialLoanRate, 1, 3)
        grid.addWidget(self.CommercialLoanRateUnit, 1, 4)


        self.ProvidentFundDes = QLabel('公积金贷款额')
        self.ProvidentFund = QLineEdit()
        grid.addWidget(self.ProvidentFundDes, 2, 0)
        grid.addWidget(self.ProvidentFund, 2, 1)

        self.ProvidentFundRateDes = QLabel('公积金利率')
        self.ProvidentFundRate = QLineEdit()
        self.ProvidentFundRate.setText('3.25')
        self.ProvidentFundRateUnit = QLabel('%')
        grid.addWidget(self.ProvidentFundRateDes, 2, 2)
        grid.addWidget(self.ProvidentFundRate, 2, 3)
        grid.addWidget(self.ProvidentFundRateUnit, 2, 4)

        self.YearDes = QLabel('贷款年限')
        self.Year = QComboBox()
        for each_year in ['5年','10年','15年','20年','25年', '30年']:
            self.Year.addItem(each_year)
        grid.addWidget(self.YearDes, 3, 0)
        grid.addWidget(self.Year, 3, 1)

        self.LoanTypeDes = QLabel('贷款类型')
        self.LoanType = QComboBox()
        for each_type in ['等额本息', '等额本金']:
            self.LoanType.addItem(each_type)
        grid.addWidget(self.LoanTypeDes, 4, 0)
        grid.addWidget(self.LoanType, 4, 1)

        self.EnterButton = QPushButton()
        self.EnterButton.setText('确认')
        grid.addWidget(self.EnterButton, 5, 0)

        self.setLayout(grid)

        self.EnterButton.clicked.connect(self.loanCal)

        # self.resultprint = ResultPrint()


        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('房贷计算器')
        self.show()

    def loanCal(self):

        sydk = float(self.CommercialLoan.text())
        yll = float(self.CommercialLoanRate.text())/1200
        years = int(self.Year.currentText().replace('年', ''))

        gjjdk = float(self.ProvidentFund.text())
        gjjll = float(self.ProvidentFundRate.text())/1200


        if self.LoanType.currentIndex() == 0:

            syhk = sydk*yll*pow((1+yll), 12*years)/(pow((1+yll), 12*years)-1)
            gjjhk = gjjdk*gjjll*pow((1+gjjll), 12*years)/(pow((1+gjjll), 12*years)-1)

            yhk = syhk + gjjhk
            self.resultprint = ResultPrint(yhk)
            self.resultprint.show()
            # print("每月还款金额为 %.2f" % yhk)


        else:

            result = []
            for i in range(12*years):
                yhk = round(sydk/(12*years)+(sydk-(sydk/(12*years))*i)*yll+
                gjjdk/(12*years)+(gjjdk-(gjjdk/(12*years))*i)*gjjll, 2)
                result.append("第 %d 个月需还款 %.2f 元 \n" % (i, yhk))

            self.resultprint = ResultPrint(result, 12*years)
            self.resultprint.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MortgageCal()
    sys.exit(app.exec_())





