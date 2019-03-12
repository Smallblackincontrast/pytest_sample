#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : web_flow_test_case.py
# @Author  : Ruanzhe
# @Date  : 2019/2/12  11:15

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class WebFlowTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = None

    def open(self, url: str, implicitly_wait: int = 30, timeout: int = 30, loc_blank: str = None,
             is_active_window: bool = False, is_auto_close: bool = True):
        """
        打开指定页面
        :param url: 要打开的URL
        :param implicitly_wait: 等待元素的时间
        :param timeout: 等待页面加载和JS执行的时间
        :param loc_blank: 空白处选择器定义
        :param is_active_window: 是否激活窗口
        :param is_auto_close: 是否自动关闭浏览器
        :return:
        """
        if self.driver is None:
            self.driver = webdriver.Chrome()

        self.is_active_window = is_active_window
        self.driver.implicitly_wait(implicitly_wait)
        self.driver.set_page_load_timeout(timeout)
        self.driver.set_script_timeout(timeout)
        self.loc_blank = loc_blank
        self.is_auto_close = is_auto_close

        if self.is_active_window:
            self.driver.switch_to.window(self.driver.current_window_handle)

        self.driver.get(url)

    def _close(self):
        """
        关闭浏览器和页面
        """
        self.driver.close()

    def get_element(self, css_loc: str):
        """
        使用css selecotr 查找元素
        :param css_loc: css selector 表达式
        """
        return self.driver.find_element(By.CSS_SELECTOR, css_loc)

    def action_chain(self):
        """
        返回动作队列
        """
        return ActionChains(self.driver)

    @staticmethod
    def keep(second: float = 0.5):
        """
        短暂的暂停,多用于等待动画执行完毕,比如弹出菜单等
        """
        sleep(second)

    def script(self, src: str):
        """
        执行JavaScript脚本
        :param src: 脚本
        """
        return self.driver.execute_script(src)

    def send_keys(self, css_loc: str, value, clear_first: bool = True, click_first: bool = False):
        """
        向制定元素发送内容
        :param css_loc: css selector 选择表达式
        :param value: 要发送的内容
        :param clear_first: 发送内容前是否先清空元素中的内容
        :param click_first: 发送内容前,是否先点击一下元素
        """
        try:
            element = self.get_element(css_loc)
            if click_first:
                element.click()
            if clear_first:
                element.clear()
            element.send_keys(value)

        except AttributeError:
            print('%s 页面找不到 "%s" css 选择表达式' % (self, css_loc))

    def maximize_window(self):
        """
        最大化窗口
        :return:
        """
        self.driver.maximize_window()

    def click(self, css_loc: str):
        """
        点击指定的元素
        :param css_loc: css selector 选择表达式
        """
        self.get_element(css_loc).click()

    def double_click(self, css_loc: str):
        """
        双击指定的元素
        :param css_loc: css selector 选择表达式
        """
        self.action_chain().double_click(self.get_element(css_loc)).perform()

    def clear(self, css_loc: str):
        """
        清空指定元素的内容
        :param css_loc: css selector 选择表达式
        """
        self.get_element(css_loc).clear()

    def right_click(self, css_loc: str):
        """
        右键单击元素
        """
        self.action_chain().context_click(self.get_element(css_loc)).perform()

    def move_to_element(self, css_loc: str):
        """
        移动到指定元素
        :param css_loc:  css selector 选择表达式
        """
        self.action_chain().move_to_element(self.get_element(css_loc)).perform()

    def drag_and_drop(self, source_css_loc: str, target_css_loc: str):
        """
        拖动一个元素到另一元素上
        :param source_css_loc:  拖动哪个元素,css selector 选择表达式
        :param target_css_loc:  拖动到哪个元素,css selector 选择表达式
        """
        self.action_chain().drag_and_drop(self.get_element(source_css_loc), self.get_element(target_css_loc))

    def click_link_by_text(self, text: str):
        """
        点击具有指定文字的超链接
        :param text: 文字
        """
        list_element = self.driver.find_elements_by_partial_link_text(text)

        # 如果过个超链接使用同样的名字,可能造成潜在的错误,直接抛出异常
        if len(list_element) > 1:
            raise AttributeError("找到了多个使用该文字的超链接")

        list_element[0].click()

    def refresh(self):
        """
        刷新当前页面
        """
        self.driver.refresh()

    def get_attribute(self, css_loc: str, attr_name: str):
        """
        获取指定元素的指定属性值
        :param css_loc: css selector 选择表达式
        :param attr_name: 属性名
        :return: 属性值
        """
        return self.get_element(css_loc).get_attribute(attr_name)

    def get_text(self, css_loc: str):
        """
        获得指定元素的text
        :param css_loc: css selector 选择表达式
        :return: 元素的text
        """
        return self.get_element(css_loc).text

    def get_title(self):
        """
        获取当前页面的标题
        :return: 页面标题
        """
        return self.driver.title

    def get_current_url(self):
        """
        获取当前页面的url
        :return:当前页面的url
        """
        return self.driver.current_url

    def accept_alert(self):
        """
        接收当前页面的(系统)弹出框
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        取消当前页面的(系统)弹出框
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css_loc: str):
        """
        切换到指定的iframe
        :param css_loc: css selector 选择表达式
        """
        self.driver.switch_to.frame(self.get_element(css_loc))

    def switch_to_frame_out(self):
        """
        从iframe中切换出来
        """
        self.driver.switch_to.default_content()

    def get_screenshot(self, file_path: str):
        """
        获得屏幕截图,并保存到指定文件夹
        :param file_path:
        """
        self.driver.get_screenshot_as_file(file_path)

    def click_blank_area(self):
        """
        点击页面空白区域
        建议在初始化类(__init__)时使用 loc_blank 为类显式定义空白区域
        否则将点击页面的左上角(0,0)处
        """
        if self.loc_blank is not None:
            self.click(self.loc_blank)
        else:
            self.action_chain().move_by_offset(1, 1).click().perform()

    def get_display(self, css_loc: str):
        """
        获取指定元素是否显示
        :param css_loc: css selector 选择表达式
        :return: 显示 True, 不显示 False
        """
        return self.get_element(css_loc).is_displayed()

    def select(self, css_loc: str, value):
        """
        选中一个Select控件中的指定值
        :param css_loc: css selector 选择表达式
        :param value: 要选择的值
        """
        el = self.get_element(css_loc)
        Select(el).select_by_value(value)

    def tearDown(self):
        if self.driver is not None and self.is_auto_close is True:
            self._close()
