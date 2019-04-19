# -*- coding: cp936 -*-

import sys
import os
from urllib.request import urlretrieve
from ctypes import *

class Code():

    def __init__(self):
        self.YDMApi = windll.LoadLibrary('yundamaAPI-x64')
        self.appId = 7452  # ����ɣģ������߷ֳɱ�Ҫ��������¼�����ߺ�̨���ҵ��������ã�
        self.appKey = b'6a1b9884fbf80b37bab5173f70733402'  # �����Կ�������߷ֳɱ�Ҫ��������¼�����ߺ�̨���ҵ��������ã�
        # print('����ɣģ�%d\r\n�����Կ��%s' % (self.appId, self.appKey))
        self.username = b'645064301'
        self.password = b'qwert12358'
        # self.code_name = code_name
        if self.username == b'test':
            exit('\r\n>>>���������û�������')


    ####################### һ��ʶ���� YDM_EasyDecodeByPath #######################
    def identify_key(self):
        # print('\r\n>>>����һ��ʶ��...')
        # ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ��ڴ˲�ѯ�������� http://www.yundama.com/price.html
        codetype = 1004

        # ����30���ֽڴ��ʶ����
        result = c_char_p(b"                              ")

        # ʶ��ʱʱ�� ��λ����
        timeout = 60

        # ��֤���ļ�·��
        filename = b'code.png'

        # һ��ʶ������������� YDM_SetAppInfo �� YDM_Login���ʺϽű�����
        captchaId = self.YDMApi.YDM_EasyDecodeByPath(self.username, self.password, self.appId, self.appKey, filename, codetype, timeout, result)

        # print("һ��ʶ����֤��ID��%d��ʶ������%s" % (captchaId, result.value))
        # print(result.value.decode("utf-8"))
        return result.value.decode("utf-8")

    def identify_ordinary(self):

        ################################################################################
        ########################## ��ͨʶ���� YDM_DecodeByPath #########################


        # print('\r\n>>>���ڵ�½...')

        # ��һ������ʼ���ƴ��룬ֻ�����һ�μ���
        self.YDMApi.YDM_SetAppInfo(self.appId, self.appKey)

        # �ڶ�������½�ƴ����˺ţ�ֻ�����һ�μ���
        uid = self.YDMApi.YDM_Login(self.username, self.password)

        if uid > 0:

            # print('>>>���ڻ�ȡ���...')

            # ��ѯ�˺�������Ҫ����
            balance = self.YDMApi.YDM_GetBalance(self.username, self.password)

            # print('��½�ɹ����û�����%s��ʣ����֣�%d' % (self.username, balance))

            # print('\r\n>>>������ͨʶ��...')

            # ����������ʼʶ��

            # ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ��ڴ˲�ѯ�������� http://www.yundama.com/price.html
            codetype = 1004

            # ����30���ֽڴ��ʶ����
            result = c_char_p(b"                              ")

            # ��֤���ļ�·��
            filename = b'code.png'

            # ��ͨʶ���������ȵ��� YDM_SetAppInfo �� YDM_Login ��ʼ��
            captchaId = self.YDMApi.YDM_DecodeByPath(filename, codetype, result)

            # print("��ͨʶ����֤��ID��%d��ʶ������%s" % (captchaId, result.value))
            return result.value.decode("utf-8")
        else:
            # print('��½ʧ�ܣ�������룺%d' % uid)
            return "ʶ��ʧ�ܣ�"

        ################################################################################

        # print('\r\n>>>����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html')
        #
        # input('\r\n������ɣ����س�������...')


if __name__ == '__main__':
    c = Code()
    print(c.identify_key())