from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from datetime import datetime

from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker, MDTimePicker

from kivy.uix.screenmanager import ScreenManager
from helper import screen_helper

import sqlite3
from kivymd.app import MDApp

from screen_classes.login_screen import LoginScreen
from screen_classes.login_screen import IntroScreen
from screen_classes.login_screen import RegisterScreen
from screen_classes.welcome_screen import WelcomeScreen
from screen_classes.baby_updates import ChooseBabyScreen, AddNewBabyScreen, UpdateBabyScreen
from screen_classes.login_screen import HomeScreen
from screen_classes.account_screen import AccountScreen

sm = ScreenManager()
sm.add_widget(IntroScreen(name='Intro'))
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(RegisterScreen(name='Register'))
sm.add_widget(WelcomeScreen(name='Welcome'))
sm.add_widget(AddNewBabyScreen(name='AddNewBaby'))
sm.add_widget(ChooseBabyScreen(name='ChooseBaby'))
sm.add_widget(UpdateBabyScreen(name='UpdateBaby'))
sm.add_widget(HomeScreen(name='Home'))
sm.add_widget(AccountScreen(name='Account'))


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def back_to_login(self):
        self.root.current = 'Login'
        self.root.get_screen('Login').ids.login_username.text = ""
        self.root.get_screen('Login').ids.login_password.text = ""

    def close_dialog_to_login(self, obj):
        self.dialog.dismiss()
        self.root.current = 'Login'

    def close_dialog_to_welcome(self, obj):
        self.dialog.dismiss()
        self.root.current = 'Welcome'

    def show_date_picker(self, var):
        date_dialog = MDDatePicker()
        if var == 1:
            date_dialog.bind(on_save=self.on_date_save_welcome, on_cancel=self.on_date_cancel)
        elif var == 2:
            date_dialog.bind(on_save=self.on_date_save_sleep, on_cancel=self.on_date_cancel)
        elif var == 3:
            date_dialog.bind(on_save=self.on_date_save_feed, on_cancel=self.on_date_cancel)
        elif var == 4:
            date_dialog.bind(on_save=self.on_date_save_update_baby, on_cancel=self.on_date_cancel)
        elif var == 5:
            date_dialog.bind(on_save=self.on_date_add_baby, on_cancel=self.on_date_cancel)
        elif var == 6:
            date_dialog.bind(on_save=self.on_date_add_measurement, on_cancel=self.on_date_cancel)
        date_dialog.open()

    def on_date_save_welcome(self, instance, value, date_range):
        formatted_date = value.strftime('%Y-%m-%d')
        self.root.get_screen('Welcome').ids.date_of_birth.text = formatted_date

    def on_date_add_measurement(self, instance, value, date_range):
        formatted_date = value.strftime('%Y-%m-%d')
        self.root.get_screen('LogMeasurement').ids.measurement_date.text = formatted_date

    def on_date_add_baby(self, instance, value, date_range):
        formatted_date = value.strftime('%Y-%m-%d')
        self.root.get_screen('AddNewBaby').ids.date_of_birth.text = formatted_date

    def on_date_save_sleep(self, instance, value, date_range):
        formatted_date = value.strftime('%Y-%m-%d')
        self.root.get_screen('SleepEntry').ids.sleep_date.text = formatted_date

    def on_date_save_feed(self, instance, value, date_range):
        formatted_date = value.strftime('%Y-%m-%d')
        self.root.get_screen('FeedingEntry').ids.feed_date.text = formatted_date

    def on_date_save_update_baby(self, instance, value, date_range):
        formatted_date = value.strftime('%Y-%m-%d')
        self.root.get_screen('UpdateBaby').ids.date_of_birth.text = formatted_date

    def on_date_cancel(self, instance, value):
        pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.set_time(datetime.now())
        time_dialog.bind(time=self.on_time_save)
        time_dialog.open()

    def on_time_save(self, instance, time):
        formatted_time = time.strftime('%H:%M')
        self.root.get_screen('Welcome').ids.hour_of_birth.text = formatted_time

    def show_time_picker_for_sleep_entry(self, start):
        time_dialog = MDTimePicker()
        time_dialog.set_time(datetime.now())
        if start:
            time_dialog.bind(time=self.on_time_save_start_hour)
        else:
            time_dialog.bind(time=self.on_time_save_end_hour)
        time_dialog.open()

    def show_time_picker_for_update_baby(self):
        time_dialog = MDTimePicker()
        time_dialog.set_time(datetime.now())
        time_dialog.bind(time=self.on_time_save_update_baby)
        time_dialog.open()

    def show_time_picker_add_baby(self):
        time_dialog = MDTimePicker()
        time_dialog.set_time(datetime.now())
        time_dialog.bind(time=self.on_time_add_baby)
        time_dialog.open()

    def on_time_save_update_baby(self, instance, time):
        formatted_time = time.strftime('%H:%M')
        self.root.get_screen('UpdateBaby').ids.hour_of_birth.text = formatted_time

    def on_time_add_baby(self, instance, time):
        formatted_time = time.strftime('%H:%M')
        self.root.get_screen('AddNewBaby').ids.hour_of_birth.text = formatted_time

    def on_time_save_start_hour(self, instance, time):
        formatted_time = time.strftime('%H:%M')
        self.root.get_screen('SleepEntry').ids.start_hour.text = formatted_time

    def on_time_save_end_hour(self, instance, time):
        formatted_time = time.strftime('%H:%M')
        self.root.get_screen('SleepEntry').ids.end_hour.text = formatted_time

    def show_time_picker_for_feed(self):
        time_dialog = MDTimePicker()
        time_dialog.set_time(datetime.now())
        time_dialog.bind(time=self.on_time_save_feed)
        time_dialog.open()

    def on_time_save_feed(self, instance, time):
        formatted_time = time.strftime('%H:%M')
        self.root.get_screen('FeedingEntry').ids.feed_hour.text = formatted_time

    def create_account(self, username, password, first_name, last_name):
        conn = sqlite3.connect('babylingo.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE username=?", (username,))
        if c.fetchone():
            self.root.get_screen('Register').ids.username.line_color_normal = self.theme_cls.error_color
            self.root.get_screen('Register').ids.username.helper_text = "This username already exists"
            conn.close()
            return

        if username and password:
            c.execute("INSERT INTO users (username, password, first_name, last_name) VALUES (?, ?, ?, ?)",
                      (username, password, first_name, last_name))
            conn.commit()

            c.execute("SELECT id FROM users WHERE username=?", (username,))
            result = c.fetchone()
            self.current_user_id = result[0]

            conn.commit()
            conn.close()

            self.dialog = MDDialog(
                title="Success",
                text="Account created successfully!",
                buttons=[
                    MDFlatButton(
                        text="Close",
                        on_release=self.close_dialog_to_welcome
                    )
                ]
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                title="Error",
                text="Username or password cannot be empty",
                buttons=[
                    MDFlatButton(
                        text="Close",
                        on_release=self.close_dialog
                    )
                ]
            )
            self.dialog.open()
        conn.close()

    def login(self, username, password):
        err = False
        conn = sqlite3.connect('babylingo.db')
        c = conn.cursor()

        c.execute("SELECT id, password FROM users WHERE username=?", (username,))
        result = c.fetchone()

        if result:
            user_id, stored_password = result
            if password == stored_password:
                self.root.get_screen('Login').ids.login_username.line_color_normal = self.theme_cls.primary_color
                self.root.get_screen('Login').ids.login_password.line_color_normal = self.theme_cls.primary_color
                self.current_user_id = user_id
                self.root.current = 'Home'
            else:
                err = True
        else:
            err = True

        if err:
            if username and password:
                self.root.get_screen('Login').ids.login_username.line_color_normal = self.theme_cls.error_color
                self.root.get_screen('Login').ids.login_password.line_color_normal = self.theme_cls.error_color
                self.dialog = MDDialog(
                    title="Error",
                    text="Incorect username or password!",
                    buttons=[
                        MDFlatButton(
                            text="Try again",
                            on_release=self.close_dialog_to_login
                        )
                    ]
                )
                self.dialog.open()
            elif not username and not password:
                self.root.get_screen('Login').ids.login_username.line_color_normal = self.theme_cls.error_color
                self.root.get_screen('Login').ids.login_password.line_color_normal = self.theme_cls.error_color
            elif not username:
                self.root.get_screen('Login').ids.login_username.line_color_normal = self.theme_cls.error_color
                self.root.get_screen('Login').ids.login_password.line_color_normal = self.theme_cls.primary_color
            elif not password:
                self.root.get_screen('Login').ids.login_password.line_color_normal = self.theme_cls.error_color
                self.root.get_screen('Login').ids.login_username.line_color_normal = self.theme_cls.primary_color

        conn.close()


if __name__ == "__main__":
    DemoApp().run()
