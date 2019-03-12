#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_login.py
# @Author  : Ruanzhe
# @Date  : 2019/2/12  11:16

from Tools.web_flow_test_case import WebFlowTestCase


class LineBusAdminLogin(WebFlowTestCase):

	def setUp(self):
		self.url = "http://line-qa.ubtbus.top:8079/#/login"
		self.username = "input[sid='usernameInput']"
		self.password = "input[sid='passwordInput']"
		self.loginbutton = "button[sid='loginBtn']"

	def _click_login(self):
		self.click(self.loginbutton)

	def _send_username(self, username):
		self.send_keys(self.username, username)

	def _send_password(self, password):
		self.send_keys(self.password, password)

	def admin_login_flow(self, username, password):
		self.open(self.url, is_active_window=True)
		self._send_username(username)
		self._send_password(password)
		self._click_login()

	def test_login_success(self):
		self.admin_login_flow('LS_admin', '666666')
		self.keep()
		self.assertEqual()
